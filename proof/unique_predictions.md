# Unique Predictions of Variable Temporal Curvature (VTC)
## Two Observable Tests That ΛCDM Cannot Reproduce

**Status:** Formal derivations with GPU verification  
**Date:** 2026-07-02

---

# Prediction 1: The Morphology Test

## The Core Idea

In ΛCDM, dark matter halos are approximately **spherically symmetric**. A galaxy's visible disk sits inside a spherical DM halo. If two galaxies have the same total baryonic mass but different morphologies (one bulge-dominated, one disk-dominated), ΛCDM predicts they sit inside **identical DM halos** (modulo halo assembly bias).

In VTC, the scalar field is **sourced by visible matter**:

$$\nabla^2\phi = \kappa\,\rho_{\text{vis}}(R,z)$$

Because $\rho_{\text{vis}}$ is disk-like (not spherical), the resulting lapse function $N(R,z)$ inherits the **morphology of the baryons**. Two galaxies with the same mass but different morphologies will have **different effective DM profiles** in VTC.

This is a **genuine, falsifiable difference** between the two frameworks.

---

## Mathematical Derivation

### The Viscible Matter Density

For an exponential disk with sech² vertical profile:

$$\rho_{\text{vis}}(R,z) = \rho_0\exp\left(-\frac{R}{R_d}\right)\text{sech}^2\left(\frac{z}{z_0}\right)$$

where $R_d$ is the disk scale length and $z_0$ is the scale height.

### The Scalar Field Equation

In the Newtonian limit:

$$\nabla^2\phi = \frac{1}{R}\frac{\partial}{\partial R}\left(R\frac{\partial\phi}{\partial R}\right) + \frac{\partial^2\phi}{\partial z^2} = \kappa\rho_{\text{vis}}(R,z)$$

### The Green's Function Solution

For an infinite thin disk, the solution at $z = 0$ is:

$$\phi(R,0) = -\frac{\kappa\rho_0 R_d^2}{2\pi}\int_0^{\infty}dk\,\frac{J_0(kR)}{(1+k^2R_d^2)^{3/2}}$$

This integral evaluates to a function that depends on $R/R_d$ — the **disk scale length sets the curvature scale**.

### The Key Difference

In ΛCDM, the DM density depends on spherical radius $r = \sqrt{R^2+z^2}$:

$$\rho_{\text{DM}}^{(\Lambda\text{CDM})}(r) = \frac{v_0^2}{4\pi G r^2}$$

In VTC, the effective density depends on the **baryonic geometry**:

$$\rho_{\text{VTC}}^{(\text{eff})}(R,z) = \frac{c^2}{4\pi G}\nabla^2\ln N(R,z)$$

Because $N$ is sourced by a disk, $\rho_{\text{VTC}}^{(\text{eff})}$ is **disk-like**, not spherical. The iso-density contours are **flattened** along the disk plane.

### Observable Consequence: Rotation Curve Shape

For a face-on galaxy, the observed rotation curve samples $v(R, z \approx 0)$. For an edge-on galaxy, line-of-sight integration averages over $z$. 

In ΛCDM, both see the same spherical halo → **same rotation curve shape** (after deprojection).

In VTC:
- Face-on: samples the strong $z = 0$ field where the disk source is concentrated
- Edge-on: line-of-sight averages over weaker field at large $|z|$

→ **Different effective rotation curves** for the same baryonic mass.

---

# Prediction 2: The Vertical Redshift Gradient

## The Core Idea

In ΛCDM, gravitational redshift depends on the **spherical potential** $\Phi(r)$. Two stars at the same cylindrical radius $R$ but different heights $z_1$ and $z_2$ above the disk are at different spherical radii $r_1 = \sqrt{R^2+z_1^2}$ and $r_2 = \sqrt{R^2+z_2^2}$. Their redshift difference comes from $r$-dependence.

In VTC, the lapse $N(R,z)$ varies with **both** $R$ and $z$ because the scalar field follows the disk. Even at fixed $R$, $N(R,z)$ decreases with $|z|$ (less source material at high $z$). Two stars at the same $(R, z_1)$ and $(R, z_2)$ experience **different clock rates** due to the $z$-gradient of the lapse.

This creates a **vertical redshift gradient** — a systematic offset in stellar line-of-sight velocities that depends on height above the disk — that ΛCDM does not predict.

---

## Mathematical Derivation

### Gravitational Redshift in VTC

For a static metric $ds^2 = -N^2(r)\,dt^2 + g_{ij}\,dx^i dx^j$, the gravitational redshift between two points is:

$$\frac{\Delta\lambda}{\lambda} = \frac{N_2}{N_1} - 1 \approx \frac{N_2 - N_1}{N_1}$$

For two stars at $(R, z_1)$ and $(R, z_2)$:

$$\frac{\Delta\lambda}{\lambda}\bigg|_{\text{VTC}} \approx \frac{1}{M_{\text{Pl}}}\frac{\partial\phi}{\partial z}\bigg|_{z=0}\cdot(z_2 - z_1)$$

### The Vertical Gradient

From the scalar field equation, near the midplane ($z \approx 0$):

$$\frac{\partial^2\phi}{\partial z^2}\bigg|_{z=0} = \kappa\rho_0\exp(-R/R_d) - \frac{1}{R}\frac{\partial}{\partial R}\left(R\frac{\partial\phi}{\partial R}\right)$$

For a thin disk where vertical gradients dominate:

$$\frac{\partial\phi}{\partial z}\bigg|_{z=0^+} \approx \frac{\kappa\rho_0 z_0}{2}\exp(-R/R_d)$$

This gives a vertical lapse gradient that depends on the **local disk density**.

### Comparison to ΛCDM

In ΛCDM with a spherical isothermal halo, the redshift difference depends on spherical radius:

$$\frac{\Delta\lambda}{\lambda}\bigg|_{\Lambda\text{CDM}} = \frac{v_0^2}{c^2}\ln\frac{r_2}{r_1}$$

For $z_1 = 0$, $z_2 = z$, $R \gg z$:

$$\frac{\Delta\lambda}{\lambda}\bigg|_{\Lambda\text{CDM}} \approx \frac{v_0^2}{c^2}\frac{z^2}{2R^2}$$

This is **quadratic in $z$** and **suppressed by $R^{-2}$**.

In VTC, the redshift gradient is **linear in $z$** and **exponentially suppressed in $R/R_d$**:

$$\frac{\Delta\lambda}{\lambda}\bigg|_{\text{VTC}} \approx \frac{\kappa\rho_0 z_0}{2M_{\text{Pl}}}\exp(-R/R_d)\cdot z$$

### Observable Signature

Measure the line-of-sight velocity of stars as a function of height $z$ above the disk at fixed projected radius $R$. Fit:

$$v_{\text{los}}(z) = v_{\text{rot}} + v_z\cdot z + v_{z^2}\cdot z^2$$

- **ΛCDM predicts:** $v_z \approx 0$ (no linear vertical redshift gradient from DM); $v_{z^2} \neq 0$ from spherical geometry
- **VTC predicts:** $v_z \neq 0$ (linear gradient from disk-sourced lapse); $v_{z^2}$ may also be non-zero

The **linear coefficient $v_z$** is the smoking gun.

---

# Summary Table

| Test | ΛCDM Prediction | VTC Prediction | Observable |
|---|---|---|---|
| **Morphology** | Same DM halo for same mass, any morphology | DM profile follows baryonic morphology | Compare rotation curves of edge-on vs face-on galaxies with matched baryonic mass |
| **Vertical Redshift** | Quadratic in $z$, suppressed at large $R$ | Linear in $z$, exponentially peaked at small $R$ | Measure stellar $v_{\text{los}}$ vs $z$ at fixed $R$; fit for linear coefficient |

---

# Why These Are Genuinely Unique

1. **Not reproducible by MOND:** MOND modifies the force law but still assumes spherical symmetry for isolated systems. It does not predict morphology-dependent halos.

2. **Not reproducible by scalar-tensor theories:** Standard scalar-tensor theories (Brans-Dicke, Horndeski) typically assume spherical symmetry for galactic solutions. A disk-sourced scalar field requires specific boundary conditions that are not generic.

3. **Not reproducible by emergent gravity:** Verlinde's emergent gravity derives from spherical entropy surfaces. Disk geometry breaks the spherical symmetry assumption.

4. **Directly testable with existing data:** Edge-on disk galaxies (e.g., NGC 891, NGC 4565) and face-on galaxies (e.g., NGC 3198) have been extensively mapped. The vertical redshift gradient can be measured with modern IFU spectroscopy (e.g., MUSE, KCWI).

---

# References

1. Binney, J. & Tremaine, S. (2008). *Galactic Dynamics* (2nd ed.). Princeton University Press.
2. Freeman, K. C. (1970). "On the Disks of Spiral and S0 Galaxies." *ApJ,* 160, 811.
3. Kuijken, K. & Gilmore, G. (1989). "The Mass Distribution in the Galactic Disc." *MNRAS,* 239, 571.
4. Bland-Hawthorn, J. & Gerhard, O. (2016). "The Galaxy in Context." *ARAA,* 54, 529.
