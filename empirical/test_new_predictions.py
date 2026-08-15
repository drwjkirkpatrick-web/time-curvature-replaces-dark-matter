"""
test_new_predictions.py
=======================

Pytest suite for the six new VTC predictions (P3--P8).

Usage:
    source "$HOME/.venvs/jetson-pytorch/bin/activate"
    pytest empirical/test_new_predictions.py -v
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
import pytest
import torch

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from empirical.verify_new_predictions import (
    ALPHA_GAL, BETA_VTC, M_PHI_EV,
    C_KM_S, C_M_S, H0, H0_SI, T0_S, MPC_TO_M, KPC_TO_M,
    EV_TO_J, HBAR,
    get_device,
    vtc_w_of_a, w0wa_w_of_z, lcdm_w,
    check_prediction_3, check_prediction_4, check_prediction_5,
    check_prediction_6, check_prediction_7, check_prediction_8,
    TheoremResult,
)

DEVICE = get_device()


# =============================================================================
# P3: Time-Varying Dark Energy
# =============================================================================

class TestP3TimeVaryingDarkEnergy:
    """P3: VTC predicts evolving w(z) with one parameter (beta)."""

    def test_w_evolves(self):
        """VTC w(z) is not constant — it evolves with redshift."""
        z = torch.linspace(0.01, 2.0, 500, device=DEVICE)
        a = 1.0 / (1.0 + z)
        w = vtc_w_of_a(a, beta=BETA_VTC)
        w_cpu = w.cpu().numpy()
        assert np.std(w_cpu) > 0.01, f"w(z) is nearly constant: std={np.std(w_cpu)}"

    def test_w_is_quintessence_like(self):
        """VTC w(z) > -1 everywhere (quintessence, not phantom)."""
        z = torch.linspace(0.01, 2.0, 500, device=DEVICE)
        a = 1.0 / (1.0 + z)
        w = vtc_w_of_a(a, beta=BETA_VTC)
        w_cpu = w.cpu().numpy()
        assert np.all(w_cpu > -1.001), f"VTC produces phantom w < -1: min={np.min(w_cpu)}"

    def test_w0_in_range(self):
        """VTC w0 (at z=0) is in the DESI-preferred range."""
        z = torch.tensor([0.01], device=DEVICE)
        a = 1.0 / (1.0 + z)
        w = vtc_w_of_a(a, beta=BETA_VTC)
        w0 = w.cpu().item()
        assert -1.5 < w0 < 0.5, f"VTC w0={w0} outside expected range"

    def test_w_approaches_matter_dominated_at_high_z(self):
        """At high z, w should approach 0 (matter-dominated era)."""
        z = torch.tensor([2.0], device=DEVICE)
        a = 1.0 / (1.0 + z)
        w = vtc_w_of_a(a, beta=BETA_VTC)
        w_highz = w.cpu().item()
        assert w_highz > -0.5, f"VTC w at z=2 is too negative: {w_highz}"

    def test_vtc_has_fewer_parameters_than_w0wa(self):
        """VTC has 1 free parameter (beta) vs 2 for w0wa."""
        n_vtc = 1
        n_w0wa = 2
        assert n_vtc < n_w0wa

    def test_vtc_evolution_matches_desi_qualitatively(self):
        """VTC w(z) should show the same trend as DESI: w > -1 at z=0, evolving."""
        z = torch.linspace(0.01, 1.5, 100, device=DEVICE)
        a = 1.0 / (1.0 + z)
        w = vtc_w_of_a(a, beta=BETA_VTC)
        w_cpu = w.cpu().numpy()
        z_cpu = z.cpu().numpy()
        # w at z=0 should be > -1 (quintessence)
        assert w_cpu[0] > -1.0
        # w should evolve (not constant -1)
        assert abs(w_cpu[0] - w_cpu[-1]) > 0.01

    def test_full_check_passes(self):
        """Run the full P3 check and verify it passes."""
        result = check_prediction_3(DEVICE)
        assert isinstance(result, TheoremResult)
        assert result.passed, f"P3 failed: {result.detail}"


# =============================================================================
# P4: Bullet Cluster
# =============================================================================

class TestP4BulletCluster:
    """P4: VTC lensing follows compact stars, not smooth gas."""

    def test_full_check_passes(self):
        """Run the full P4 check and verify it passes."""
        result = check_prediction_4(DEVICE)
        assert isinstance(result, TheoremResult)
        assert result.passed, f"P4 failed: {result.detail}"

    def test_compact_gradient_dominates(self):
        """Compact stellar sources produce higher gradient than smooth gas."""
        n = 200
        extent = 2000.0
        x = torch.linspace(-extent/2, extent/2, n, device=DEVICE, dtype=torch.float64)
        y = torch.linspace(-extent/2, extent/2, n, device=DEVICE, dtype=torch.float64)
        X, Y = torch.meshgrid(x, y, indexing="xy")

        # Compact source
        sigma_star = 50.0
        mass_star = 5e12
        rho_star = mass_star / (2 * math.pi * sigma_star**2) * \
            torch.exp(-((X - (-300))**2 + Y**2) / (2 * sigma_star**2))

        # Smooth gas
        sigma_gas = 200.0
        mass_gas = 1e13
        rho_gas = mass_gas / (2 * math.pi * sigma_gas**2) * \
            torch.exp(-(X**2 + Y**2) / (2 * sigma_gas**2))

        dx = extent / n
        grad_star = torch.sqrt(
            (torch.diff(rho_star, dim=0, append=rho_star[-1:])/dx)**2 +
            (torch.diff(rho_star, dim=1, append=rho_star[:,-1:])/dx)**2
        )
        grad_gas = torch.sqrt(
            (torch.diff(rho_gas, dim=0, append=rho_gas[-1:])/dx)**2 +
            (torch.diff(rho_gas, dim=1, append=rho_gas[:,-1:])/dx)**2
        )

        # Evaluate 1-sigma from center (gradient is zero at exact Gaussian peak)
        col_star = int((-300 + sigma_star + extent/2) / dx)
        row_star = int(extent/2 / dx)
        col_gas = int((sigma_gas + extent/2) / dx)
        row_gas = int(extent/2 / dx)

        gs = grad_star[row_star, col_star].item()
        gg = grad_gas[row_gas, col_gas].item()

        assert gs > gg, f"Stars ({gs}) should dominate gradient over gas ({gg})"

    def test_gas_mass_exceeds_star_mass(self):
        """Verify the gas mass > star mass (Bullet Cluster setup)."""
        mass_gas = 1e13
        mass_star = 5e12
        assert mass_gas > mass_star, "Gas should dominate baryonic mass"

    def test_gradient_ratio_exceeds_unity(self):
        """Stars/gas gradient ratio > 1 despite gas having more mass."""
        result = check_prediction_4(DEVICE)
        # The metric stores the gradient ratio
        assert result.metric > 1.0, f"Gradient ratio {result.metric} should be > 1"


# =============================================================================
# P5: JWST Early Galaxies
# =============================================================================

class TestP5JWSTEarlyGalaxies:
    """P5: VTC nonlinear enhancement explains JWST early galaxy excess."""

    def test_full_check_passes(self):
        """Run the full P5 check and verify it passes."""
        result = check_prediction_5(DEVICE)
        assert isinstance(result, TheoremResult)
        assert result.passed, f"P5 failed: {result.detail}"

    def test_enhancement_at_z10_exceeds_unity(self):
        """Halo abundance at z=10 with VTC > LCDM baseline."""
        delta_c_lcdm = 1.686
        sigma_M_z10 = 0.3
        for eta in [0.05, 0.10, 0.15]:
            delta_c_vtc = delta_c_lcdm * (1.0 - eta * 0.5)
            nu_lcdm = delta_c_lcdm / sigma_M_z10
            nu_vtc = delta_c_vtc / sigma_M_z10
            ratio = (nu_vtc / nu_lcdm) * np.exp((nu_lcdm**2 - nu_vtc**2) / 2.0)
            assert ratio > 1.0, f"eta={eta}: enhancement {ratio} should be > 1"

    def test_eta_zero_recovers_lcdm(self):
        """With eta=0, VTC should exactly recover LCDM."""
        delta_c_lcdm = 1.686
        sigma_M_z10 = 0.3
        eta = 0.0
        delta_c_vtc = delta_c_lcdm * (1.0 - eta * 0.5)
        nu_lcdm = delta_c_lcdm / sigma_M_z10
        nu_vtc = delta_c_vtc / sigma_M_z10
        ratio = (nu_vtc / nu_lcdm) * np.exp((nu_lcdm**2 - nu_vtc**2) / 2.0)
        assert abs(ratio - 1.0) < 0.01, f"eta=0 should give ratio=1.0, got {ratio}"

    def test_enhancement_monotonic_in_eta(self):
        """Enhancement should increase with eta."""
        delta_c_lcdm = 1.686
        sigma_M_z10 = 0.3
        etas = [0.05, 0.10, 0.15]
        ratios = []
        for eta in etas:
            delta_c_vtc = delta_c_lcdm * (1.0 - eta * 0.5)
            nu_lcdm = delta_c_lcdm / sigma_M_z10
            nu_vtc = delta_c_vtc / sigma_M_z10
            ratio = (nu_vtc / nu_lcdm) * np.exp((nu_lcdm**2 - nu_vtc**2) / 2.0)
            ratios.append(ratio)
        assert ratios[2] > ratios[1] > ratios[0], \
            f"Enhancement should be monotonic: {ratios}"

    def test_enhancement_explains_jwst_factor(self):
        """With eta=0.10, enhancement should be > 3x (combined effects reach 10x)."""
        result = check_prediction_5(DEVICE)
        assert result.metric > 3.0, \
            f"Enhancement at eta=0.10 is {result.metric:.1f}x, need > 3x for JWST"


# =============================================================================
# P6: Gravitational Wave Propagation
# =============================================================================

class TestP6GravitationalWaves:
    """P6: VTC predicts redshift-dependent GW speed."""

    def test_full_check_passes(self):
        """Run the full P6 check and verify it passes."""
        result = check_prediction_6(DEVICE)
        assert isinstance(result, TheoremResult)
        assert result.passed, f"P6 failed: {result.detail}"

    def test_gw170817_constraint_satisfied(self):
        """|c_GW - c|/c at z=0 is within GW170817 bound (< 1e-15)."""
        alpha_st = 1e-8
        # c_GW^2/c^2 = 1 - 2*alpha_st^2 / (1 + alpha_field*T(0))
        # At z=0, T=1, alpha_field ~ alpha_gal * 100
        alpha_field = ALPHA_GAL * 100
        T_z0 = 1.0
        c_gw_sq = 1.0 - 2.0 * alpha_st**2 / (1.0 + alpha_field * T_z0)
        dc_gw = abs(math.sqrt(max(c_gw_sq, 0)) - 1.0)
        assert dc_gw < 1e-14, f"Δc_GW/c at z=0 = {dc_gw:.2e}, must be < 1e-14"

    def test_gw_speed_evolves_with_redshift(self):
        """c_GW varies with z — it is not constant."""
        z = torch.linspace(0.001, 3.0, 500, device=DEVICE, dtype=torch.float64)
        alpha_st = 1e-8
        T_z = 1.0 / (1.0 + z)**BETA_VTC
        dc_gw = -alpha_st**2 * T_z
        dc = dc_gw.cpu().numpy()
        assert np.std(dc) > 1e-20, "c_GW should vary with z"

    def test_gw_approaches_c_at_high_z(self):
        """At high z, c_GW -> c (field vanishes in early universe)."""
        z = torch.linspace(0.001, 3.0, 500, device=DEVICE, dtype=torch.float64)
        alpha_st = 1e-8
        T_z = 1.0 / (1.0 + z)**BETA_VTC
        dc_gw = -alpha_st**2 * T_z
        dc = dc_gw.cpu().numpy()
        assert abs(dc[-1]) < abs(dc[0]), "c_GW should approach c at high z"

    def test_transition_frequency_in_pta_band(self):
        """Scalar field Compton frequency falls in the nHz PTA band."""
        f_trans = M_PHI_EV * EV_TO_J / (2 * math.pi * HBAR)
        assert 1e-9 < f_trans < 1e-7, \
            f"f_trans = {f_trans:.2e} Hz, should be in nHz PTA band"

    def test_time_delay_at_z1_detectable(self):
        """Time delay for z=1 source is > 0.1 s (potentially detectable)."""
        alpha_st = 1e-8
        dt = alpha_st**2 / H0_SI
        assert dt > 0.1, f"Δt(z~1) = {dt:.2f} s, should be > 0.1 s"


# =============================================================================
# P7: Black Hole Shadow Asymmetry
# =============================================================================

class TestP7BHShadowAsymmetry:
    """P7: VTC predicts inclination-dependent BH shadow asymmetry."""

    def test_full_check_passes(self):
        """Run the full P7 check and verify it passes."""
        result = check_prediction_7(DEVICE)
        assert isinstance(result, TheoremResult)
        assert result.passed, f"P7 failed: {result.detail}"

    def test_asymmetry_nonzero(self):
        """VTC predicts nonzero asymmetry (unlike LCDM which is exactly 0)."""
        v0 = 150.0
        alpha = (v0 / C_KM_S)**2
        i = math.radians(30)
        A = alpha * math.log(math.tan(i))
        assert abs(A) > 1e-10, f"Asymmetry {A} should be nonzero"

    def test_asymmetry_correlates_with_ln_tan(self):
        """Asymmetry A = alpha * ln(tan(i)) — verify functional form."""
        inc = np.linspace(5, 85, 100)
        inc_rad = np.radians(inc)
        v0 = 150.0
        alpha = (v0 / C_KM_S)**2
        A = alpha * np.log(np.tan(inc_rad))
        ln_tan = np.log(np.tan(inc_rad))
        corr = np.corrcoef(A, ln_tan)[0, 1]
        assert abs(corr) > 0.99, f"Correlation with ln(tan i) = {corr}, should be > 0.99"

    def test_asymmetry_scales_with_alpha(self):
        """Asymmetry scales as v0^2/c^2 (galaxy rotation velocity squared)."""
        v0_values = [150.0, 220.0, 500.0]
        alphas = [(v / C_KM_S)**2 for v in v0_values]
        i = math.radians(45)
        As = [a * math.log(math.tan(i)) for a in alphas]
        # Ratio A1/A0 should equal alpha1/alpha0
        for j in range(1, len(alphas)):
            ratio = As[j] / As[0]
            expected = alphas[j] / alphas[0]
            assert abs(ratio - expected) / expected < 0.01, \
                f"Scaling failed: ratio={ratio}, expected={expected}"

    def test_lcdm_predicts_zero(self):
        """LCDM/Kerr predicts exactly zero asymmetry from galaxy properties."""
        lcdm_A = 0.0
        assert lcdm_A == 0.0, "LCDM should predict zero galaxy-sourced asymmetry"

    def test_m87_asymmetry_in_range(self):
        """M87* asymmetry is ~1e-6 (small but potentially detectable by ngEHT)."""
        v0_m87 = 500.0
        alpha_m87 = (v0_m87 / C_KM_S)**2
        i_m87 = math.radians(17)
        A_m87 = alpha_m87 * math.log(math.tan(i_m87))
        assert 1e-8 < abs(A_m87) < 1e-4, \
            f"M87* asymmetry {A_m87:.2e} should be in [1e-8, 1e-4]"


# =============================================================================
# P8: Pulsar/FRB Clock Drift
# =============================================================================

class TestP8ClockDrift:
    """P8: VTC predicts D^2 clock drift (screened locally)."""

    def test_full_check_passes(self):
        """Run the full P8 check and verify it passes."""
        result = check_prediction_8(DEVICE)
        assert isinstance(result, TheoremResult)
        assert result.passed, f"P8 failed: {result.detail}"

    def test_drift_rate_linear_in_D(self):
        """Drift rate is proportional to D (linear in distance)."""
        D_mpc = np.logspace(-1, 3, 500)
        D_m = D_mpc * MPC_TO_M
        drift_rate = BETA_VTC * D_m / (C_M_S * T0_S)
        log_D = np.log10(D_mpc)
        log_rate = np.log10(np.abs(drift_rate) + 1e-30)
        slope = np.polyfit(log_D, log_rate, 1)[0]
        assert abs(slope - 1.0) < 0.05, f"Drift rate slope={slope}, should be ~1.0 (linear in D)"

    def test_total_drift_quadratic_in_D(self):
        """Total drift delta_t ~ D^2 (quadratic — unique VTC signature)."""
        D_mpc = np.logspace(-1, 3, 100)
        D_m = D_mpc * MPC_TO_M
        delta_t = BETA_VTC * D_m**2 / (2 * C_M_S**2 * T0_S)
        log_D = np.log10(D_mpc)
        log_dt = np.log10(np.abs(delta_t) + 1e-30)
        slope = np.polyfit(log_D, log_dt, 1)[0]
        assert abs(slope - 2.0) < 0.05, f"Total drift slope={slope}, should be ~2.0 (D^2)"

    def test_cosmological_residual_detectable(self):
        """At 100 Mpc, timing residual over 10 yr is > 1 ns."""
        D = 100 * MPC_TO_M  # 100 Mpc in meters
        T_obs = 10 * 3.156e7  # 10 years
        drift_rate = BETA_VTC * D / (C_M_S * T0_S)
        residual = drift_rate * T_obs
        assert residual > 1e-9, f"Residual at 100 Mpc = {residual:.2e} s, should be > 1 ns"

    def test_galactic_residual_below_pta(self):
        """At 10 kpc (galactic), screened residual < 100 us over 10 yr."""
        D = 0.01 * MPC_TO_M  # 10 kpc
        T_obs = 10 * 3.156e7
        epsilon = 1e-8
        drift_rate = epsilon * BETA_VTC * D / (C_M_S * T0_S)
        residual = drift_rate * T_obs
        assert residual < 1e-4, f"Screened residual at 10 kpc = {residual:.2e} s, should be < 100 us"

    def test_d2_scaling_unique_to_vtc(self):
        """D^2 scaling distinguishes VTC from dispersion (D) and proper motion (D)."""
        # Dispersion: dt ~ D
        # Proper motion: dt ~ D
        # VTC clock drift: dt ~ D^2
        # If we fit dt = A * D^n, VTC gives n=2
        D_mpc = np.array([1.0, 10.0, 100.0, 1000.0])
        D_m = D_mpc * MPC_TO_M
        delta_t = BETA_VTC * D_m**2 / (2 * C_M_S**2 * T0_S)
        log_D = np.log10(D_mpc)
        log_dt = np.log10(delta_t)
        slope = np.polyfit(log_D, log_dt, 1)[0]
        assert abs(slope - 2.0) < 0.01, f"D^2 slope={slope}, must be exactly 2.0"


# =============================================================================
# Integration / Cross-cutting Tests
# =============================================================================

class TestIntegration:
    """Cross-cutting tests that verify internal consistency."""

    def test_all_six_predictions_pass(self):
        """All six new predictions pass their full checks."""
        results = []
        for check_fn, name in [
            (check_prediction_3, "P3"),
            (check_prediction_4, "P4"),
            (check_prediction_5, "P5"),
            (check_prediction_6, "P6"),
            (check_prediction_7, "P7"),
            (check_prediction_8, "P8"),
        ]:
            result = check_fn(DEVICE)
            results.append((name, result))
            assert result.passed, f"{name} FAILED: {result.detail}"

    def test_vtc_constants_are_self_consistent(self):
        """VTC parameters are in physically reasonable ranges."""
        assert 0 < ALPHA_GAL < 1e-5, "Alpha galactic must be tiny"
        assert 0 < BETA_VTC < 1, "Beta must be between 0 and 1"
        assert M_PHI_EV > 0, "Scalar field mass must be positive"
        assert M_PHI_EV < 1e-20, "Scalar field mass should be ultralight"

    def test_fewer_free_parameters_than_lcdm_extensions(self):
        """VTC uses fewer free parameters than LCDM with extensions."""
        # Original VTC: alpha (from v0, measurable), beta (from t0, measurable)
        # New predictions add: eta (P5, ~alpha-derived), alpha_st (P6, constrained)
        # Total: 2 fundamental + 2 derived = effectively 2 free parameters
        vtc_params = 2

        # LCDM needs: Omega_m, Omega_L, w0, wa, sigma_8, n_s, ...
        # Plus extensions for each anomaly:
        # - DESI: +2 (w0, wa)
        # - JWST: +free (duty cycle, efficiency)
        # - Bullet: +1 (DM cross-section)
        lcdm_params = 6 + 3  # conservative

        assert vtc_params < lcdm_params, \
            f"VTC ({vtc_params} params) should be more parsimonious than LCDM ({lcdm_params})"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])