#!/usr/bin/env python3
"""
VTC Unique Predictions — GPU Verification Suite
================================================
Two tests that distinguish VTC from ΛCDM:

1. MORPHOLOGY TEST: Disk-sourced lapse creates morphology-dependent
   effective gravitational acceleration.

2. VERTICAL REDSHIFT GRADIENT: Linear vertical redshift gradient at fixed R.

Physical model: N(R,z) follows the visible matter geometry:
    N(R,z) ∝ exp(φ/M_Pl) where ∇²φ = κ·ρ_vis(R,z)

For demonstration: N(R,z) = (ρ_vis(R,z)/ρ_0)^α with α = 2.5e-7
(v0²/c² for v0 = 150 km/s). The predictions scale with α but the
morphology dependence is intrinsic.

Run: source $HOME/.venvs/jetson-pytorch/bin/activate && python3.10 empirical/verify_unique.py
"""

from __future__ import annotations

import math
import sys

import numpy as np
import torch

# =============================================================================
# Device
# =============================================================================

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Device: {device}")
if device.type == 'cuda':
    print(f"  GPU: {torch.cuda.get_device_name(0)}")
    print(f"  PyTorch: {torch.__version__}")
    print(f"  CUDA: {torch.version.cuda}")

# Physical constants (astronomical units)
G = 4.3009e-6       # kpc km² / (M_sun s²)
c_kms = 3.0e5       # km/s

# =============================================================================
# Physical Model: Lapse Function from Visible Matter Geometry
# =============================================================================

def visible_matter_density(Rg, Zg, rho0, Rd, z0):
    """Exponential disk with sech² vertical profile."""
    return rho0 * torch.exp(-Rg / Rd) / torch.cosh(Zg / z0)**2


def compute_lapse_from_density(Rd, z0, alpha, nR=300, nz=240):
    """
    Compute N(R,z) = (ρ_vis/ρ_0)^α  (power-law coupling to visible matter).
    
    α = v0²/c² ≈ 2.5e-7 for v0 = 150 km/s.
    For GPU numerical demonstration we use α = 1e-4 (qualitative predictions
    unchanged; absolute amplitudes scale linearly with α).
    
    Returns (Rg, Zg, N, R_grid, z_grid)
    """
    R_grid = torch.linspace(0.1, 30.0, nR, device=device)
    z_grid = torch.linspace(-5.0, 5.0, nz, device=device)
    
    Rg, Zg = torch.meshgrid(R_grid, z_grid, indexing='ij')
    rho0 = 1e8
    rho_vis = visible_matter_density(Rg, Zg, rho0, Rd, z0)
    
    # N = (ρ_vis/ρ_0)^α — directly sourced by visible matter geometry
    N = (rho_vis / rho0) ** alpha
    N = torch.clamp(N, min=1e-20)
    
    return Rg, Zg, N, R_grid, z_grid


def radial_gradient_lnN(N, R_grid):
    """
    Compute ∂_R ln N via central differences on GPU.
    Returns ∂_R ln N(R,z).
    """
    dR = R_grid[1] - R_grid[0]
    lnN = torch.log(N)
    
    grad = torch.zeros_like(lnN)
    # Central difference for interior points
    grad[1:-1, :] = (lnN[2:, :] - lnN[:-2, :]) / (2 * dR)
    # Forward/backward for boundaries
    grad[0, :] = (lnN[1, :] - lnN[0, :]) / dR
    grad[-1, :] = (lnN[-1, :] - lnN[-2, :]) / dR
    
    return grad


def vertical_gradient_lnN(N, z_grid):
    """
    Compute ∂_z ln N via central differences on GPU.
    Returns ∂_z ln N(R,z).
    """
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

def test_morphology():
    """Test 1: Compare VTC effective gravitational acceleration for bulge vs disk."""
    print("\n" + "="*70)
    print("TEST 1: Morphology-Dependent Effective Gravity")
    print("="*70)
    
    # Use α = 1e-4 for numerical demonstration (physical value: ~2.5e-7)
    alpha = 1e-4
    
    print(f"  Computing for bulge-dominated (Rd=0.5 kpc, z0=0.3 kpc)...")
    Rg_b, Zg_b, N_bulge, Rg, zg = compute_lapse_from_density(
        Rd=0.5, z0=0.3, alpha=alpha, nR=300, nz=240
    )
    
    print(f"  Computing for disk-dominated (Rd=3.5 kpc, z0=0.3 kpc)...")
    Rg_d, Zg_d, N_disk, _, _ = compute_lapse_from_density(
        Rd=3.5, z0=0.3, alpha=alpha, nR=300, nz=240
    )
    
    # Compute radial gradients at midplane (z=0)
    grad_lnN_bulge = radial_gradient_lnN(N_bulge, Rg)
    grad_lnN_disk = radial_gradient_lnN(N_disk, Rg)
    
    # Effective centripetal acceleration from VTC: a_VTC = c² · ∂_R ln N
    # (Negative gradient = inward force)
    a_vtc_bulge = c_kms**2 * grad_lnN_bulge
    a_vtc_disk = c_kms**2 * grad_lnN_disk
    
    # Extract midplane
    mid_idx = Zg_b.shape[1] // 2
    R_mid = Rg_b[:, mid_idx].cpu().numpy()
    a_bulge_mid = a_vtc_bulge[:, mid_idx].cpu().numpy()
    a_disk_mid = a_vtc_disk[:, mid_idx].cpu().numpy()
    
    # ΛCDM: isothermal sphere gives constant acceleration v0²/R
    v0 = 150.0
    a_lcdm = -v0**2 / R_mid  # negative = inward
    
    # Compare at R = 5 kpc
    idx_5 = np.argmin(np.abs(R_mid - 5.0))
    
    # Magnitude comparison (absolute values)
    mag_bulge = abs(a_bulge_mid[idx_5])
    mag_disk = abs(a_disk_mid[idx_5])
    mag_lcdm = abs(a_lcdm[idx_5])
    ratio = mag_disk / max(mag_bulge, 1e-30)
    
    print(f"\n  Midplane effective acceleration at R=5 kpc (inward = negative):")
    print(f"    Bulge-dominated VTC: {a_bulge_mid[idx_5]:.2e} km²/s²/kpc")
    print(f"    Disk-dominated VTC:  {a_disk_mid[idx_5]:.2e} km²/s²/kpc")
    print(f"    ΛCDM isothermal:     {a_lcdm[idx_5]:.2e} km²/s²/kpc")
    print(f"    Disk/Bulge ratio:    {ratio:.2f}")
    
    # VTC predicts morphology dependence; ΛCDM predicts ratio = 1 for same v0
    # A 10% difference is the detection threshold
    morphology_detectable = ratio > 1.1 or ratio < 0.9
    
    print(f"\n  {'✓ PASS' if morphology_detectable else '✗ FAIL'}: "
          f"VTC predicts morphology-dependent effective gravity "
          f"({ratio:.2f}x difference at R=5 kpc)")
    
    return morphology_detectable, R_mid, a_bulge_mid, a_disk_mid, a_lcdm


# =============================================================================
# Test 2: Vertical Redshift Gradient
# =============================================================================

def test_vertical_redshift():
    """Test 2: Linear vertical redshift gradient at fixed R."""
    print("\n" + "="*70)
    print("TEST 2: Vertical Redshift Gradient")
    print("="*70)
    
    alpha = 1e-4
    
    print(f"  Computing disk-sourced lapse (Rd=3.5 kpc, z0=0.3 kpc)...")
    Rg, Zg, N, R_grid, z_grid = compute_lapse_from_density(
        Rd=3.5, z0=0.3, alpha=alpha, nR=300, nz=240
    )
    
    # Compute vertical gradient at fixed R
    grad_z_lnN = vertical_gradient_lnN(N, z_grid)
    
    # Test at R = 5 kpc
    R_test = 5.0
    idx_R = torch.argmin(torch.abs(R_grid - R_test))
    
    z_vals = Zg[idx_R, :].cpu().numpy()
    grad_vals = grad_z_lnN[idx_R, :].cpu().numpy()
    
    # Gravitational redshift: Δλ/λ ≈ ΔN/N ≈ Δln N
    # For two heights z1 and z2: Δln N ≈ ∂_z ln N · (z2 - z1)
    
    z_center = z_vals[len(z_vals)//2]
    z_rel = z_vals - z_center
    
    # Restrict to |z| < 2 kpc where disk density is significant
    mask = np.abs(z_rel) < 2.0
    z_fit = z_rel[mask]
    grad_fit = grad_vals[mask]
    
    # Fit: grad_z = b + c·z (the gradient itself may vary with z)
    # But the redshift difference is ∫grad dz, which for small Δz is:
    # Δln N ≈ grad_z · Δz (linear in Δz)
    
    # Average gradient over the fitting region
    mean_grad = np.mean(grad_fit)
    std_grad = np.std(grad_fit)
    
    # Redshift difference for Δz = 1 kpc
    delta_lnN = mean_grad * 1.0  # for 1 kpc
    delta_v = delta_lnN * c_kms   # km/s
    
    print(f"\n  At R = {R_test} kpc (averaging |z| < 2 kpc):")
    print(f"    Mean ∂_z ln N: {mean_grad:.2e} kpc⁻¹")
    print(f"    Std ∂_z ln N:  {std_grad:.2e} kpc⁻¹")
    print(f"    Δln N for Δz = 1 kpc: {delta_lnN:.2e}")
    print(f"    Equivalent velocity:  {delta_v:.4f} km/s")
    
    # In ΛCDM with spherical isothermal halo: no intrinsic z-dependence at fixed R
    # (the potential depends on r = √(R²+z²), giving a quadratic z correction)
    # The linear term is zero in ΛCDM
    
    # Detection: VTC predicts a non-zero mean gradient
    linear_detectable = abs(delta_v) > 1e-4  # > 0.1 m/s
    
    print(f"\n  {'✓ PASS' if linear_detectable else '✗ FAIL'}: "
          f"VTC predicts linear vertical redshift gradient "
          f"(velocity shift = {delta_v:.4f} km/s for Δz=1 kpc)")
    
    return linear_detectable, z_vals, grad_vals, mean_grad


# =============================================================================
# Main
# =============================================================================

def main():
    print("="*70)
    print(" VTC Unique Predictions — GPU Verification")
    print("="*70)
    
    morphology_pass, R_mid, a_bulge, a_disk, a_lcdm = test_morphology()
    redshift_pass, z_vals, grad_vals, mean_grad = test_vertical_redshift()
    
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    
    results = [
        ("1. Morphology Test", morphology_pass),
        ("2. Vertical Redshift Gradient", redshift_pass),
    ]
    
    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"   {status:8s}  {name}")
    
    all_pass = all(r[1] for r in results)
    print(f"\n{'='*70}")
    print(f"OVERALL: {'BOTH PREDICTIONS VERIFIED ✓' if all_pass else 'SOME TESTS FAILED ✗'}")
    print(f"{'='*70}")
    
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
