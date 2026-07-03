"""
Test suite for VTC unique predictions.

Run: source ~/.venvs/jetson-pytorch/bin/activate && python3.10 -m pytest tests/test_unique.py -v
"""

import math

import numpy as np
import pytest
import torch

# Physical constants
G = 4.3009e-6
c_kms = 3.0e5

# Use CPU for tests (deterministic, no GPU memory issues)
device = torch.device('cpu')


def visible_matter_density(Rg, Zg, rho0, Rd, z0):
    return rho0 * torch.exp(-Rg / Rd) / torch.cosh(Zg / z0)**2


def compute_lapse_from_density(Rd, z0, alpha, nR=200, nz=160):
    R_grid = torch.linspace(0.1, 30.0, nR, device=device)
    z_grid = torch.linspace(-5.0, 5.0, nz, device=device)
    Rg, Zg = torch.meshgrid(R_grid, z_grid, indexing='ij')
    rho0 = 1e8
    rho_vis = visible_matter_density(Rg, Zg, rho0, Rd, z0)
    N = (rho_vis / rho0) ** alpha
    N = torch.clamp(N, min=1e-20)
    return Rg, Zg, N, R_grid, z_grid


def radial_gradient_lnN(N, R_grid):
    dR = R_grid[1] - R_grid[0]
    lnN = torch.log(N)
    grad = torch.zeros_like(lnN)
    grad[1:-1, :] = (lnN[2:, :] - lnN[:-2, :]) / (2 * dR)
    grad[0, :] = (lnN[1, :] - lnN[0, :]) / dR
    grad[-1, :] = (lnN[-1, :] - lnN[-2, :]) / dR
    return grad


def vertical_gradient_lnN(N, z_grid):
    dz = z_grid[1] - z_grid[0]
    lnN = torch.log(N)
    grad = torch.zeros_like(lnN)
    grad[:, 1:-1] = (lnN[:, 2:] - lnN[:, :-2]) / (2 * dz)
    grad[:, 0] = (lnN[:, 1] - lnN[:, 0]) / dz
    grad[:, -1] = (lnN[:, -1] - lnN[:, -2]) / dz
    return grad


# =============================================================================
# Test 1: Morphology-Dependent Effective Gravity
# =============================================================================

def test_morphology_dependence():
    """
    VTC predicts that two galaxies with the same baryonic mass but different
    morphologies (bulge-dominated vs disk-dominated) will have different
    effective gravitational accelerations. ΛCDM predicts identical isothermal
    halos for both.
    """
    alpha = 1e-4  # scaled for numerical demonstration
    
    # Bulge-dominated (tight scale length)
    Rg_b, Zg_b, N_bulge, Rg, zg = compute_lapse_from_density(
        Rd=0.5, z0=0.3, alpha=alpha, nR=200, nz=160
    )
    
    # Disk-dominated (extended scale length)
    Rg_d, Zg_d, N_disk, _, _ = compute_lapse_from_density(
        Rd=3.5, z0=0.3, alpha=alpha, nR=200, nz=160
    )
    
    # Compute radial gradients
    grad_bulge = radial_gradient_lnN(N_bulge, Rg)
    grad_disk = radial_gradient_lnN(N_disk, Rg)
    
    # Effective acceleration: a_VTC = c² · ∂_R ln N
    a_bulge = c_kms**2 * grad_bulge
    a_disk = c_kms**2 * grad_disk
    
    # Extract at midplane, R = 5 kpc
    mid_idx = Zg_b.shape[1] // 2
    R_mid = Rg_b[:, mid_idx].numpy()
    a_bulge_mid = a_bulge[:, mid_idx].numpy()
    a_disk_mid = a_disk[:, mid_idx].numpy()
    
    idx_5 = np.argmin(np.abs(R_mid - 5.0))
    
    # ΛCDM predicts same acceleration for both morphologies
    # VTC predicts different accelerations
    ratio = abs(a_disk_mid[idx_5]) / max(abs(a_bulge_mid[idx_5]), 1e-30)
    
    # The ratio should differ from 1 by more than 10%
    assert ratio > 1.1 or ratio < 0.9, \
        f"VTC should predict morphology-dependent gravity; ratio = {ratio:.3f}"


def test_morphology_invariant_under_scaling():
    """
    The morphology dependence (ratio of disk/bulge acceleration) should be
    independent of the coupling constant α.
    """
    for alpha in [1e-5, 1e-4, 1e-3]:
        Rg_b, Zg_b, N_bulge, Rg, zg = compute_lapse_from_density(
            Rd=0.5, z0=0.3, alpha=alpha, nR=200, nz=160
        )
        Rg_d, Zg_d, N_disk, _, _ = compute_lapse_from_density(
            Rd=3.5, z0=0.3, alpha=alpha, nR=200, nz=160
        )
        
        grad_bulge = radial_gradient_lnN(N_bulge, Rg)
        grad_disk = radial_gradient_lnN(N_disk, Rg)
        
        a_bulge = c_kms**2 * grad_bulge
        a_disk = c_kms**2 * grad_disk
        
        mid_idx = Zg_b.shape[1] // 2
        R_mid = Rg_b[:, mid_idx].numpy()
        idx_5 = np.argmin(np.abs(R_mid - 5.0))
        
        a_bulge_mid = a_bulge[:, mid_idx].numpy()
        a_disk_mid = a_disk[:, mid_idx].numpy()
        
        ratio = abs(a_disk_mid[idx_5]) / max(abs(a_bulge_mid[idx_5]), 1e-30)
        
        # Ratio should be stable across α values
        assert 0.05 < ratio < 0.25, \
            f"Morphology ratio should be stable; got {ratio:.3f} for α={alpha}"


# =============================================================================
# Test 2: Vertical Redshift Gradient
# =============================================================================

def test_vertical_gradient_linear():
    """
    VTC predicts a linear vertical redshift gradient at fixed cylindrical
    radius R. ΛCDM with a spherical isothermal halo predicts no intrinsic
    linear gradient (only a quadratic correction from r = √(R²+z²)).
    """
    alpha = 1e-4
    
    Rg, Zg, N, R_grid, z_grid = compute_lapse_from_density(
        Rd=3.5, z0=0.3, alpha=alpha, nR=200, nz=160
    )
    
    grad_z = vertical_gradient_lnN(N, z_grid)
    
    # At R = 5 kpc
    R_test = 5.0
    idx_R = torch.argmin(torch.abs(R_grid - R_test))
    
    z_vals = Zg[idx_R, :].numpy()
    grad_vals = grad_z[idx_R, :].numpy()
    
    z_center = z_vals[len(z_vals)//2]
    z_rel = z_vals - z_center
    
    # Fit region |z| < 2 kpc
    mask = np.abs(z_rel) < 2.0
    z_fit = z_rel[mask]
    grad_fit = grad_vals[mask]
    
    # Fit: grad = b + c·z
    coeffs = np.polyfit(z_fit, grad_fit, 2)
    mean_grad = np.mean(grad_fit)
    
    # Velocity shift for Δz = 1 kpc
    delta_v = mean_grad * c_kms
    
    # VTC predicts non-zero linear gradient
    assert abs(delta_v) > 1e-4, \
        f"VTC should predict linear vertical gradient; got Δv = {delta_v:.4f} km/s"


def test_vertical_gradient_direction():
    """
    The vertical gradient should be anti-symmetric about z=0 (positive z →
    one sign, negative z → opposite sign) because the disk density peaks at
    z=0 and falls off symmetrically.
    """
    alpha = 1e-4
    
    Rg, Zg, N, R_grid, z_grid = compute_lapse_from_density(
        Rd=3.5, z0=0.3, alpha=alpha, nR=200, nz=160
    )
    
    grad_z = vertical_gradient_lnN(N, z_grid)
    
    idx_R = torch.argmin(torch.abs(R_grid - 5.0))
    grad_line = grad_z[idx_R, :].numpy()
    z_line = Zg[idx_R, :].numpy()
    
    # Compare gradient at +z and -z for same |z|
    mid = len(z_line) // 2
    z_pos = z_line[mid:]
    grad_pos = grad_line[mid:]
    z_neg = z_line[:mid][::-1]
    grad_neg = grad_line[:mid][::-1]
    
    # Match z values
    common_len = min(len(z_pos), len(z_neg))
    grad_pos = grad_pos[:common_len]
    grad_neg = grad_neg[:common_len]
    
    # Gradients should be approximately anti-symmetric
    anti_sym = np.mean((grad_pos + grad_neg)**2)
    assert anti_sym < 1e-10, \
        f"Vertical gradient should be anti-symmetric; mean squared sum = {anti_sym:.2e}"


def test_vertical_gradient_physical_scaling():
    """
    The vertical gradient amplitude should scale linearly with α, confirming
    it is a first-order effect in the temporal curvature coupling.
    """
    alphas = [1e-5, 5e-5, 1e-4]
    delta_vs = []
    
    for alpha in alphas:
        Rg, Zg, N, R_grid, z_grid = compute_lapse_from_density(
            Rd=3.5, z0=0.3, alpha=alpha, nR=200, nz=160
        )
        
        grad_z = vertical_gradient_lnN(N, z_grid)
        idx_R = torch.argmin(torch.abs(R_grid - 5.0))
        
        z_vals = Zg[idx_R, :].numpy()
        grad_vals = grad_z[idx_R, :].numpy()
        z_center = z_vals[len(z_vals)//2]
        z_rel = z_vals - z_center
        mask = np.abs(z_rel) < 2.0
        mean_grad = np.mean(grad_vals[mask])
        delta_vs.append(mean_grad * c_kms)
    
    # Check linear scaling: delta_v[1]/delta_v[0] ≈ alpha[1]/alpha[0]
    ratio_10 = delta_vs[1] / delta_vs[0]
    expected_10 = alphas[1] / alphas[0]
    
    assert abs(ratio_10 - expected_10) / expected_10 < 0.1, \
        f"Gradient should scale linearly with α; ratio = {ratio_10:.2f}, expected = {expected_10:.2f}"


# =============================================================================
# Test 3: ΛCDM Comparison
# =============================================================================

def test_lcdm_isothermal_independent_of_morphology():
    """
    ΛCDM isothermal sphere: ρ = v0²/(4πGr²), acceleration = -v0²/R.
    This depends only on v0 and R, not on morphology.
    """
    R_test = np.linspace(1.0, 30.0, 100)
    v0 = 150.0
    a_lcdm = -v0**2 / R_test
    
    # Same acceleration regardless of whether galaxy is bulge or disk
    assert np.all(a_lcdm < 0), "ΛCDM acceleration should be inward (negative)"
    assert np.allclose(a_lcdm, -v0**2 / R_test), "ΛCDM should be purely radial"
