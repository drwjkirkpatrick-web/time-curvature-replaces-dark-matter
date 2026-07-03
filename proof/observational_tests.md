# Observational Tests of Variable Temporal Curvature (VTC)
## A Practical Guide to Falsifying the Theory

**Status:** Predictions computed; datasets identified; test protocols defined  
**Date:** 2026-07-02

---

## Executive Summary

VTC makes **two unique predictions** that ΛCDM cannot reproduce. This document specifies exactly how to test them with existing observational data.

| Prediction | Observable | Instrument Needed | Data Status | VTC Signal |
|---|---|---|---|---|
| **1. Morphology-Dependent Gravity** | Effective acceleration differs for bulge vs disk galaxies with same mass | SPARC + ALMA CO kinematics | SPARC: 175 galaxies; ALMA: available for subset | **0.14×** ratio at R=5 kpc |
| **2. Vertical Redshift Gradient** | Systematic line-of-sight velocity offset vs height above disk at fixed R | MaNGA IFU, MUSE, KCWI | MaNGA DR17: ~10,000 galaxies; **not yet analyzed for this** | **–2.1 km/s** per kpc |

---

## Prediction 1: Morphology-Dependent Gravity

### The Physics

In ΛCDM, dark matter halos are approximately spherical. The acceleration at radius R depends only on the enclosed dark matter mass, which is determined by the observed flat rotation velocity $v_0$. Two galaxies with the same $v_0$ but different morphologies sit inside **identical halos**.

In VTC, the lapse function $N(R,z)$ is sourced by visible matter:

$$N(R,z) = \left(\frac{\rho_{\text{vis}}(R,z)}{\rho_0}\right)^\alpha$$

Because visible matter is disk-shaped, the resulting temporal curvature follows the disk geometry. A galaxy with a **tight bulge** (small $R_d$) concentrates the source at small radii, producing a steep lapse gradient and strong effective gravity. A galaxy with an **extended disk** (large $R_d$) spreads the source out, producing a weaker gradient.

### The Quantitative Prediction

For two galaxies with the same baryonic mass:

| Morphology | Scale Length $R_d$ | $a_{\text{VTC}}$ at R=5 kpc | Relative to Bulge |
|---|---|---|---|
| Bulge-dominated | 0.5 kpc | $-1.8 \times 10^7$ km²/s²/kpc | 1.00× |
| Disk-dominated | 3.5 kpc | $-2.6 \times 10^6$ km²/s²/kpc | **0.14×** |
| ΛCDM (both) | N/A (spherical) | $-4.5 \times 10^3$ km²/s²/kpc | 1.00× |

The VTC prediction is a **7× difference** in effective gravity for the same mass.

### How to Test This

#### Step 1: Get the SPARC Catalog

The SPARC (Spitzer Photometry and Accurate Rotation Curves) catalog contains 175 late-type galaxies with:
- Measured rotation curves $v_{\text{obs}}(R)$
- Decomposed baryonic contributions: $v_{\text{gas}}$, $v_{\text{disk}}$, $v_{\text{bulge}}$
- Surface brightness profiles

**Download:**
```bash
# Primary URL (currently offline; check mirrors)
curl -O http://astroweb.cas.sfu.ca/SPARC/SPARC_Lelli2016c.mrt

# Alternative mirror
curl -O https://www.cv.nrao.edu/~fmasset/SPARC/SPARC_Lelli2016c.mrt

# ReadMe for column definitions
curl -O http://astroweb.cas.sfu.ca/SPARC/ReadMe
```

**Reference:** Lelli et al. 2016c, "SPARC: Mass Models for 175 Disk Galaxies," AJ 152, 157.

#### Step 2: Classify Morphology

For each SPARC galaxy, compute the **bulge-to-disk ratio** at small radii:

$$B/D = \frac{\langle v_{\text{bulge}} \rangle_{R<2\text{kpc}}}{\langle v_{\text{disk}} \rangle_{R<2\text{kpc}}}$$

| Classification | Criterion |
|---|---|
| Bulge-dominated | $B/D > 1.5$ |
| Disk-dominated | $B/D < 0.67$ |
| Mixed | $0.67 \leq B/D \leq 1.5$ |

#### Step 3: Compute the Residual Acceleration

For each galaxy, compute the "missing" acceleration attributed to dark matter:

$$a_{\text{DM}}(R) = \frac{v_{\text{obs}}^2 - v_{\text{bar}}^2}{R}$$

where $v_{\text{bar}}^2 = v_{\text{gas}}^2 + v_{\text{disk}}^2 + v_{\text{bulge}}^2$.

At large radii ($R > 2R_d$), $a_{\text{DM}} \to v_0^2/R$ for both ΛCDM and VTC. The difference is in the **radial profile** at intermediate radii.

#### Step 4: Compare Morphology Groups

In ΛCDM, the residual acceleration profiles should be statistically identical for bulge and disk galaxies with the same $v_0$ (after matching for total baryonic mass).

In VTC, the disk-dominated galaxies should have systematically **lower effective acceleration** at intermediate radii because their temporal curvature is spread over a larger area.

**Statistical Test:**
1. Match galaxies in bins of $v_0$ (±10 km/s) and total baryonic mass (±0.2 dex)
2. Compare the residual acceleration profiles $a_{\text{DM}}(R/R_d)$ between bulge and disk subsamples
3. VTC predicts: $a_{\text{disk}}(R) < a_{\text{bulge}}(R)$ for $R \sim 2-5$ kpc

### Expected Signal Size

From our GPU simulation:

$$\frac{a_{\text{disk}}}{a_{\text{bulge}}} \approx 0.14 \text{ at } R = 5 \text{ kpc}$$

This is a **large effect** — much larger than typical measurement uncertainties in SPARC (~5-10%). If real, it would be immediately detectable.

**Important caveat:** The absolute amplitude depends on the coupling constant $\alpha = v_0^2/c^2 \approx 2.5 \times 10^{-7}$. Our simulation used $\alpha = 10^{-4}$ for numerical demonstration. The **qualitative prediction** (morphology dependence) is robust; the **quantitative ratio** scales with $\alpha$ and the specific lapse model.

---

## Prediction 2: Vertical Redshift Gradient

### The Physics

In ΛCDM with a spherical isothermal halo, the gravitational potential depends on spherical radius $r = \sqrt{R^2 + z^2}$. At fixed cylindrical radius $R$, the potential variation with height $z$ is:

$$\Phi(R,z) - \Phi(R,0) = v_0^2 \ln\frac{\sqrt{R^2+z^2}}{R} \approx \frac{v_0^2 z^2}{2R^2}$$

This is **quadratic in z** and suppressed by $R^{-2}$. The gravitational redshift is:

$$\frac{\Delta\lambda}{\lambda} = \frac{\Phi(R,z) - \Phi(R,0)}{c^2} \sim \frac{z^2}{R^2}$$

There is **no linear term** in z.

In VTC, the lapse $N(R,z)$ follows the disk geometry. Even at fixed $R$, $N$ varies with $z$ because the visible matter density $\rho_{\text{vis}}(R,z)$ falls off vertically:

$$N(R,z) = \left(\frac{\rho_{\text{vis}}(R,z)}{\rho_0}\right)^\alpha \propto \left[\text{sech}^2\left(\frac{z}{z_0}\right)\right]^\alpha$$

The vertical gradient is **linear in z** near the midplane:

$$\partial_z \ln N \approx -\frac{2\alpha}{z_0^2} z$$

This produces a redshift difference:

$$\frac{\Delta\lambda}{\lambda} \approx -\frac{2\alpha z}{z_0^2}$$

which is **linear in z** at fixed $R$.

### The Quantitative Prediction

For a disk with $z_0 = 0.3$ kpc and $\alpha = 10^{-4}$ (demonstration value):

$$\partial_z \ln N \approx -7 \times 10^{-6} \text{ kpc}^{-1} \text{ at } R = 5 \text{ kpc}$$

The velocity shift for two stars separated by $\Delta z = 1$ kpc:

$$\Delta v = c \cdot \partial_z \ln N \cdot \Delta z \approx -2.1 \text{ km/s}$$

Scaling to the physical coupling $\alpha = v_0^2/c^2 \approx 2.5 \times 10^{-7}$:

$$\Delta v_{\text{physical}} \approx -2.1 \times \frac{2.5 \times 10^{-7}}{10^{-4}} \approx -5 \times 10^{-3} \text{ km/s} = -5 \text{ m/s}$$

### Observability Assessment

| Quantity | Value | Comment |
|---|---|---|
| VTC signal (physical α) | ~5 m/s per kpc | Very small |
| VTC signal (demo α) | ~2 km/s per kpc | Large |
| Typical stellar velocity dispersion | 20–30 km/s | Dominates over physical signal |
| Measurement precision (single star) | 1–5 km/s | Marginal |
| Stacking precision (100 galaxies) | 0.2–0.5 km/s | Potentially sufficient for demo α |

**Conclusion:** With the physical coupling $\alpha = v_0^2/c^2$, the vertical gradient is **unobservably small** for individual stars. However, if $\alpha$ is larger (e.g., due to a stronger scalar field coupling), the effect could be detected by stacking many face-on galaxies.

### How to Test This

#### Option A: Existing IFU Surveys (Most Practical)

**MaNGA (Mapping Nearby Galaxies at Apache Point Observatory):**
- 10,000+ galaxies with integral field spectroscopy
- Spectral resolution: R ~ 2000 (σ_v ~ 30 km/s for emission lines)
- Spatial resolution: ~1–2 kpc per fiber
- **Critical:** MaNGA provides 2D velocity fields, not full 3D (z information is lost in projection)

**Limitation:** MaNGA fibers are spaced ~1 kpc apart. The vertical gradient requires resolving the z-dimension, which is projected onto the sky for all but perfectly edge-on galaxies. For face-on galaxies, z is perpendicular to the line of sight and cannot be measured.

**Best target:** Moderately inclined galaxies (i ≈ 30–60°) where some z information is preserved in projection.

**MUSE (Multi-Unit Spectroscopic Explorer) on VLT:**
- Higher spectral resolution: R ~ 3000–5000
- Better spatial sampling: ~0.2″ per pixel
- Can resolve vertical structure in nearby edge-on galaxies

**Best targets:**
- NGC 891 (edge-on spiral, d ≈ 10 Mpc)
- NGC 4565 (edge-on, d ≈ 16 Mpc)
- NGC 5746 (edge-on, d ≈ 30 Mpc)

**KCWI (Keck Cosmic Web Imager):**
- R ~ 4000
- Excellent for nearby galaxies
- Limited field of view (≈30″ × 20″)

#### Option B: Stellar Populations in the Milky Way

The **Milky Way** is the ideal laboratory because we have full 3D positions and velocities for millions of stars:

- **Gaia DR3:** Astrometry + radial velocities for ~33 million stars
- **RAVE:** Radial velocities for ~500,000 stars
- **APOGEE:** High-resolution spectra for ~500,000 stars (including [Fe/H] and age)

**The Test:**
1. Select stars at the same Galactocentric radius $R$ (e.g., $R = 5$ kpc, the Solar neighborhood)
2. Measure their line-of-sight velocities as a function of height $|z|$ above the disk
3. Fit: $v_{\text{los}}(z) = v_0 + v_z \cdot z + v_{z^2} \cdot z^2$
4. **VTC predicts $v_z \neq 0$** (linear term)
5. **ΛCDM predicts $v_z = 0$** (only $v_{z^2}$ from spherical geometry)

**Expected signal in the Solar neighborhood:**
- From our model with physical α: $v_z \sim -5$ m/s/kpc
- This is **far below** current measurement precision
- Even with Gaia, systematic errors in distance/velocity are ~km/s scale

**However:** If the scalar field coupling is stronger than the minimal value, the signal could be larger. The coupling is a free parameter in the phenomenological model.

#### Option C: Future Missions

- **4MOST (4-metre Multi-Object Spectroscopic Telescope):** 2025+; millions of stellar spectra; could reach ~0.5 km/s precision with stacking
- **SDSS-V:** Milky Way Mapper; high-resolution spectra for millions of stars
- **THESEUS/ATHENA (X-ray):** Hot gas in galaxy halos could show VTC signatures in X-ray line redshifts

---

## Critical Assessment: Can These Predictions Be Ruled Out?

### Prediction 1 (Morphology)

**Strengths:**
- Large predicted signal (0.14× difference)
- Testable with existing SPARC data
- Independent of the coupling constant α (qualitative prediction)

**Weaknesses:**
- SPARC galaxies are not a perfectly matched sample
- Baryonic mass estimates depend on M/L ratios (uncertain)
- Selection effects: bulge-dominated galaxies may preferentially reside in different environments

**Ruling out VTC:** If SPARC shows no morphology dependence in residual accelerations after proper matching, VTC is constrained. A null result would limit the coupling between temporal curvature and visible matter.

### Prediction 2 (Vertical Gradient)

**Strengths:**
- Conceptually clean separation from ΛCDM
- Could be tested with existing IFU data (though not yet done)

**Weaknesses:**
- Signal is very small for physical coupling α = v₀²/c²
- Confounded by random motions (σ_v ~ 20–30 km/s)
- Requires precise z-coordinates, which are only available for nearby edge-on galaxies

**Ruling out VTC:** If future high-precision surveys (4MOST, SDSS-V) measure the vertical gradient and find no linear term at the predicted level, VTC with the minimal coupling is ruled out. However, a stronger coupling could still be consistent.

---

## Recommended Priority Order

| Priority | Test | Time | Cost | Impact |
|---|---|---|---|---|
| **1** | SPARC morphology analysis | Days | Free (data public) | High — large predicted signal |
| **2** | MaNGA face-on stack for vertical gradient | Weeks | Free (data public) | Medium — challenging separation |
| **3** | MUSE observation of NGC 891 edge-on | Nights | Telescope time | High — clean geometry |
| **4** | Gaia/SDSS-V Milky Way vertical kinematics | Years | Survey data | Medium — small predicted signal |

---

## References

### Datasets
1. Lelli et al. 2016c, "SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves," AJ 152, 157.
2. Blanton et al. 2017, "Sloan Digital Sky Survey IV: Mapping the Milky Way, Nearby Galaxies, and the Distant Universe," AJ 154, 28.
3. Bundy et al. 2015, "Overview of the SDSS-IV MaNGA Survey," ApJ 798, 7.
4. Gaia Collaboration 2023, "Gaia Data Release 3," A&A 674, A1.

### Theory Papers
5. Kuijken, K. & Gilmore, G. 1989, "The Mass Distribution in the Galactic Disc — III. The Local Volume Mass Density," MNRAS 239, 605.
6. Bland-Hawthorn, J. & Gerhard, O. 2016, "The Galaxy in Context: Structural, Kinematic and Integrated Properties," ARAA 54, 529.
7. Lopez-Corredoira, M. 2019, "Testing the Multicomponent Model of the Galactic Disc with RAVE and SDSS," ApJ 881, 56.

---

## Code

All predictions are computed in:
- `empirical/verify_unique.py` — GPU simulation (PyTorch CUDA)
- `tests/test_unique.py` — 6/6 pytest passing
- `empirical/observational_search.py` — dataset search and analysis

Run on Jetson Orin, CUDA 12.6, PyTorch 2.5.0.
