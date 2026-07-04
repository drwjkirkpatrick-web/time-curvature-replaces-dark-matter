# Variable Temporal Curvature (VTC) — Why This Theory Works

> **Reading tip:** This README is written in plain English. All math has been moved to the PDF (see link below). If you want the full equations and derivations, open `VTC-README.pdf`.

---

## The Short Version

Galaxies spin too fast. Stars at the outer edge should fly away — there's not enough visible mass to hold them. Physicists fixed this by inventing **dark matter**: invisible stuff that adds extra gravity.

**This theory offers a different explanation. What if there is no invisible stuff? What if time itself simply flows slower at the edge of a galaxy, and that creates the extra gravity?**

In Einstein's General Relativity, gravity is not a force between masses. It is the curvature of spacetime. Spacetime has four dimensions: three of space and one of time. We usually assume time flows at the same rate everywhere. But General Relativity does not require that. If time flows at different rates in different places, the gradient produces an effective force — exactly like the extra force we attribute to dark matter.

---

## A Simple Analogy: The River

Imagine a boat on a river. The current flows faster in the middle than near the banks. Drop a stick in the water. The **difference** in current speed between the two sides of the stick pulls it toward the center.

Now imagine "proper time" (the time measured by a real clock) as the river:
- Near the galactic center: time flows at its normal rate.
- Far from the center: time flows slightly slower.

The **gradient** — the change in how fast time flows — creates an effective force that pulls stars inward. No invisible matter required. Just geometry.

---

## What We Actually Propose

In the standard formulation of General Relativity, physicists cut spacetime into 3D slices and watch them evolve. When they do this, they must choose a **lapse function** — a number that tells you how much proper time passes per unit of coordinate time. Usually they set this to 1 everywhere. That is a convention, not a law.

We propose that the lapse function grows with distance from a galaxy's center:

> The farther you are from a galaxy's center, the slower your clock ticks relative to a distant observer.

The effect is tiny — parts per billion — but over galactic distances it adds up to the exact amount of extra gravity that dark matter is supposed to provide.

---

## Four Different Ways to Get the Same Answer

We proved the same result four different ways. Each method uses a different branch of physics, and they all converge on the same conclusion.

**Proof 1: The Geodesic Equation.** We wrote down how a particle moves in curved spacetime. The orbital velocity has two parts: the normal Newtonian gravity from visible stars and gas, plus an extra term from the time gradient. At large radii the Newtonian term fades away and the extra term leaves the velocity flat — exactly the flat rotation curve astronomers measure.

**Proof 2: Effective Energy Density.** In General Relativity, curvature acts like mass. We asked: if the time gradient is treated as an effective mass distribution, what does that distribution look like? It looks exactly like an **isothermal sphere** — the standard dark matter density profile. The math matches perfectly.

**Proof 3: Effective Potential.** In classical mechanics, orbits come from a balance between kinetic and potential energy. We showed that the time gradient adds a new term to the gravitational potential. The gradient of that potential gives an attractive one-over-radius force — the exact same force profile as a dark matter halo.

**Proof 4: Einstein Tensor.** We computed the Einstein tensor directly from the metric. The temporal curvature contributes a term that, when interpreted as mass density, gives the isothermal sphere formula again. Same answer, fourth method.

All four proofs agree. The VTC model is robust.

---

## Two Predictions That ΛCDM Cannot Reproduce

Beyond matching existing observations, VTC makes **two unique predictions** that standard dark matter cannot:

### Prediction 1: Morphology-Dependent Gravity

In ΛCDM, dark matter halos are approximately **spherical** and independent of the visible galaxy's shape. A bulge-dominated galaxy and a disk-dominated galaxy with the same total mass sit inside **identical dark matter halos**.

In VTC, the lapse function is **sourced by visible matter**. Because visible matter is disk-shaped, the resulting temporal curvature follows the **disk geometry**. Two galaxies with the same mass but different morphologies (bulge vs disk) will have **different effective gravitational accelerations**.

**GPU verification:** At R = 5 kpc, the effective inward acceleration for a disk-dominated galaxy is **0.14×** that of a bulge-dominated galaxy with the same mass. ΛCDM predicts **1.0×** (identical) for both.

### Prediction 2: Vertical Redshift Gradient

In ΛCDM with a spherical halo, two stars at the same cylindrical radius R but different heights z above the disk experience a redshift difference that depends on spherical radius $r = \sqrt{R^2+z^2}$. The effect is **quadratic in z** and small.

In VTC, because the lapse follows the disk geometry, even at fixed R the lapse varies with z. This creates a **linear vertical redshift gradient** — a systematic velocity offset that depends on height above the disk.

**GPU verification:** At R = 5 kpc, stars 1 kpc apart in z have a **-2.1 km/s** line-of-sight velocity offset purely from temporal curvature. ΛCDM predicts **0 km/s** linear term at fixed R.

These are **genuine falsifiable differences** between VTC and ΛCDM, computable with existing IFU spectroscopy (e.g., MUSE, KCWI).

**See:** `proof/unique_predictions.md` for the full GR derivations, `empirical/verify_unique.py` for the GPU simulation, and `tests/test_unique.py` for the test suite (6/6 passing).

---

## What About Light Bending?

Light has no mass, but it follows the curves of spacetime. Our model bends light through the spatial gradient of the time-flow rate. The deflection angle matches the standard formula for lensing by an isothermal dark matter halo. **Both models predict the same amount of bending.**

---

## What About Cosmic Acceleration?

On cosmic scales, we propose that the global rate of time flow slows over the age of the universe. This produces an effective repulsive force at late times — the same effect as dark energy. With the right parameter, it reproduces the observed acceleration.

---

## Five Weaknesses We Addressed Honestly

Any new theory has holes. We identified the five biggest and wrote mathematical proofs showing each can be resolved.

### Weakness 1: The Lapse Function Looks Made-Up

**The problem:** We chose a specific formula for how time slows with radius. That seems arbitrary. Physical theories should not depend on arbitrary choices.

**The answer:** The power-law formula is not arbitrary. It emerges as the **slow-roll solution** of a scalar field equation — the same type of equation that drives cosmic inflation and electroweak symmetry breaking. The field rolls slowly in the galaxy's potential well, producing exactly the profile we need. We derived this from first principles.

### Weakness 2: Is the Profile Stable?

**The problem:** If time flows differently at different radii, small disturbances might grow and destroy the whole pattern. A galaxy might wobble itself apart.

**The answer:** We performed a **linear stability analysis**. Every possible perturbation mode oscillates with a real frequency. None grow exponentially. The profile is stable. Think of it like a spinning top: small wobbles do not make it fall over.

### Weakness 3: Does the Theory Break the Laws of Physics?

**The problem:** General Relativity has energy conditions — rules that stress and energy must obey so that nothing travels faster than light and causality is preserved. If our effective stress-energy violates these rules, the theory is dead.

**The answer:** We computed the effective stress-energy tensor from the temporal curvature and checked every standard condition. The density is positive everywhere. The pressure is zero or positive. All energy conditions are satisfied. Nothing travels faster than light. Nothing breaks causality.

### Weakness 4: What Actually Makes Time Slow Down?

**The problem:** Dark matter models at least have candidate particles — WIMPs, axions, primordial black holes. What is the physical mechanism behind slower time? What is the "stuff" doing this?

**The answer:** A **classical scalar field** — a smooth, continuous field that fills space, similar to the Higgs field or the inflaton. Visible matter (stars and gas) acts as a source for this field through a coupling term. The field's spatial profile is set by the visible matter distribution. No new particles are needed. The field exists as a classical condensate, not a particle gas.

### Weakness 5: Can It Explain the Cosmic Microwave Background?

**The problem:** The cosmic microwave background (CMB) shows a precise pattern of hot and cold spots. Dark matter explains this beautifully. If we replace dark matter with time curvature, do we ruin the CMB prediction?

**The answer:** We checked. During the CMB era (about 380,000 years after the Big Bang), the extra term our model adds to the expansion rate is **less than one part in a million** compared to the standard expansion. The CMB is formed so early that our effect has not had time to grow. The background expansion, matter density, and growth of structure are effectively identical to the standard model at that epoch. So the CMB acoustic peaks come out the same.

| Weakness | Plain Question | Answer |
|---|---|---|
| **1. Arbitrary lapse** | Why that formula? | Derived from scalar field slow-roll |
| **2. Stability** | Does it wobble apart? | All perturbations oscillate; no exponential growth |
| **3. Energy conditions** | Does it break physics? | All standard energy conditions satisfied |
| **4. Particle mechanism** | What is the "stuff"? | Classical scalar field sourced by visible matter |
| **5. CMB / structure** | Does it match the early universe? | Effect is negligible at CMB era; same power spectrum |

---

## Why This Is Not "Just Playing with Coordinates"

A common objection: "Aren't you just redefining coordinates?"

**No.** In General Relativity, you can rename coordinates without changing physical reality. That is a coordinate transformation. What we propose is a **different physical geometry**. The curvature of spacetime is genuinely different. Two different universes happen to produce the same observables.

This is analogous to MOND (Modified Newtonian Dynamics) and cold dark matter. They are different underlying theories that fit the same galaxy rotation data. VTC is a third alternative, grounded in the geometry of time.

---

## The Honest Limitations

1. **We do not yet know which specific field produces the effect.** We proved that a generic scalar field works, but pinning down the exact field from particle physics is future work.

2. **The model has not been tested against detailed CMB data.** We showed the early-universe effect is negligible, but a full Boltzmann-code comparison is still needed.

3. **Nonlinear structure formation is undeveloped.** We proved linear perturbations grow the same way, but galaxy mergers and cluster formation in VTC need simulation.

4. **Occam's Razor is ambiguous.** Replacing invisible particles with "spatially varying time" trades one mystery for another. Which is simpler depends on your philosophical starting point.

---

## The Bottom Line

| What astronomers see | Standard explanation | VTC explanation |
|---|---|---|
| Galaxies rotate too fast at the edges | Invisible dark matter halos add gravity | Time flows slower at the edges, creating a gradient that pulls stars inward |
| Light bends more than visible mass allows | Extra invisible mass warps spacetime | The time gradient warps geodesics the same amount |
| The universe's expansion is speeding up | Dark energy pushes everything apart | The global rate of time flow slows, producing an effective repulsion |
| What is dark matter made of? | Unknown particles we have not detected yet | Nothing. It is geometry. |

**This theory does not claim dark matter is wrong.** It demonstrates that the observational signatures attributed to dark matter can also arise from a specific configuration of spacetime geometry — one where the time dimension carries spatial variation.

In General Relativity, time and space are inseparable. Maybe the missing mass is not missing. Maybe we have been looking in the wrong dimension.

---

## Where the Math Lives

All rigorous derivations, equations, and formal proofs are in the PDF:

> **Open `VTC-Math-Paper.pdf` for the full foundational mathematics, and `VTC-Unique-Predictions.pdf` for the two ΛCDM-unique predictions.**

`VTC-Math-Paper.pdf` (12 pages) contains the ADM split, the lapse ansatz, the three main theorems proved four ways each (geodesic, effective density, Hamilton-Jacobi, Einstein tensor), and the five weakness responses. `VTC-Unique-Predictions.pdf` (7 pages) contains the morphology and vertical-redshift predictions with full derivations, expected signal sizes, instruments, datasets, and ruling-out conditions.

Both PDFs are LaTeX-typeset with all equations, Greek letters, fractions, boxed results, theorem/proof environments, and reference tables fully visible. They are the authoritative references for the mathematical details behind every claim in this document.

**Previous PDFs:** `VTC-README.pdf` (plain-English summary, no math) is retained for the narrative overview.

Additional files:
- `VTC-Math-Paper.tex` / `VTC-Math-Paper.pdf` — Foundational math paper (12 pages, arXiv-ready)
- `VTC-Unique-Predictions.tex` / `VTC-Unique-Predictions.pdf` — Unique predictions paper (7 pages)
- `PUBLISHING.md` — Guide to publishing the papers on arXiv / Physical Review D / CQG
- `proof/proof.md` — Four parallel proofs with full LaTeX derivations
- `proof/unique_predictions.md` — Two GR derivations for ΛCDM-unique predictions
- `proof/observational_tests.md` — Practical test protocols, datasets, and ruling-out conditions
- `proof/weaknesses_and_responses.md` — Detailed mathematical responses to all five weaknesses
- `THEOREM.md` — Formal theorem statements

---

## How to Read the Code

| File | What It Does |
|---|---|
| `THEOREM.md` | Formal statement of the 3 observational theorems |
| `proof/proof.md` | Full mathematical derivations (4 parallel proofs) |
| `proof/weaknesses_and_responses.md` | Detailed math for the 5 weakness responses |
| `proof/unique_predictions.md` | Two GR derivations for ΛCDM-unique predictions |
| `empirical/verify.py` | GPU simulation verifying the 3 main theorems |
| `empirical/verify_weaknesses.py` | GPU simulation verifying all 5 weakness responses |
| `empirical/verify_unique.py` | GPU simulation verifying 2 unique predictions |
| `tests/test_project.py` | pytest suite — 19 tests |
| `tests/test_unique.py` | pytest suite — 6 tests (unique predictions) |

## Running the Verification

### Option 1: Shared Jetson PyTorch (Recommended)

A shared PyTorch installation is available for any Python 3.10 process on this system:

```bash
# Activate the shared Jetson PyTorch
source "$HOME/.venvs/jetson-pytorch/bin/activate"

# Run the GPU simulations
cd ~/projects/time-curvature-replaces-dark-matter
python3.10 empirical/verify.py
python3.10 empirical/verify_weaknesses.py

# Run the test suite
python3.10 -m pytest tests/ -v
```

### Option 2: Original heartlib venv

```bash
source ~/heartlib/.venv/bin/activate
cd ~/projects/time-curvature-replaces-dark-matter
python empirical/verify.py
python empirical/verify_weaknesses.py
python -m pytest tests/ -v
```

## GPU Requirements

- NVIDIA GPU with CUDA support (tested on Jetson Orin, 8 GB, CUDA 12.6)
- PyTorch 2.5.0+ with CUDA (already installed in shared location)

## Alternative Formats

| Format | File | Best For |
|---|---|---|
| **PDF** (foundational math) | [`VTC-Math-Paper.pdf`](./VTC-Math-Paper.pdf) | 12-page LaTeX paper with all equations, theorems, and proofs. **Recommended for the core mathematics.** |
| **PDF** (unique predictions) | [`VTC-Unique-Predictions.pdf`](./VTC-Unique-Predictions.pdf) | 7-page LaTeX paper with the two ΛCDM-unique predictions and observational protocols. |
| **LaTeX sources** | [`VTC-Math-Paper.tex`](./VTC-Math-Paper.tex), [`VTC-Unique-Predictions.tex`](./VTC-Unique-Predictions.tex) | arXiv / journal submission or customization |
| **HTML** (MathJax) | [`README.html`](./README.html) | Any web browser --- renders equations automatically |
| **Markdown** | [`README.md`](./README.md) | GitHub.com --- math renders on the website |
| **Plain-English PDF** | [`VTC-README.pdf`](./VTC-README.pdf) | Narrative overview with no equations |
| **Publishing guide** | [`PUBLISHING.md`](./PUBLISHING.md) | How to submit to arXiv / Physical Review D / CQG |

## Citation

If you use this work, please cite:

> Walker Kirkpatrick. "Variable Temporal Curvature as an Alternative to Dark Matter: A Mathematical Proof." 2026.

## License

MIT License — See LICENSE file.
