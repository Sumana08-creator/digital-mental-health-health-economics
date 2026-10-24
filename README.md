# Health Economic Evaluation Portfolio: Digital Mental Health Intervention

**A reproducible Python-based health economics project demonstrating cost-effectiveness analysis, budget impact analysis, health equity assessment, and deterministic sensitivity analysis using synthetic data.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Analysis](https://img.shields.io/badge/Analysis-Health%20Economics-teal)
![Methods](https://img.shields.io/badge/Methods-CEA%20%7C%20BIA%20%7C%20Equity-orange)
![Data](https://img.shields.io/badge/Data-Synthetic-lightgrey)
![Status](https://img.shields.io/badge/Status-Research%20Portfolio-brightgreen)

---

## 1. Project Overview

This project demonstrates a reproducible analytical workflow for evaluating the potential economic value, budgetary implications, and distributional considerations of a hypothetical digital mental health intervention.

The project was developed as a practical health economics portfolio to demonstrate the application of quantitative methods to health service evaluation and resource allocation.

It combines synthetic participant-level data, Python-based analytical functions, automated tests, and structured output files to illustrate how economic evidence can be generated, organised, and interpreted.

The analytical workflow focuses on four areas:

1. **Cost-effectiveness analysis (CEA):** Comparing incremental costs and estimated health outcomes between a hypothetical intervention and a comparator.
2. **Budget impact analysis (BIA):** Exploring how intervention uptake, eligible population size, implementation costs, and assumed cost offsets may influence budgetary requirements.
3. **Health equity assessment:** Describing differences in costs and health-related outcomes across illustrative population groups with different levels of access.
4. **Deterministic sensitivity analysis:** Examining how changes in selected economic and health-outcome assumptions affect estimated cost-effectiveness.

The project also incorporates unit tests and a documented execution workflow to support reproducibility and analytical quality assurance.

> **Important research qualification:** All participant data and model inputs used in this portfolio are synthetic or illustrative. The results are not findings from the SAMPO project, a clinical trial, or an observational study. They do not establish the clinical effectiveness, cost-effectiveness, affordability, or equity impact of any real intervention.

---

## 2. Research Rationale

Healthcare systems must make decisions about how to allocate limited resources across competing services and interventions.

Digital mental health interventions may offer opportunities to expand access to support, but their economic value depends on several factors, including:

* The cost of developing, implementing, and maintaining the intervention.
* The number and characteristics of eligible participants.
* Intervention uptake and engagement.
* The health outcomes achieved relative to existing care.
* Changes in healthcare resource utilisation.
* The distribution of costs and benefits across population groups.
* Uncertainty in intervention costs, outcomes, and model assumptions.

An intervention that improves outcomes may not necessarily represent good value for money. Similarly, an intervention that appears cost-effective at the individual level may still create substantial short-term budgetary requirements when implemented across a large eligible population.

Economic evaluation therefore requires consideration of both efficiency and affordability, alongside questions about who benefits and whether access is distributed equitably.

This project uses a simplified, hypothetical digital mental health intervention to demonstrate how these questions can be translated into a structured analytical workflow.

---

## 3. Project Objectives

### Objective 1: Demonstrate cost-effectiveness analysis

Estimate the incremental costs and approximate health-related quality-adjusted life-year (QALY) outcomes associated with a hypothetical intervention compared with a comparator.

The analysis demonstrates the calculation and interpretation of:

* Intervention and comparator costs.
* Incremental costs.
* Approximate QALY outcomes.
* Incremental QALYs.
* Incremental cost-effectiveness ratios.
* Incremental improvement rates.
* Illustrative net monetary benefit.

### Objective 2: Demonstrate budget impact analysis

Explore the potential financial implications of implementing an intervention under alternative scenarios.

The analysis considers parameters such as:

* Eligible population size.
* Intervention uptake.
* Cost per participant.
* Implementation costs.
* Assumed cost offsets.

The purpose is to illustrate how assumptions about implementation and uptake can influence the estimated budget impact.

### Objective 3: Examine distributional differences

Produce descriptive summaries comparing illustrative population groups categorised by access level.

This component demonstrates how an analyst might begin investigating whether costs and health-related outcomes differ across population groups.

The analysis is exploratory and does not establish that differences are caused by access, socioeconomic circumstances, or the intervention.

### Objective 4: Assess parameter uncertainty

Conduct deterministic sensitivity analysis by varying selected intervention-cost and incremental-QALY assumptions.

This helps demonstrate how changes in key model inputs can affect estimated incremental cost-effectiveness.

### Objective 5: Establish a reproducible analytical workflow

Organise the project into separate data, analytical, testing, and output components.

The workflow is designed to support:

* Repeated execution.
* Consistent output generation.
* Separation of analysis logic from generated results.
* Basic automated testing.
* Transparent documentation of assumptions and limitations.

---

## 4. Analytical Framework

The project uses four complementary analytical components.

| Component                          | Main question                                                                     | Analytical approach                    | Main output                  |
| ---------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------- | ---------------------------- |
| Cost-effectiveness analysis        | What additional cost is associated with the estimated additional health outcome?  | Incremental cost and QALY calculations | Cost-effectiveness summary   |
| Budget impact analysis             | What might implementation cost under alternative uptake and population scenarios? | Scenario-based financial modelling     | Budget impact scenarios      |
| Equity assessment                  | How do descriptive outcomes differ between illustrative access groups?            | Group-level descriptive summaries      | Equity summary               |
| Deterministic sensitivity analysis | How sensitive are the results to selected assumptions?                            | Parameter variation                    | Sensitivity analysis results |

These analyses address related but distinct decision questions. They should not be treated as interchangeable.

Cost-effectiveness analysis concerns the relationship between additional costs and additional health outcomes. Budget impact analysis focuses on the financial consequences of adopting an intervention. Equity assessment examines the distribution of outcomes, while sensitivity analysis explores how assumptions influence the results.

---

## 5. Data and Simulation Design

### 5.1 Data source

The project uses a synthetic cohort dataset stored at:

`data/synthetic_cohort.csv`

The dataset contains 1,000 simulated participants.

The observations are generated for methodological demonstration rather than collected from real patients.

The dataset should not be interpreted as representing a particular hospital, country, clinical population, mental health service, or intervention trial.

### 5.2 Purpose of synthetic data

Synthetic data make it possible to demonstrate the structure of an analytical workflow without exposing personal health information or misrepresenting access to clinical research data.

They also allow the analysis to be executed independently of a restricted research environment.

The synthetic dataset provides a starting point for demonstrating:

1. Participant-level data handling.
2. Economic calculations.
3. Group-level descriptive analysis.
4. Scenario modelling.
5. Sensitivity analysis.
6. Automated testing.

### 5.3 Illustrative population groups

The project includes illustrative access categories:

* `Higher_access`
* `Lower_access`

These categories are used to demonstrate group-level summaries.

They should not be interpreted as validated measures of health inequality, socioeconomic deprivation, digital exclusion, or barriers to care.

Any real-world equity assessment would require a clearly defined conceptual framework, appropriate variables, suitable population data, and a justified analytical approach.

### 5.4 Data quality considerations

Before applying this workflow to real research data, the analyst would need to assess:

* Missing observations.
* Duplicate participant records.
* Variable definitions and units.
* Plausibility of cost values.
* Validity and range of health-outcome measures.
* Consistency of intervention and comparator definitions.
* Alignment of follow-up periods.
* The appropriate treatment of incomplete follow-up.
* The provenance and reliability of each input variable.

These checks are important because errors in source data can affect incremental cost estimates, QALY calculations, and subsequent economic conclusions.

---

## 6. Cost-Effectiveness Analysis

### 6.1 Purpose

Cost-effectiveness analysis evaluates the additional cost associated with an intervention relative to its additional health benefit.

In this project, the analysis uses approximate 12-month QALY outcomes to demonstrate incremental economic evaluation.

A QALY combines information about health-related quality of life and time spent in a particular health state. A QALY is a measure of health outcome rather than a monetary value.

The interpretation of QALYs depends on how health-related quality of life is measured, how outcomes are valued, and how changes over time are handled.

### 6.2 Incremental costs

Incremental cost is calculated as:

$$
\Delta C = C_I - C_C
$$

Where:

* \(\Delta C\) = incremental cost.
* \(C_I\) = cost associated with the intervention.
* \(C_C\) = cost associated with the comparator.

A positive incremental cost means that the intervention costs more than the comparator under the assumptions used.

A negative incremental cost indicates that the intervention costs less.

### 6.3 Incremental health outcomes

Incremental QALYs are calculated as:

$$
\Delta Q = Q_I - Q_C
$$

Where:

* \(\Delta Q\) = incremental QALYs.
* \(Q_I\) = QALY outcome associated with the intervention.
* \(Q_C\) = QALY outcome associated with the comparator.

Positive incremental QALYs indicate a higher estimated QALY outcome for the intervention.

Negative incremental QALYs indicate a lower estimated QALY outcome.

The calculations in this portfolio are approximate and illustrative. They do not constitute a validated patient-level QALY analysis.

### 6.4 Incremental cost-effectiveness ratio

The incremental cost-effectiveness ratio (ICER) is calculated as:

$$
ICER = \frac{\Delta C}{\Delta Q}
$$

The ICER expresses the incremental cost per additional QALY when incremental QALYs are positive and the ratio is interpretable.

The ratio must be considered alongside the underlying incremental costs and health outcomes. It should not be interpreted in isolation, particularly when incremental effects are zero or negative.

### 6.5 Illustrative net monetary benefit

Net monetary benefit (NMB) provides an alternative way to express the relationship between health outcomes and costs.

The conventional incremental net monetary benefit is:

$$
\Delta NMB = \lambda \Delta Q - \Delta C
$$

Where:

* \(\Delta NMB\) = incremental net monetary benefit.
* \(\lambda\) = illustrative monetary value assigned to one additional QALY.
* \(\Delta Q\) = incremental QALYs.
* \(\Delta C\) = incremental costs.

This portfolio uses an illustrative threshold of **€30,000 per QALY** in its reported summary.

That value is a modelling assumption, not a recommendation for a particular healthcare system or an official decision threshold applicable to the SAMPO project.

A positive incremental NMB indicates that the intervention has a positive net monetary benefit under the specified assumptions. It does not, by itself, demonstrate that the intervention is clinically effective or suitable for adoption.

### 6.6 Illustrative results

The current synthetic analysis produces the following approximate results:

| Measure                                          | Illustrative result |
| ------------------------------------------------ | ------------------: |
| Incremental cost per participant                 |              €58.66 |
| Incremental approximate QALYs                    |            0.016172 |
| ICER                                             |     €3,627 per QALY |
| Incremental improvement rate                     |               0.054 |
| Illustrative incremental NMB at €30,000 per QALY |             €426.50 |

Values are rounded for presentation.

The incremental improvement rate is reported as produced by the current implementation. Its precise interpretation depends on the definition and denominator used in the code.

The ICER is an approximate result calculated from synthetic inputs. It should not be interpreted as an estimate of the cost-effectiveness of an actual digital mental health intervention.

Likewise, the illustrative NMB is conditional on the model's cost and outcome definitions and the assumed €30,000-per-QALY threshold.

These results are included to demonstrate analytical implementation, not to make a clinical, commissioning, reimbursement, or policy recommendation.

---

## 7. Budget Impact Analysis

### 7.1 Purpose

Budget impact analysis (BIA) estimates the financial consequences of introducing an intervention into a defined healthcare setting over a specified period.

Unlike cost-effectiveness analysis, which considers incremental costs relative to health outcomes, BIA focuses on the expected budgetary consequences of adoption.

An intervention may appear cost-effective but still be difficult to implement if the eligible population is large or substantial upfront investment is required.

### 7.2 Scenario modelling

The project generates budget impact scenarios using assumptions concerning:

* The eligible population.
* Intervention uptake.
* Cost per participant.
* Implementation costs.
* Assumed cost offsets.

The purpose is to demonstrate how changes in implementation assumptions may influence the estimated financial requirement.

### 7.3 Conceptual calculation

A simplified budget impact model can be represented as:

$$
B = N \times U \times C + I - O
$$

Where:

* \(B\) = net budget impact.
* \(N\) = eligible population.
* \(U\) = intervention uptake proportion.
* \(C\) = cost per participant.
* \(I\) = implementation cost.
* \(O\) = assumed cost offsets.

This equation is a conceptual illustration. The exact calculations in the repository are determined by the implementation in `src/health_economics.py`.

In a real application, the analyst would need to define the perspective, time horizon, target population, relevant cost categories, implementation assumptions, and treatment of offsets.

### 7.4 Interpreting the scenarios

The generated file:

`outputs/budget_impact_scenarios.csv`

contains the scenario-based budget impact results.

The scenarios are useful for exploring the financial implications of alternative assumptions. They do not represent actual healthcare expenditure forecasts.

A real-world budget impact analysis would require setting-specific information about population size, expected uptake, implementation arrangements, resource use, unit costs, and the period over which the budget impact is assessed.

---

## 8. Health Equity Assessment

### 8.1 Purpose

Economic evaluations can conceal important differences in the distribution of costs and health benefits.

An intervention may improve average outcomes while leaving some groups with limited access to its benefits.

For this reason, examining outcomes across population groups can provide additional information beyond an overall cost-effectiveness estimate.

### 8.2 Current approach

This project produces descriptive summaries for the illustrative `Higher_access` and `Lower_access` groups.

The analysis demonstrates how outcomes can be organised and compared across groups as an initial step in a broader equity assessment.

The resulting output is stored in:

`outputs/equity_summary.csv`

### 8.3 Interpretation

Group-level differences may indicate patterns that warrant further investigation.

However, descriptive differences do not establish causation.

They cannot demonstrate that access level caused differences in costs or health outcomes. The categories may also omit other factors that influence the observed results.

### 8.4 Potential extensions

A more comprehensive equity-focused economic evaluation could investigate:

* Differences in intervention uptake.
* Differences in intervention completion.
* Health outcomes across relevant population groups.
* Differences in resource use and costs.
* Digital access and digital literacy.
* Socioeconomic disadvantage.
* Geographic variation in service availability.
* Distribution of incremental health benefits.
* Potential trade-offs between total health gain and the distribution of that gain.

Any extension would require appropriate data, justified group definitions, a clear analytical framework, and careful consideration of sample size and uncertainty.

---

## 9. Deterministic Sensitivity Analysis

### 9.1 Purpose

Economic evaluations rely on assumptions about costs, outcomes, resource use, and other parameters.

If these assumptions are uncertain, the resulting ICER and related measures may also be uncertain.

Deterministic sensitivity analysis examines how selected changes in model inputs affect the estimated results.

### 9.2 Current implementation

The project varies selected assumptions concerning:

* Programme costs.
* Incremental QALYs.

The analysis produces a set of alternative results that can be used to examine how the cost-effectiveness estimate changes under different input assumptions.

The output is stored in:

`outputs/deterministic_sensitivity.csv`

### 9.3 Interpretation

Sensitivity analysis can help identify parameters that materially influence the model results.

For example, an intervention's estimated ICER may change if programme costs increase or the incremental QALY gain decreases.

The results remain conditional on the parameters selected and the range of values examined.

The current analysis is deterministic. It does not estimate a joint probability distribution for uncertain parameters and does not quantify the probability that an intervention is cost-effective.

### 9.4 Potential extensions

Further development could include:

* Probabilistic sensitivity analysis.
* Appropriate probability distributions for uncertain parameters.
* Joint simulation of costs and health outcomes.
* A cost-effectiveness plane.
* A cost-effectiveness acceptability curve.
* Scenario analyses for alternative perspectives and time horizons.
* Alternative assumptions concerning missing data and treatment effects.

These methods would require additional implementation and validation. They are not claimed to be part of the current version of the project.

---

## 10. Repository Structure

The repository separates the data, analytical code, automated tests, and generated results.

```text
SAMPO_Health_Economic_Evaluation_Portfolio/
│
├── README.md
├── requirements.txt
├── run_analysis.py
├── LICENSE
├── .gitignore
│
├── data/
│   └── synthetic_cohort.csv
│
├── src/
│   └── health_economics.py
│
├── tests/
│   └── test_health_economics.py
│
└── outputs/
    ├── budget_impact_scenarios.csv
    ├── cost_effectiveness_by_group.csv
    ├── cost_effectiveness_summary.csv
    ├── deterministic_sensitivity.csv
    └── equity_summary.csv
```

### File descriptions

| File or directory                | Purpose                                                                |
| -------------------------------- | ---------------------------------------------------------------------- |
| `README.md`                      | Documents the project, methods, assumptions, results, and limitations. |
| `requirements.txt`               | Lists the Python dependencies required by the project.                 |
| `run_analysis.py`                | Entry point for executing the analytical workflow.                     |
| `LICENSE`                        | Specifies the terms under which the project may be reused.             |
| `.gitignore`                     | Excludes generated or unnecessary files from version control.          |
| `data/synthetic_cohort.csv`      | Contains the simulated participant-level dataset.                      |
| `src/health_economics.py`        | Contains the health economics calculations and analytical functions.   |
| `tests/test_health_economics.py` | Contains automated tests for selected analytical functions.            |
| `outputs/`                       | Contains generated CSV files from the analysis.                        |

The `outputs` directory contains results generated by the project. The analytical functions and execution script should be consulted when investigating how those results were produced.

---

## 11. Technology Stack

The project uses Python for data analysis and reproducible computation.

The dependency list is maintained in `requirements.txt`.

The analytical workflow is organised around:

* **Python:** Analytical logic and execution.
* **Pandas:** Structured data handling and tabular outputs.
* **NumPy:** Numerical computation, where required by the implementation.
* **Pytest:** Automated testing of selected analytical functions.
* **Git:** Version control.
* **GitHub:** Repository hosting and sharing of the project.

The exact dependencies and version requirements should be checked in `requirements.txt`.

The project is designed to be executed locally without requiring access to proprietary clinical datasets.

---

## 12. Installation and Setup

### Prerequisites

Install a compatible Python version and Git.

Python 3.10 or later is a suggested starting point. Compatibility should be confirmed against the dependencies listed in `requirements.txt`.

### Step 1: Clone the repository

```bash
git clone https://github.com/Sumana08-creator/digital-mental-health-health-economics.git
```

Move into the project directory:

```bash
cd digital-mental-health-health-economics
```

### Step 2: Create a virtual environment

On Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### Step 3: Install dependencies

```bash
python -m pip install --upgrade pip
```

Then install the project requirements:

```bash
pip install -r requirements.txt
```

### Step 4: Run the analysis

From the project root, execute:

```bash
python run_analysis.py
```

The script is intended to run the project's analytical workflow and generate the corresponding outputs.

Check the terminal for any errors or execution messages.

### Step 5: Run the tests

```bash
python -m pytest -v
```

The tests help check selected aspects of the analytical implementation.

A passing test suite does not establish that the model is clinically valid, that its assumptions are appropriate for a real healthcare system, or that the results generalise beyond the synthetic dataset.

---

## 13. Reproducibility and Analytical Quality Assurance

Reproducibility is an important feature of health economics research.

Analytical results should be traceable to their source data, code, parameter assumptions, and execution procedures.

This project supports reproducibility through:

1. A structured repository layout.
2. A documented synthetic input dataset.
3. Centralised analytical functions.
4. A script for running the analysis.
5. Automated tests for selected functions.
6. Generated CSV outputs.
7. Version control through Git.
8. Documentation of methodological limitations.

### Current quality assurance approach

The project includes a dedicated test file:

`tests/test_health_economics.py`

The tests are intended to check selected behaviours of the implemented analytical functions.

For research applications, additional quality assurance would be appropriate, including:

* Independent verification of key calculations.
* Tests for missing and invalid values.
* Checks for zero or negative incremental effects.
* Validation of units and denominators.
* Reconciliation of summary results with underlying data.
* Review of cost and outcome definitions.
* Confirmation that generated outputs correspond to the current code.
* Documentation of any changes to model parameters.

The current tests should be interpreted as software checks rather than comprehensive statistical or clinical validation.

---

## 14. Limitations

This project is a methodological demonstration, not a completed health technology assessment or empirical economic evaluation.

Its principal limitations are outlined below.

### 14.1 Synthetic data

The dataset is simulated and does not represent actual patient-level observations.

Consequently, the results cannot establish real-world clinical effectiveness, health service utilisation, intervention costs, or cost-effectiveness.

### 14.2 Approximate QALY outcomes

The project uses approximate 12-month QALY outcomes to demonstrate economic calculations.

A full economic evaluation would require a clearly specified health-outcome measurement and valuation method, appropriate treatment of changes over time, and a justified approach to uncertainty and missing observations.

### 14.3 Illustrative economic assumptions

The cost inputs, implementation assumptions, cost offsets, and monetary value assigned to a QALY are illustrative.

They are not validated estimates of the costs or opportunity costs faced by a specific healthcare system.

### 14.4 Simplified budget impact model

The budget impact component demonstrates scenario-based calculations.

It does not constitute a setting-specific financial forecast and should not be used to estimate an actual healthcare organisation's future expenditure.

### 14.5 Descriptive equity analysis

The current equity component compares illustrative access groups.

It does not establish causal relationships or provide a comprehensive distributional cost-effectiveness analysis.

### 14.6 Limited uncertainty analysis

The current sensitivity analysis is deterministic and examines selected parameter variations.

It does not provide a complete probabilistic assessment of joint parameter uncertainty.

### 14.7 No independent empirical validation

The reported results have not been validated against clinical trial results, administrative healthcare records, published intervention evaluations, or an external benchmark.

For these reasons, the findings should be interpreted strictly as outputs from the specified synthetic modelling exercise.

---

## 15. Future Development Roadmap

The following enhancements could extend the project from a methodological demonstration towards a more comprehensive health economic evaluation framework.

These are proposed future developments and are not claimed to be implemented in the current repository.

### Phase 1: Strengthen analytical validation

* Expand automated unit tests.
* Verify key economic calculations independently.
* Add validation for missing, invalid, and implausible inputs.
* Document model parameters, units, and denominators.
* Add a clear data dictionary.
* Improve the traceability of generated outputs.

### Phase 2: Extend cost-effectiveness analysis

* Develop a more explicit health-outcome calculation framework.
* Document the intervention and comparator perspectives.
* Clarify the cost categories included in the analysis.
* Examine alternative analytical perspectives and time horizons where appropriate.
* Investigate alternative methods for handling missing data and uncertainty.

### Phase 3: Extend uncertainty analysis

* Implement probabilistic sensitivity analysis.
* Define suitable distributions for uncertain parameters.
* Generate simulated incremental cost and outcome pairs.
* Produce a cost-effectiveness plane.
* Produce a cost-effectiveness acceptability curve.
* Examine how uncertainty affects decision conclusions.

### Phase 4: Strengthen budget impact analysis

* Introduce more explicit population and uptake assumptions.
* Examine implementation over multiple periods.
* Distinguish recurring costs from upfront costs.
* Evaluate alternative adoption scenarios.
* Document the treatment of cost offsets.
* Add validation against independently calculated scenario totals.

### Phase 5: Develop equity-focused evaluation

* Establish an explicit equity framework.
* Define population groups using justified variables.
* Examine intervention reach and uptake across groups.
* Investigate the distribution of health benefits and costs.
* Explore appropriate distributional methods where the data support them.

### Phase 6: Prepare for real-world research applications

* Define a transparent data-management workflow.
* Document the provenance of every input.
* Use appropriate research governance and data-access arrangements.
* Apply methods consistent with the research question and available evidence.
* Validate the model using relevant empirical data.
* Document uncertainty and limitations before drawing policy conclusions.

Implementation of these enhancements would require additional development, testing, and methodological review.

---

## 16. Relevance to Health Economics Research

This portfolio demonstrates practical engagement with analytical tasks relevant to health economics and health services research.

### Economic evaluation

The project implements a simplified framework for calculating incremental costs, incremental health outcomes, and an ICER.

### Budget impact modelling

It demonstrates how assumptions about the eligible population, uptake, participant costs, implementation costs, and cost offsets can be incorporated into financial scenarios.

### Equity-focused analysis

It illustrates the organisation and comparison of descriptive outcomes across population groups.

### Quantitative analysis

It uses a structured data-analysis workflow to generate summary measures and tabular results.

### Reproducible research

It separates source data, analytical functions, execution scripts, tests, and generated outputs.

### Research transparency

It documents the synthetic nature of the data, the illustrative assumptions, the interpretation of results, and the limitations of the current model.

These capabilities provide a foundation for further development in applied health economics, health technology assessment, public health research, and economic evaluation.

They do not replace the need for appropriate research design, statistical expertise, methodological supervision, or validation against real-world evidence.

---

## 17. Relationship to the SAMPO Research Context

This portfolio was developed to demonstrate an interest in health economic evaluation and the practical application of quantitative methods to healthcare decision-making.

Its focus on cost-effectiveness, budget impact, equity, sensitivity analysis, and reproducibility provides a methodological starting point for learning about the types of analytical questions that arise in applied health economics research.

**This is an independent portfolio project, not an official SAMPO deliverable.**

The repository does not contain SAMPO trial data, confidential research material, or validated SAMPO results. No direct methodological or empirical conclusions about the SAMPO intervention should be inferred from this project.

Any future adaptation to a specific research study would require understanding the study protocol, research questions, available data, outcome measures, resource-use definitions, analytical plan, and applicable governance requirements.

The methods would then need to be reviewed and adapted to the actual study rather than transferred uncritically from this synthetic example.

---

## 18. Responsible Interpretation

The economic results in this repository should be interpreted within the assumptions and limitations of the synthetic model.

In particular:

* A low illustrative ICER is not evidence that a real intervention is cost-effective.
* A positive illustrative NMB is conditional on the specified model inputs and monetary threshold.
* A scenario-based budget impact is not an observed expenditure or validated forecast.
* Differences between synthetic access groups are not evidence of real-world health inequalities.
* Passing automated tests does not establish clinical or economic validity.
* Sensitivity analysis over selected assumptions does not quantify all relevant uncertainty.

The purpose of the project is to demonstrate analytical methods and reproducible implementation, not to make clinical, commissioning, or reimbursement recommendations.

---

## 19. Author and Project Information

**Author:** Sumana Shivaprakash

**Project:** Health Economic Evaluation Portfolio — Digital Mental Health Intervention

**Primary analytical focus:**

* Cost-effectiveness analysis.
* Budget impact analysis.
* QALY-based economic evaluation.
* Descriptive health equity assessment.
* Deterministic sensitivity analysis.
* Python-based quantitative analysis.
* Reproducible research workflows.

**Repository:** [digital-mental-health-health-economics](https://github.com/Sumana08-creator/digital-mental-health-health-economics)

This repository is intended for educational, portfolio, and methodological demonstration purposes.

---

## 20. Licence and Use

Refer to the repository's `LICENSE` file for the applicable licence terms.

The presence of a licence does not establish the validity of the economic model or the suitability of its outputs for real-world decision-making.

Users who adapt the project should review the code, understand the assumptions, validate the calculations, and establish the suitability of the methods for their intended application.

**Final note:** This project illustrates a reproducible approach to selected health economic analyses using synthetic data. Any application to clinical research or healthcare policy requires appropriate empirical evidence, methodological justification, validation, and interpretation within the relevant decision-making context.
