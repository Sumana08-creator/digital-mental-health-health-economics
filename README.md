# Digital Mental Health: Health Economic Evaluation Portfolio

An independent, reproducible skills demonstration covering cost-effectiveness analysis (CEA), budget impact analysis (BIA), equity-stratified reporting, and deterministic sensitivity analysis.

**All data and parameters are synthetic and illustrative. They are not SAMPO trial data, not evidence about the real SAMPO intervention, and must not be used for clinical, commissioning, reimbursement, or policy decisions. This portfolio does not claim prior paid health-economics experience.**

## Question
For a hypothetical digital mental-health support programme compared with usual support, what are the illustrative incremental costs and health outcomes, how does the budget impact vary by uptake and eligible population, and how do descriptive outcomes differ across a synthetic access grouping?

## Methods
- Illustrative health-service payer perspective and 12-month horizon.
- Approximate QALY calculated as the mean of baseline and follow-up utility for demonstration only.
- ICER = incremental cost / incremental QALYs; dominance and optional net monetary benefit also reported.
- Budget impact varies eligible population, uptake, implementation cost, per-user cost, and assumed offsets.
- Equity summaries disaggregate synthetic costs and outcomes by access group; they are descriptive, not causal or a fairness certification.
- One-way scenario sensitivity analysis varies programme cost and incremental QALYs.
- €30,000/QALY is included only as a configurable demonstration input, not asserted as an official threshold for any country.

## Structure
- `data/synthetic_cohort.csv` — 1,000 simulated participants.
- `src/health_economics.py` — reusable calculation functions.
- `run_analysis.py` — generates tables in `outputs/`.
- `tests/test_health_economics.py` — unit tests.
- `outputs/` — generated summaries.

## Run
Python 3.10+ recommended.
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python run_analysis.py
python -m unittest discover -s tests -v
```

## Data dictionary
`participant_id` is synthetic; `group` is `Digital_support` or `Usual_support`; `access_group` is `Higher_access` or `Lower_access`; `baseline_utility` and `followup_utility` are simulated 0–1 utility scores; `health_service_cost_eur` and `programme_cost_eur` are simulated 12-month costs; `improved` is a simulated binary outcome.

## Interpretation safeguards
An ICER is not interpreted in isolation. Negative or near-zero incremental QALYs require particular care. Cost-effectiveness and affordability are different questions. Synthetic subgroup differences do not demonstrate real-world inequity or effect modification. For real evaluation, use appropriately governed data, pre-specify methods, justify the perspective and horizon, document parameter sources, and follow applicable health-economic guidance.

## Future improvements
Add probabilistic sensitivity analysis (PSA), cost-effectiveness planes and acceptability curves, discounting for longer horizons, model validation, parameter-source register, and reporting aligned to the relevant study protocol and health-economic guidance.

Author: Sumana Shivaprakash — independent portfolio project.
