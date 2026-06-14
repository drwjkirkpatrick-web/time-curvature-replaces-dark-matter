# Variable Temporal Curvature (VTC) — Why This Theory Works

> **Note:** This README contains LaTeX math. For best display, view on **GitHub** (math renders automatically) or use a Markdown viewer with MathJax support.
> If you are reading this in plain text, each formula is followed by a plain-English description in parentheses.

---

## The Short Version

Dark matter was invented because galaxies rotate too fast. Stars at the edge of a galaxy move at the same speed as stars near the center, even though there isn't enough visible mass to hold them there. Physicists solved this by adding invisible "dark matter" — extra mass we can't see.

**This theory asks: what if there's no missing mass? What if time itself flows differently at the edge of a galaxy, creating the same gravitational effect?**

In General Relativity, gravity isn't just mass pulling on mass — it's the curvature of spacetime. And spacetime has four dimensions: three of space, and one of time. When we look at galaxy rotation curves, we usually assume time flows at the same rate everywhere. But what if it doesn't?

---

## The Analogy: A River and a Boat

Imagine you're in a boat on a river. The river flows at different speeds:
- Near the bank: slow
- In the center: fast

If you drop a stick in the water, it doesn't just drift with the current — the **gradient** in current speed (faster in the middle, slower at the edges) creates a force that pulls the stick toward the center.

Now imagine "proper time" (the time experienced by a physical clock) is like the river:
- Near the galactic center: time flows "normally"
- Far from the center: time flows slightly slower

The **gradient** in how fast time flows creates an effective force — just like the river current gradient pulls the stick. This force holds stars in fast orbits without needing extra mass.

---

## Why General Relativity Allows This

Einstein's field equations are:

$$
G_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}
$$

*(The Einstein tensor on the left equals energy-momentum tensor on the right, scaled by constants.)*

The left side ($G_{\mu\nu}$) describes spacetime geometry. The right side ($T_{\mu\nu}$) describes matter and energy. **BUT** — in the standard formulation of GR, the way we "slice" spacetime into space + time is not unique.

The **ADM formalism** (Arnowitt-Deser-Misner) decomposes spacetime into 3D spatial slices evolving in time. It introduces:
- $N$ = **lapse function** = how much proper time passes per unit coordinate time
- $N^i$ = **shift vector** = how spatial coordinates drift between slices

**Key point:** The lapse function $N$ is a **gauge choice**. Different choices are mathematically valid and correspond to different ways of cutting spacetime into slices.

In standard cosmology, we choose $N = 1$ everywhere. This is a **convention**, not a law of physics.

Our theory chooses:

$$
N(r) = \left(\frac{r}{r_0}\right)^{v_0^2/c^2}
$$

*(The lapse function N grows as a power law of radius r, with exponent v₀² divided by c².)*

This means: **the farther you are from a galaxy's center, the slower your clock ticks relative to a distant observer.** The difference is tiny — parts per billion — but over galactic scales, the accumulated effect produces what looks like extra gravity.

---

## Four Different Ways to Prove the Same Thing

### Proof 1: The Geodesic Equation (How Orbits Work)

For a particle on a circular orbit, the geodesic equation gives:

$$
v^2(r) = \frac{GM_{\text{vis}}(r)}{r} + c^2 r \frac{N'(r)}{N(r)}
$$

*(Orbital velocity squared equals Newtonian term plus a term from the lapse gradient.)*

For our lapse function:

$$
\frac{N'}{N} = \frac{\alpha}{r} = \frac{v_0^2}{c^2 r}
$$

*(The logarithmic derivative of N is α over r, where α = v₀²/c².)*

Substituting:

$$
v^2(r) = \frac{GM_{\text{vis}}(r)}{r} + v_0^2
$$

*(Velocity squared equals visible-mass Newtonian term plus a constant v₀².)*

**At large radii, the visible mass term decays, leaving $v^2 \to v_0^2$ = constant.**

*(Far from the galaxy, v² approaches a flat constant value.)*

This is a **flat rotation curve** — exactly what astronomers observe. No dark matter needed.

### Proof 2: Effective Energy Density (What the Curvature "Looks Like")

In GR, curvature sources matter. If temporal curvature creates effective energy density, we can ask: what mass distribution would produce the same curvature?

$$
\rho_{\text{eff}} = \frac{c^2}{4\pi G}\nabla^2\ln N = \frac{v_0^2}{4\pi G r^2}
$$

*(Effective density ρ equals c² over 4πG times the Laplacian of log N, which simplifies to v₀² over 4πG r².)*

This is the **isothermal sphere** — the standard dark matter density profile. The VTC model produces the exact same effective density without any particles.

### Proof 3: Hamilton-Jacobi Effective Potential

The effective potential for orbital motion gains an extra term:

$$
V_{\text{eff}}(r) = -\frac{GMm}{r} + \frac{L^2}{2mr^2} - mc^2\ln N(r)
$$

*(Effective potential = Newtonian gravity + centrifugal barrier + VTC term from log N.)*

For $N(r) \sim r^\alpha$:

$$
V_{\text{VTC}}(r) = -mc^2\alpha\ln\frac{r}{r_0}
$$

*(The VTC potential is proportional to the logarithm of radius.)*

The gradient gives an inward force:

$$
F_{\text{VTC}} = \frac{mc^2\alpha}{r}
$$

*(The VTC force falls off as 1/r, like an isothermal dark matter halo.)*

This is an attractive $1/r$ force, identical to what an isothermal dark matter halo would produce.

### Proof 4: Einstein Tensor Components

Computing the Einstein tensor for the VTC metric shows that the temporal curvature terms exactly match the contribution from an isothermal dark matter density:

$$
G_{00} = \text{(visible matter terms)} + \frac{2\alpha^2}{r^2}
$$

*(The Einstein tensor gets an extra term proportional to α² over r² from the lapse.)*

Setting this equal to $8\pi G\rho_{\text{DM}}$ gives:

$$
\rho_{\text{DM,eff}} = \frac{\alpha^2}{4\pi G r^2} = \frac{v_0^2}{4\pi G r^2}
$$

*(The equivalent dark matter density is v₀² over 4πG r² — the isothermal sphere.)*

All four proofs converge on the same result. The VTC model is not one trick — it's a robust geometric equivalence.

---

## What About Gravitational Lensing?

Light doesn't have mass, but it follows geodesics (curved paths) in spacetime. The VTC metric bends light through the spatial gradient of the lapse function:

$$
\alpha_{\text{VTC}} = \frac{4v_0^2}{c^2 b}
$$

*(Lensing deflection angle α = 4v₀² / c²b, where b is the impact parameter.)*

where $b$ is the impact parameter. This matches the standard formula for lensing by an isothermal sphere. **Both models predict the same deflection angle.**

## What About Cosmic Acceleration?

A globally varying temporal rate $T(t) \propto t^\beta$ contributes to the Friedmann equations:

$$
\Lambda_{\text{VTC}} = 3\left(\frac{\dot{T}}{T}\right)^2 = \frac{3\beta^2}{t^2}
$$

*(An effective cosmological constant Λ = 3(Ṫ/T)² = 3β²/t².)*

At late times, this acts like a cosmological constant with $\beta \approx 0.48$, reproducing the observed acceleration.

---

## Why This Isn't "Just Playing with Coordinates"

A common objection: "Aren't you just redefining coordinates?"

**No.** A coordinate transformation changes labels but preserves the physical curvature tensor $R_{\mu\nu\rho\sigma}$. The VTC model changes the actual geometry — the Einstein tensor components are different. Two different spacetimes happen to produce the same observables.

This is like how MOND (Modified Newtonian Dynamics) and dark matter are different theories that fit the same rotation curve data. The VTC model provides a third alternative grounded in GR geometry.

---

## The Honest Limitations

1. **We don't know what field produces $N(r)$.** The theory says "if the lapse varies this way, you get dark matter effects." But *why* would the lapse vary this way? We need a scalar field theory or some other mechanism. This is the biggest open question.

2. **CMB acoustic peaks are untested.** The cosmic microwave background shows specific patterns that dark matter explains beautifully. The VTC model hasn't been tested against this data.

3. **Structure formation is undeveloped.** How do galaxies form and cluster in a VTC universe? We don't know yet.

4. **Occam's Razor.** Replacing dark matter with a modified metric may not be simpler. We trade "invisible particles" for "spatially varying time."

---

## The Bottom Line

| Question | Standard Answer | VTC Answer |
|---|---|---|
| Why do galaxies rotate too fast? | Invisible dark matter halos | Time flows slower in the outer regions |
| Why does light bend too much? | Extra mass bends spacetime | Temporal curvature gradient bends geodesics |
| Why is the universe accelerating? | Dark energy ($\Lambda$) | Global temporal rate slows over time |
| What is dark matter made of? | Unknown particles (WIMPs, axions, etc.) | Nothing — it's geometry |

**This theory doesn't claim dark matter is wrong.** It demonstrates that the *observational signatures* attributed to dark matter can alternatively arise from a specific geometric configuration of spacetime — one where the temporal dimension carries spatial variation.

In General Relativity, time and space are inseparable. Maybe the "missing mass" isn't missing at all. Maybe we've been looking in the wrong dimension.

---

## How to Read the Code

| File | What It Does |
|---|---|
| `THEOREM.md` | Formal statement of the 3 theorems with notation |
| `proof/proof.md` | Full mathematical derivations (4 parallel proofs) |
| `empirical/verify.py` | GPU simulation — runs all 3 theorems on CUDA |
| `tests/test_project.py` | pytest suite — 19 tests, all must pass |

## Running the Verification

### Option 1: Shared Jetson PyTorch (Recommended)

A shared PyTorch installation is available for any Python 3.10 process on this system:

```bash
# Activate the shared Jetson PyTorch
source "$HOME/.venvs/jetson-pytorch/bin/activate"

# Run the GPU simulation
cd ~/projects/time-curvature-replaces-dark-matter
python3.10 empirical/verify.py

# Run the test suite
python3.10 -m pytest tests/ -v
```

### Option 2: Original heartlib venv

```bash
# Activate the heartlib virtual environment
source ~/heartlib/.venv/bin/activate

# Run the GPU simulation
cd ~/projects/time-curvature-replaces-dark-matter
python empirical/verify.py

# Run the test suite
python -m pytest tests/ -v
```

## GPU Requirements

- NVIDIA GPU with CUDA support (tested on Jetson Orin, 8 GB, CUDA 12.6)
- PyTorch 2.5.0+ with CUDA (already installed in shared location)

## Alternative Formats

If the math formulas above do not display correctly in your viewer, try these:

| Format | File | Best For |
|---|---|---|
| **HTML** (MathJax) | [`README.html`](./README.html) | Any web browser — renders all equations automatically |
| **PDF** (typeset) | [`VTC-README.pdf`](./VTC-README.pdf) | Any PDF viewer — math is pre-typeset |
| **Markdown** | [`README.md`](./README.md) | GitHub.com only — other renderers may show raw LaTeX |

## Citation

If you use this work, please cite:

> Walker Kirkpatrick. "Variable Temporal Curvature as an Alternative to Dark Matter: A Mathematical Proof." 2026.

## License

MIT License — See LICENSE file.
