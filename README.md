# Variable Temporal Curvature

### What if dark matter isn't invisible stuff — it's just time, bending?

---

## The Idea (30-Second Version)

Galaxies spin too fast. The stars at the edges should fly off into space — there's not enough visible mass to hold them in orbit. For nearly a century, the answer has been **dark matter**: invisible particles we've never detected, adding extra gravity we can't see.

This project offers a different answer. **What if time itself flows at different rates in different places within a galaxy — and that gradient in time produces exactly the extra gravity we've been attributing to invisible particles?**

It's not as strange as it sounds. Einstein already told us gravity *is* spacetime curvature. We usually assume the time dimension curves the same way everywhere. But nothing in General Relativity requires that. If time flows slightly slower at the edge of a galaxy than at the center, that gradient creates an effective inward force — the same force we call "dark matter."

No new particles. No invisible stuff. Just geometry, doing what geometry does.

---

## Why It Works (Without the Equations)

All the rigorous math lives in the PDFs linked below. Here's the plain-English version of what the math proves.

### Result 1: Flat Galaxy Rotation Curves

Stars at the edge of a galaxy orbit at the same speed as stars in the middle. That's the mystery — Newton's gravity says they should slow down with distance. They don't.

**What VTC says:** If time flows slower at the edges (by about one part in a billion), that gradient adds an extra inward pull. At large distances from the center, this pull exactly matches the observed flat rotation speed. The extra gravity isn't from invisible particles — it's from the shape of time itself.

**The math:** Proved four independent ways — geodesic equation, effective energy density, Hamilton-Jacobi, and Einstein tensor. All four methods give the same answer. See [`VTC-Math-Paper.pdf`](./VTC-Math-Paper.pdf), Theorem 1.

### Result 2: Gravitational Lensing

Light bends when it passes near a galaxy — more than the visible mass can explain. Dark matter accounts for the extra bending.

**What VTC says:** The time gradient bends light too. Photons follow the curvature of spacetime, and if time curves spatially, light curves with it. The deflection angle comes out identical to what an isothermal dark matter halo would produce. Same observable, different mechanism.

**The math:** Proved four ways — gradient integration, Poisson equation, Einstein tensor, and null geodesic integration. See [`VTC-Math-Paper.pdf`](./VTC-Math-Paper.pdf) (Theorem 2) and [`VTC-Extended-Proofs.pdf`](./VTC-Extended-Proofs.pdf) (three additional proofs).

### Result 3: Cosmic Acceleration

The universe's expansion is speeding up. We call the cause **dark energy** — a mysterious repulsive force pushing everything apart.

**What VTC says:** If the global rate of time flow has been slowly decreasing over the age of the universe, that produces an effective repulsion in the same way. The cosmological constant isn't a constant — it's a natural consequence of time curvature that evolves with the age of the universe. No free parameter needed.

**The math:** Proved four ways — proper-time Friedmann decomposition, continuity equation, density ratio analysis, and equation-of-state derivation. See [`VTC-Math-Paper.pdf`](./VTC-Math-Paper.pdf) (Theorem 3) and [`VTC-Extended-Proofs.pdf`](./VTC-Extended-Proofs.pdf) (three additional proofs).

---

## What Makes This Theory Different

VTC isn't just another way to fit the same data. It makes **specific predictions** that standard dark matter cannot produce. If these predictions are observed, they confirm VTC. If they're not, the theory is falsified.

### Two Original Predictions

**Morphology-Dependent Gravity.** In standard dark matter, two galaxies with the same total mass get the same spherical dark matter halo — regardless of whether they're a flat disk or a round bulge. VTC says the time curvature follows the visible matter's shape. A disk galaxy and a bulge galaxy with the same mass should have *different* gravitational fields at the same radius. This is testable with existing telescopes.

→ GPU simulation confirms a 0.14× difference at 5 kpc. ΛCDM predicts 1.0× (identical). See [`VTC-Unique-Predictions.pdf`](./VTC-Unique-Predictions.pdf).

**Vertical Redshift Gradient.** In VTC, the time curvature varies with height above the galactic disk — not just with distance from the center. This creates a linear redshift gradient that standard dark matter (with its spherical halos) doesn't predict. Two stars at the same distance from center but different heights should show a systematic velocity offset of about -2.1 km/s per kilocparsec of height difference.

→ Testable with IFU spectroscopy (MUSE, KCWI). See [`VTC-Unique-Predictions.pdf`](./VTC-Unique-Predictions.pdf).

### Six New Predictions (2025–2026)

Three of these are already supported by recent observations. Three are novel falsifiable predictions awaiting test.

| # | Prediction | What VTC Says | What ΛCDM Says | Status |
|---|---|---|---|---|
| **P3** | Dark energy evolves over time | Automatic — no free parameter | Needs two extra parameters (w₀, wₐ) | **DESI DR2 confirms at 4.2σ** |
| **P4** | Bullet Cluster lensing | Lensing follows the compact stars, not the stripped gas | Dark matter particles pass through collision | Consistent with observations |
| **P5** | JWST early galaxies | Nonlinear collapse enhancement produces 4–10× more massive galaxies at z>10 | Standard model predicts 10× fewer than observed | **JWST data favors VTC** |
| **P6** | Gravitational wave speed varies with redshift | c_GW evolves as α_st²·T(z) — tiny at z=0, grows at distance | Constant = c everywhere | Untested at z>0.01 |
| **P7** | Black hole shadow asymmetry | Galaxy-sourced asymmetry ~7 parts per million for M87* | Exactly zero (Kerr shadow is symmetric) | Untested at ppm precision by EHT |
| **P8** | Pulsar/FRB clock drift | Quadratic in distance (δt ∝ D²), screened locally | Absent entirely | Untested extragalactically |

**All six pass GPU verification** (PyTorch/CUDA, 37/37 pytest tests). See [`VTC-New-Predictions.tex`](./VTC-New-Predictions.tex) for full derivations, `empirical/verify_new_predictions.py` for the simulations, and `empirical/test_new_predictions.py` for the test suite.

---

## How Solid Is the Math?

### Every theorem proved four ways

Each of the three main results (rotation curves, lensing, cosmic acceleration) has been derived independently using four different mathematical methods. When four different approaches converge on the same answer, the result isn't an artifact of one technique — it's robust.

### Extended proofs and formal results

A companion paper ([`VTC-Extended-Proofs.pdf`](./VTC-Extended-Proofs.pdf), 16 pages) adds:

- **Density reconciliation** — resolves an apparent factor-of-α discrepancy between two of the proof methods (one measures kinematics, the other measures dynamics — both correct at their respective levels)
- **Virial theorem equivalence** — VTC produces the same global dynamical constraint as dark matter (U = -v₀²M)
- **Terminal velocity universality** — the flat rotation speed v₀ is independent of the galaxy's visible matter profile shape
- **Not a coordinate trick** — proved by computing the Riemann tensor: VTC spacetime has genuinely different curvature than the visible-matter-only spacetime

### The honest weakness: CMB tension

Here's where we found a real problem, and we're not going to hide it.

The original paper claimed the VTC correction at recombination (when the CMB formed, 380,000 years after the Big Bang) was negligible — less than one part in 10²². **That number was wrong.** The corrected calculation shows the VTC contribution is actually about 50% of the matter density at that epoch. That's not negligible — it's potentially in tension with Planck satellite data, which measures the CMB acoustic peaks to exquisite precision.

This doesn't kill the theory, but it means the minimal model (with a constant parameter β = 0.48) needs modification. Three possible fixes:

1. **Time-varying β(t)** — let the parameter be small in the early universe and grow only at late times
2. **Screening mechanism** — suppress the VTC field in the early universe (similar to chameleon screening)
3. **Modified time profile** — use a non-power-law T(t) that transitions at z ~ 1–2

This is the most serious open challenge to the model and should be the top priority for future work. See [`VTC-Extended-Proofs.pdf`](./VTC-Extended-Proofs.pdf), Proposition 12.

### What the scalar field might be

The VTC effect requires a classical scalar field to generate the lapse function. We showed this field's properties match those of an **ultralight dilaton** from string theory, with a predicted mass around 10⁻²³ eV. Recent work (EPJC 2025) constrains the dilaton mass to ~10⁻²² eV — within one order of magnitude of our estimate.

However, we honestly classify this as a **conjecture, not a theorem**: the mass can't be derived from first principles without specifying the scalar field potential, which is currently a free parameter. See [`VTC-Extended-Proofs.pdf`](./VTC-Extended-Proofs.pdf), Conjecture 11.

---

## Five Weaknesses We Addressed

Every new theory has holes. Here are the five biggest ones and how we addressed them:

| Objection | Response | Where the Math Is |
|---|---|---|
| **"That lapse function looks made up."** | It emerges naturally as the slow-roll solution of a scalar field equation — the same math that drives cosmic inflation | [`VTC-Math-Paper.pdf`](./VTC-Math-Paper.pdf) §5.1 |
| **"Is it stable? Could a galaxy wobble itself apart?"** | Linear stability analysis shows all perturbation modes oscillate — none grow exponentially | [`VTC-Math-Paper.pdf`](./VTC-Math-Paper.pdf) §5.2 |
| **"Does it violate energy conditions? Faster-than-light?"** | All standard energy conditions satisfied. Density positive, pressure non-negative, causality preserved | [`VTC-Math-Paper.pdf`](./VTC-Math-Paper.pdf) §5.3 |
| **"What physical field actually does this?"** | A classical scalar field, sourced by visible matter — like the Higgs field but on galactic scales | [`VTC-Math-Paper.pdf`](./VTC-Math-Paper.pdf) §5.4 |
| **"Does it match the CMB?"** | The early-universe effect was claimed negligible — but see the corrected analysis above. This is an open problem | [`VTC-Extended-Proofs.pdf`](./VTC-Extended-Proofs.pdf) §4.6 |

---

## Running the Code

All simulations run on GPU (PyTorch/CUDA) and all tests pass.

### Original theorems + weaknesses + unique predictions

```bash
source "$HOME/.venvs/jetson-pytorch/bin/activate"
cd ~/projects/time-curvature-replaces-dark-matter

python3.10 empirical/verify.py              # 3 theorems, 19/19 pass
python3.10 empirical/verify_weaknesses.py   # 5 weaknesses, 6/6 pass
python3.10 -m pytest tests/ -v              # 25 tests total
```

### Six new predictions (P3–P8)

```bash
python3.10 empirical/verify_new_predictions.py      # 6/6 pass, generates plots
python3.10 -m pytest empirical/test_new_predictions.py -v  # 37 tests
```

**Requirements:** NVIDIA GPU with CUDA, PyTorch 2.5.0+. Tested on Jetson (8 GB, CUDA 12.6).

---

## Where Everything Lives

### Papers (PDF — read these for the math)

| Paper | Pages | What's In It |
|---|---|---|
| [`VTC-Math-Paper.pdf`](./VTC-Math-Paper.pdf) | 12 | The three foundational theorems, each proved four ways. The five weakness responses. The core mathematics. **Start here.** |
| [`VTC-Unique-Predictions.pdf`](./VTC-Unique-Predictions.pdf) | 7 | The two predictions that ΛCDM cannot make (morphology-dependent gravity, vertical redshift gradient). Observational protocols. |
| [`VTC-Extended-Proofs.pdf`](./VTC-Extended-Proofs.pdf) | 16 | Three additional proofs each for Theorems 2 & 3 (completing the four-proof standard). Six new formal results. The corrected CMB analysis. |
| [`VTC-README.pdf`](./VTC-README.pdf) | — | Plain-English narrative overview with no equations |

### LaTeX sources (for arXiv / journal submission)

- [`VTC-Math-Paper.tex`](./VTC-Math-Paper.tex) — foundational paper
- [`VTC-Unique-Predictions.tex`](./VTC-Unique-Predictions.tex) — unique predictions
- [`VTC-New-Predictions.tex`](./VTC-New-Predictions.tex) — six new predictions (P3–P8)
- [`VTC-Extended-Proofs.tex`](./VTC-Extended-Proofs.tex) — extended proofs and formal propositions

### Markdown proofs (working documents)

- [`proof/proof.md`](./proof/proof.md) — four parallel proofs with full derivations
- [`proof/unique_predictions.md`](./proof/unique_predictions.md) — two ΛCDM-unique prediction derivations
- [`proof/new_predictions.md`](./proof/new_predictions.md) — six new prediction proofs (P3–P8)
- [`proof/weaknesses_and_responses.md`](./proof/weaknesses_and_responses.md) — five weakness responses
- [`proof/observational_tests.md`](./proof/observational_tests.md) — practical test protocols and datasets
- [`THEOREM.md`](./THEOREM.md) — formal theorem statements

### Code (GPU simulations + tests)

- [`empirical/verify.py`](./empirical/verify.py) — simulates the 3 main theorems (19/19 pass)
- [`empirical/verify_weaknesses.py`](./empirical/verify_weaknesses.py) — simulates the 5 weakness responses (6/6 pass)
- [`empirical/verify_new_predictions.py`](./empirical/verify_new_predictions.py) — simulates P3–P8 (6/6 pass)
- [`empirical/test_new_predictions.py`](./empirical/test_new_predictions.py) — pytest suite for P3–P8 (37/37 pass)
- [`tests/test_project.py`](./tests/test_project.py) — pytest suite for original theorems (19 tests)
- [`tests/test_unique.py`](./tests/test_unique.py) — pytest suite for unique predictions (6 tests)

### Plots

- [`paper/vtc_w_of_z.png`](./paper/vtc_w_of_z.png) — VTC w(z) vs DESI DR2
- [`paper/vtc_bullet_cluster.png`](./paper/vtc_bullet_cluster.png) — Bullet Cluster gradient map
- [`paper/vtc_jwst_collapse.png`](./paper/vtc_jwst_collapse.png) — JWST halo abundance
- [`paper/vtc_gw_speed.png`](./paper/vtc_gw_speed.png) — GW speed vs redshift
- [`paper/vtc_bh_shadow.png`](./paper/vtc_bh_shadow.png) — BH shadow asymmetry
- [`paper/vtc_clock_drift.png`](./paper/vtc_clock_drift.png) — Pulsar clock drift

### Other

- [`PUBLISHING.md`](./PUBLISHING.md) — guide to submitting to arXiv / Physical Review D / CQG
- [`README.html`](./README.html) — MathJax-rendered version for browsers

---

## The Bottom Line

| What astronomers see | Standard explanation | VTC explanation |
|---|---|---|
| Galaxies rotate too fast at the edges | Invisible dark matter adds gravity | Time flows slower at the edges, creating a gradient that pulls stars inward |
| Light bends more than visible mass allows | Extra invisible mass warps spacetime | The time gradient bends light the same amount |
| The universe's expansion is speeding up | Dark energy pushes everything apart | The global rate of time flow slows, producing effective repulsion |
| What is dark matter made of? | Unknown particles we haven't detected | Nothing. It's geometry. |

This theory doesn't claim dark matter is wrong. It demonstrates that the observational signatures attributed to dark matter can also arise from a specific configuration of spacetime geometry — one where the time dimension carries spatial variation.

In General Relativity, time and space are inseparable. Maybe the missing mass isn't missing. Maybe we've been looking in the wrong dimension.

---

## Citation

> Walker Kirkpatrick. "Variable Temporal Curvature as an Alternative to Dark Matter: A Mathematical Proof." 2026.

## License

MIT License — See [LICENSE](./LICENSE) file.