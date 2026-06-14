"""
test_project.py
===============

pytest suite for the Variable Temporal Curvature (VTC) proof project.

Run with:
    source ~/heartlib/.venv/bin/activate
    python -m pytest tests/ -v
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest
import torch

sys.path.insert(0, str(Path(__file__).parent.parent / "empirical"))
from verify import (
    get_device,
    manual_seed,
    visible_mass_profile,
    dark_matter_mass_isothermal,
    v_newtonian,
    v_dark_matter,
    v_vtc,
    lensing_dm_isothermal,
    lensing_vtc,
    hubble_lcdm,
    hubble_vtc,
    GALAXY_V_FLAT,
)


@pytest.fixture(scope="module", autouse=True)
def seed():
    manual_seed(1729)


class TestVisibleMass:
    """Unit tests for visible mass profile."""

    def test_mass_at_zero(self):
        """Mass at r=0 is approximately zero (clamped to 1e-6 kpc gives tiny mass)."""
        r = torch.tensor([0.0])
        m = visible_mass_profile(r)
        # The function clamps r to 1e-6 to avoid division by zero,
        # so mass at "zero" is actually the mass at 1e-6 kpc — extremely small
        assert m.item() < 1e5  # Should be effectively zero on galactic scales

    def test_mass_monotonic(self):
        r = torch.linspace(0.1, 30.0, 100)
        m = visible_mass_profile(r)
        assert torch.all(m[1:] >= m[:-1] - 1e-6)

    def test_mass_saturates(self):
        r = torch.tensor([100.0])
        m = visible_mass_profile(r)
        total = 2.0e10 + 6.0e10  # bulge + disk
        assert m.item() == pytest.approx(total, rel=0.01)


class TestDarkMatterMass:
    """Unit tests for dark matter mass profile."""

    def test_linear_in_radius(self):
        r = torch.tensor([1.0, 2.0, 3.0, 10.0])
        m = dark_matter_mass_isothermal(r, v_flat=150.0)
        # M_DM ~ r, so ratios should be ~ r ratios
        ratios = m[1:] / m[:-1]
        expected = r[1:] / r[:-1]
        assert torch.allclose(ratios, expected, atol=1e-6)


class TestRotationCurves:
    """Tests for rotation curve models."""

    def test_newtonian_decreases_at_large_r(self):
        r = torch.tensor([5.0, 10.0, 20.0, 30.0])
        m_vis = visible_mass_profile(r)
        v = v_newtonian(r, m_vis)
        # At large r, v should decrease (Keplerian)
        assert v[-1].item() < v[-2].item()

    def test_dm_flat_at_large_r(self):
        r = torch.linspace(10.0, 30.0, 500)
        m_vis = visible_mass_profile(r)
        v = v_dark_matter(r, m_vis, v_flat=150.0)
        outer = v[-100:].cpu().numpy()
        assert np.std(outer) / np.mean(outer) < 0.05
        assert abs(np.mean(outer) - 150.0) / 150.0 < 0.10

    def test_vtc_flat_at_large_r(self):
        r = torch.linspace(10.0, 30.0, 500)
        m_vis = visible_mass_profile(r)
        v = v_vtc(r, m_vis, v0=150.0)
        outer = v[-100:].cpu().numpy()
        assert np.std(outer) / np.mean(outer) < 0.05
        assert abs(np.mean(outer) - 150.0) / 150.0 < 0.10

    def test_vtc_matches_dm(self):
        r = torch.linspace(0.5, 30.0, 1000)
        m_vis = visible_mass_profile(r)
        v_dm_curve = v_dark_matter(r, m_vis, v_flat=150.0)
        v_vtc_curve = v_vtc(r, m_vis, v0=150.0)
        max_diff = torch.abs(v_vtc_curve - v_dm_curve).max().item()
        assert max_diff / 150.0 < 0.05


class TestLensing:
    """Tests for gravitational lensing models."""

    def test_dm_deflection_nonzero(self):
        b = torch.linspace(1.0, 50.0, 100)
        alpha = lensing_dm_isothermal(b, v_flat=150.0)
        assert torch.all(alpha > 0.0)

    def test_vtc_deflection_nonzero(self):
        b = torch.linspace(1.0, 50.0, 100)
        alpha = lensing_vtc(b, v0=150.0)
        assert torch.all(alpha > 0.0)

    def test_dm_vtc_agree(self):
        b = torch.linspace(1.0, 50.0, 100)
        a_dm = lensing_dm_isothermal(b, v_flat=150.0)
        a_vtc = lensing_vtc(b, v0=150.0)
        ratio = a_vtc.mean().item() / max(a_dm.mean().item(), 1e-10)
        assert 0.8 < ratio < 1.2

    def test_deflection_constant_for_isothermal(self):
        b = torch.linspace(1.0, 100.0, 500)
        alpha = lensing_dm_isothermal(b, v_flat=150.0)
        std = alpha.std().item()
        mean = alpha.mean().item()
        assert std / mean < 0.01  # essentially constant


class TestCosmicExpansion:
    """Tests for cosmic expansion models."""

    def test_lcdm_h0_match(self):
        a = torch.tensor([1.0])
        h = hubble_lcdm(a, omega_m=0.31, omega_l=0.69, h0=67.4)
        assert h.item() == pytest.approx(67.4, rel=0.05)

    def test_vtc_h0_match(self):
        a = torch.tensor([1.0])
        h = hubble_vtc(a, omega_m=0.31, beta=0.48, h0=67.4)
        assert h.item() == pytest.approx(67.4, rel=0.10)

    def test_lcdm_accelerates_vs_matter(self):
        a = torch.linspace(0.1, 1.0, 100)
        h_lcdm = hubble_lcdm(a).cpu().numpy()
        h_matter = 67.4 * np.sqrt(0.31 / (a.cpu().numpy() ** 3))
        # At late times (a=1), LCDM H > matter-only H due to Lambda
        assert h_lcdm[-1] > h_matter[-1]

    def test_vtc_accelerates_vs_matter(self):
        a = torch.linspace(0.1, 1.0, 100)
        h_vtc = hubble_vtc(a, beta=0.48).cpu().numpy()
        h_matter = 67.4 * np.sqrt(0.31 / (a.cpu().numpy() ** 3))
        assert h_vtc[-1] > h_matter[-1]

    def test_vtc_tracks_lcdm(self):
        a = torch.linspace(0.1, 1.0, 500)
        h_lcdm = hubble_lcdm(a).cpu().numpy()
        h_vtc = hubble_vtc(a, beta=0.48).cpu().numpy()
        rel_err = np.abs(h_vtc - h_lcdm) / np.maximum(h_lcdm, 1e-10)
        assert rel_err.mean() < 0.15


class TestGPU:
    """Verify GPU tensors actually run on CUDA."""

    def test_device_is_cuda(self):
        device = get_device()
        assert device.type == "cuda", "CUDA not available"

    def test_tensor_on_gpu(self):
        device = get_device()
        x = torch.randn(100, 100, device=device)
        y = x @ x.T
        assert y.device.type == "cuda"
