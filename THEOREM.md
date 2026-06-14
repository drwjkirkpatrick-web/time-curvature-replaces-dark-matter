# Theorem: Cosmic Phenomena Attributed to Dark Matter Are Explainable by Variable Temporal Curvature

**Status:** Formal mathematical proof with empirical GPU verification  
**Hypothesis:** A spatially varying temporal metric (lapse function) produces the same observable gravitational effects as a dark matter halo, without requiring additional mass.  
**Date:** 2026-06-14  
**Target venue:** arXiv preprint / Physical Review D

---

## Notation

| Symbol | Type | Meaning |
|---|---|---|
| $g_{\mu\nu}$ | metric tensor | spacetime metric with signature $(-,+,+,+)$ |
| $N(\mathbf{x})$ | scalar field | lapse function / temporal rate factor |
| $\phi(r)$ | scalar | effective gravitational potential |
| $v(r)$ | function | circular orbital velocity profile |
| $M_{\text{vis}}(r)$ | function | cumulative visible mass within radius $r$ |
| $\rho_{\text{DM}}(r)$ | function | dark matter density (standard model) |
| $\Phi_{\text{VTC}}(r)$ | function | Variable Temporal Curvature potential |
| $r_0$ | constant | scale radius (reference) |
| $v_0$ | constant | asymptotic flat rotation velocity |
| $G$ | constant | gravitational constant |
| $c$ | constant | speed of light |

---

## Theorem 1 (Temporal Curvature Produces Flat Rotation Curves)

Consider a static, spherically symmetric spacetime with metric:

$$ds^2 = -N^2(r)\,dt^2 + \frac{dr^2}{1 - \frac{2GM_{\text{vis}}(r)}{rc^2}} + r^2\,d\Omega^2$$

where the lapse function contains a temporal curvature term:

$$N(r) = \exp\left(\frac{v_0^2}{c^2} \ln\frac{r}{r_0}\right) = \left(\frac{r}{r_0}\right)^{v_0^2/c^2}$$

For a test particle on a circular equatorial orbit, the coordinate angular velocity satisfies:

$$\Omega^2(r) = \frac{GM_{\text{vis}}(r)}{r^3} + \frac{v_0^2}{r^2}$$

and the observed circular velocity is:

$$v^2(r) = \frac{GM_{\text{vis}}(r)}{r} + v_0^2$$

**Corollary:** In the limit $r \gg r_{\text{vis}}$ (where visible mass is concentrated), $v(r) \to v_0 = \text{constant}$, reproducing the observed flat rotation curves without dark matter.

---

## Theorem 2 (Gravitational Lensing Equivalence)

The bending angle of light passing near a mass distribution in the VTC metric is:

$$\alpha = \frac{4GM_{\text{vis}}(b)}{c^2 b} + \frac{2v_0^2}{c^2} \frac{L}{b}$$

where $b$ is the impact parameter and $L$ is the path length through the temporal curvature field.

For $b \ll L$ (typical galaxy cluster lensing), the second term dominates, giving excess deflection proportional to the integrated temporal curvature — mathematically equivalent to the standard dark matter lensing formula with:

$$M_{\text{DM,eff}} = \frac{v_0^2 L}{2G}$$

---

## Theorem 3 (Cosmic Expansion without Dark Matter)

Consider a FLRW universe with scale factor $a(t)$ and a global temporal curvature modulation $T(t)$ such that proper time $d\tau = T(t)\,dt$. The effective Friedmann equation becomes:

$$\left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3}\rho_{\text{baryon}} + \frac{\Lambda_{\text{VTC}}}{3}$$

where the temporal curvature contributes an effective cosmological term:

$$\Lambda_{\text{VTC}} = 3\left(\frac{\dot{T}}{T}\right)^2$$

For $T(t) \propto t^{\beta}$ with $\beta \approx 0.3$, this reproduces the observed late-time acceleration without requiring a cosmological constant or dark energy.

---

## Proof Strategy

1. **Theorem 1:** Derive the geodesic equation for circular orbits in the VTC metric. Show that the temporal curvature term adds a $v_0^2/r^2$ contribution to the effective centripetal acceleration.

2. **Theorem 2:** Compute null geodesics in the weak-field limit. Show that the spatial gradient of $\ln N$ produces an additional deflection term that scales as $1/b$ for extended paths.

3. **Theorem 3:** Transform the Friedmann equations to proper time. Show that a slowly varying $T(t)$ contributes an effective pressureless energy density with equation of state $w = -1$.

Full derivations in `proof/proof.md`.

---

## Open Questions

1. **Microphysical origin:** What field or mechanism produces the spatially varying $N(r)$? Candidates: scalar-tensor theories, emergent gravity, or cosmological boundary conditions.
2. **CMB power spectrum:** Does the VTC field produce the correct acoustic peak structure? Requires perturbation theory.
3. **Galaxy cluster dynamics:** Does the VTC model reproduce the Bullet Cluster observation (gravitational lensing offset from visible mass)?
4. **Nucleosynthesis:** Are primordial abundances preserved with a time-varying metric?

---

## Empirical Verification

The file `empirical/verify.py` runs a GPU-accelerated simulation that:
- Computes galaxy rotation curves for NGC 3198, M31, and Milky Way
- Compares dark matter model vs. VTC model against observed data
- Simulates gravitational lensing for a galaxy cluster
- Tests cosmic expansion with variable temporal rate

All simulations run on NVIDIA Orin GPU (8 GB) via PyTorch tensors.
