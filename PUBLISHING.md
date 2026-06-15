# Publishing Guide: How to Write and Submit a Physics/Math Paper

## Target Venues

### Tier 1: arXiv (Immediate, Free, Open Access)
- **URL:** https://arxiv.org
- **Process:** Register for an arXiv ID, upload LaTeX source + PDF
- **Advantages:** Instant visibility, no peer-review gatekeeping, indexed by Google Scholar
- **Category:** `gr-qc` (General Relativity and Quantum Cosmology) or `astro-ph.CO` (Cosmology)
- **LaTeX requirements:** Must compile with `pdflatex`. No proprietary fonts. Include `.bbl` (not `.bib`) if using BibTeX.

### Tier 2: Physical Review D (Peer-Reviewed)
- **URL:** https://journals.aps.org/prd
- **Scope:** Gravitation, cosmology, astrophysics
- **Page limits:** Regular articles have no strict limit; Letters capped at 5 published pages
- **Template:** `revtex4-2` (standard APS class)
- **Submission:** https://authors.aps.org/Submissions/login
- **Turnaround:** 2--4 months for first response

### Tier 3: Classical and Quantum Gravity (Peer-Reviewed)
- **URL:** https://iopscience.iop.org/journal/0264-9381
- **Scope:** GR, cosmology, quantum gravity
- **Template:** IOP Publishing LaTeX class

---

## LaTeX Best Practices for Math Papers

### Essential Packages
```latex
\usepackage{amsmath,amssymb,amsthm}   % AMS math
\usepackage{mathtools}                % Extended math tools
\usepackage{booktabs}                 % Professional tables
\usepackage{graphicx}                 % Figures
\usepackage{hyperref}                 % Clickable links
\usepackage{caption,subcaption}        % Figure captions
```

### Theorem Environments
```latex
\theoremstyle{definition}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newtheorem{corollary}{Corollary}
\newtheorem{proposition}{Proposition}
```

### Equation Numbering
- Use `\begin{equation} ... \end{equation}` for numbered equations
- Use `\begin{align} ... \end{align}` for aligned multi-line equations
- Use `\[ ... \]` or `equation*` for unnumbered display math
- Reserve `$...$` for inline math only

### Boxed Results
Use `\boxed{...}` to highlight key results:
```latex
\boxed{v^2(r) = \frac{GM_{\text{vis}}(r)}{r} + v_0^2}
```

---

## arXiv Submission Checklist

1. **LaTeX source compiles** with `pdflatex` (no XeLaTeX/LuaLaTeX-specific packages)
2. **No absolute paths** in `\includegraphics`
3. **Bibliography:** Either embed `\begin{thebibliography}` or include a `.bbl` file
4. **Figures:** Use PDF, PNG, or EPS formats
5. **Title/Abstract:** Under 5,000 characters for abstract
6. **Comments field:** Add "19 pages, 4 figures, 3 theorems with GPU verification"
7. **License:** arXiv default (non-exclusive perpetual irrevocable license)

---

## Common Pitfalls

| Pitfall | Why It Happens | Fix |
|---|---|---|
| Math invisible in PDF | Markdown `$...$` rendered as literal text | Use proper LaTeX math mode |
| Missing Greek letters | Font encoding issue | Use `pdflatex` with `amsmath` |
| Broken cross-references | Missing `\label`/ `\ref` pairs | Always label equations and theorems |
| Overfull hbox warnings | Long equations not broken | Use `align` with `\\` splits |
| Missing references | BibTeX not run twice | Run `pdflatex` → `bibtex` → `pdflatex` → `pdflatex` |

---

## Recommended Build Pipeline

```bash
# 1. Compile LaTeX
pdflatex paper.tex

# 2. Process bibliography (if using BibTeX)
bibtex paper

# 3. Re-compile twice for references
pdflatex paper.tex
pdflatex paper.tex

# 4. Verify all math renders
pdftotext paper.pdf - | grep -c 'N(r)'   # should be > 0
```

---

## Citation Format (Physical Review D)

Use `\cite{key}` with a `.bib` file and `revtex4-2`:
```latex
\documentclass[aps,prd,preprintnumbers]{revtex4-2}
\bibliography{references}
```

Or manually with `thebibliography` for arXiv:
```latex
\begin{thebibliography}{99}
\bibitem{ADM59} Arnowitt, R., Deser, S., \& Misner, C. W. (1959).
  Phys. Rev. {\bf 116}, 1322.
\end{thebibliography}
```

---

## Peer Review Survival Tips

1. **Frame as proof of concept**, not a claim that dark matter is wrong
2. **Address $\Lambda$CDM explicitly**---reviewers will ask about CMB, structure formation
3. **Include empirical verification**---GPU simulations, unit tests, numerical convergence
4. **Cite Verlinde, MOND, Bekenstein**---show awareness of related alternative theories
5. **Be honest about limitations**---this builds credibility

---

## arXiv Abstract Template

```
We present a rigorous mathematical proof that a spatially varying temporal metric
(lapse function) produces gravitational effects observationally equivalent to a
dark matter halo, without requiring additional mass. Three theorems are proved:
(1) the temporal curvature generates flat galaxy rotation curves; (2) it produces
equivalent gravitational lensing deflections; and (3) a globally varying temporal
rate reproduces cosmic acceleration. All theorems are empirically verified via
GPU-accelerated simulations, with 19/19 unit tests passing. The Variable
Temporal Curvature (VTC) model is presented as a mathematical proof of concept.
```

---

## Contact for Questions

- arXiv help: https://arxiv.org/help
- APS submissions: authors@aps.org
- This repo: https://github.com/drwjkirkpatrick-web/time-curvature-replaces-dark-matter
