# Churn Prediction MLOps Project

This repository contains a reproducible churn-classification workflow, MLflow
tracking and model registration, a quality gate, production inference, CI, and
failure/recovery checks.

## Setup

Run commands from the repository root. Create and activate a virtual
environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On macOS or Linux, activate it with `source .venv/bin/activate`.

## Run the complete MLOps pipeline

```powershell
python src/mlops_pipeline/churn_prediction_pipeline.py
```

The pipeline loads and validates the raw data, preprocesses it, trains and
registers a model, evaluates it, enforces the configured F1 quality gate,
promotes the best eligible model, and writes inference predictions.

Key generated outputs include:

- `logs/churn_prediction_pipeline_run_log.json`
- `reports/model_evaluation_report.json`
- `reports/quality_gate_report.json`
- `outputs/inference_predictions.csv`

Run the Lab 9 failure and recovery scenarios after the normal pipeline has
completed:

```powershell
python src/mlops_pipeline/10_failure_injection.py
```

The scenarios temporarily corrupt or remove inputs/artifacts and restore them
after each test. Do not run them while another process is using the same data
or model files.

## Labs and CI

The individual lab entry points are in `pipelines/`. GitHub Actions workflows
run the regular MLOps pipeline and the Lab 9 failure/recovery checks on pushes
and pull requests. See `docs/` for the pipeline, CI, failure-handling, and
MLflow setup notes.

To inspect local MLflow runs, start the UI with:

```powershell
mlflow ui --backend-store-uri sqlite:///mlflow.db
```
