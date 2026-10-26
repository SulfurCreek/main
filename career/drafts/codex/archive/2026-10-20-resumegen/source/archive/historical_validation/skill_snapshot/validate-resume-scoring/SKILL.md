---
name: validate-resume-scoring
description: Validate, calibrate, or audit resume scoring systems and then apply them to resumes. Use when asked to test a resume rubric with synthetic resumes, separate generator and grader models, rank resumes from poor to excellent, check score reliability or bias, assign a resume to a quality spectrum, or distinguish content quality from PDF/ATS and AI-authorship checks.
---

# Validate Resume Scoring

Treat a resume score as a diagnostic instrument. Do not present it as hiring truth.

## Run the validation

1. Freeze the rubric, target jobs, score anchors, acceptance thresholds, and randomization seed before grading.
2. Have one model generate the corpus and hidden answer key. Use a separate fresh model or agent for grading. Give the grader only randomized resumes, full target jobs, and the frozen rubric.
3. Build a balanced corpus across roles and quality. For a 50-resume test, use ten quality levels with five roles per level.
4. Derive target dimension scores from explicit feature flags. Do not lower every dimension merely because the overall resume is weak. A resume may have clear structure and weak achievements.
5. Include controlled pairs that change one dimension at a time. Balance roles, metric types, managerial scope, language style, and quantified versus qualitative outcomes.
6. Record hashes of the grader inputs. Keep answers and generation code outside the grader-visible directory.
7. Calculate rank agreement, score calibration, cross-level inversions, per-dimension error, and same-level role spread. Use `scripts/evaluate_calibration.py` for the deterministic calculations.
8. Preserve failed thresholds. Tune only on a calibration split, then generate or reserve an untouched holdout set. Never reuse the same evaluated set as proof that a revised rubric works.

Read [references/validation-design.md](references/validation-design.md) when designing or interpreting a corpus.

## Apply the result to a resume

Report these separately:

- **Spectrum level (1–10):** the primary summary. Cite the evidence and give an uncertainty of one level unless independent labels justify narrower precision.
- **Dimension profile:** positioning, evidence, target-role fit, decision depth and attribution, structure, and wording. Avoid converting small numeric differences into confident ranking claims.
- **HR screen:** likely initial impression, credibility questions, career narrative, seniority signal, and interview risks.
- **PDF/ATS status:** test extraction, reading order, and actual target ATS import separately. If no import was performed, state `not tested`.
- **AI provenance:** use `indeterminate from text alone` unless there is generation history or another provenance record. Discuss template-like writing only as an editing issue.

Use [references/level-spectrum.md](references/level-spectrum.md) to assign the level. If the rubric has failed calibration, do not issue a precise total as the main result. A raw diagnostic score may be shown only with its calibration error and limitations.

## Guardrails

- Do not equate quantified claims with verified truth.
- Do not reward terminology, employer prestige, school prestige, or management scope by default.
- Do not penalize missing people management unless the target job requires it.
- Do not double-count one strength or defect across dimensions without distinct evidence.
- Treat dates, attribution, denominators, comparison cohorts, and causal language as verification questions rather than accusations.
- Keep internal synthetic calibration, human inter-rater reliability, real hiring outcomes, PDF/ATS parsing, and AI provenance as separate tests.
