# Lab 7: End-to-end MLOps pipeline

## Goal

Run the churn model workflow as an ordered pipeline with explicit checks,
artifacts, and a status log for every stage.

## Run

From the repository root, install the packages in `requirements.txt` and run:

```powershell
python src/mlops_pipeline/churn_prediction_pipeline.py
```

## Stages

The runner executes the following scripts in order and halts at the first
non-zero exit code:

1. Load the raw Telco churn dataset.
2. Validate the raw schema and values.
3. Split the data and fit preprocessing on the training split.
4. Validate the processed train/test outputs.
5. Train a Random Forest, log its metrics to MLflow, and register the model.
6. Evaluate on the held-out test split.
7. Apply the configured F1 quality gate.
8. Compare eligible registered versions and promote or archive them.
9. Load the Production model and write sample inference predictions.

## Outputs

The run log is written to `logs/churn_prediction_pipeline_run_log.json`.
Evaluation and quality-gate reports are written under `reports/`, model and
preprocessor artifacts under `models/` and `artifacts/`, and inference output
to `outputs/inference_predictions.csv`. These are generated run products;
the project Git workflow generally keeps them out of commits.

The pipeline uses `config.yaml` for the input paths, model parameters, MLflow
tracking URI, quality threshold, and artifact locations.
