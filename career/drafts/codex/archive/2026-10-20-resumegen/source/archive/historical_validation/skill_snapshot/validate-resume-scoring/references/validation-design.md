# Validation design

## Corpus

For 50 resumes, balance five roles across ten levels. Define each resume with independent feature flags:

- target and career continuity
- relevant scope
- action or deliverable
- outcome
- period and population
- baseline or comparison
- source or calculation definition
- individual versus team ownership
- tradeoff or decision reasoning
- limitation or alternative explanation
- readable structure
- precise wording

Compute hidden dimension targets from these flags. Do not infer all dimension targets from the overall level.

Include at least ten single-variable pairs. Examples: the same facts in plain versus jargon-heavy wording; one added measurement denominator; one added responsibility boundary; an unexplained versus explained date overlap; identical content with a different role family.

## Separation

- Put randomized resumes and the frozen rubric in a grader-visible directory.
- Put answer keys, seeds, generation code, and hypotheses elsewhere.
- Use a fresh independent grader context when possible.
- Do not ask the grader to create a ranking. Score each resume independently.
- Hash inputs and record model availability, tool limits, and any data correction.

## Metrics

Pre-register thresholds. At minimum calculate:

- Spearman correlation between target and graded totals
- Kendall rank agreement between target levels and graded totals
- mean absolute error and signed bias
- count within the expected score interval
- adjacent-level mean monotonicity
- strict inversions for pairs separated by at least two levels
- per-dimension MAE and bias
- score spread among roles at the same target level

High rank agreement with poor MAE means the system orders resumes but does not support precise numerical claims. A ceiling at high levels means the anchors cannot distinguish strong from excellent resumes.

## Failure and revision

Keep the failed result. Identify whether the defect is in the grader, rubric, or answer key. Common answer-key defects include forcing clean structure to score poorly because achievements are weak.

Revise with a calibration subset. Validate the revision on untouched holdout resumes or a newly generated corpus. Describe same-set rescoring as regression testing only.

Synthetic success is internal consistency. Real hiring validity requires anonymized real resumes, complete target jobs, at least two HR or hiring-manager raters, human inter-rater analysis, and later-stage outcomes where available.
