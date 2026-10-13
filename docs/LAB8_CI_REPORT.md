# Lab 8: Continuous integration report

## Workflow

`.github/workflows/lab8_ci.yml` runs the end-to-end MLOps pipeline on matching
pushes and pull requests, and can also be started manually with
`workflow_dispatch`.

The workflow checks out the repository, installs the declared dependencies,
runs `src/mlops_pipeline/churn_prediction_pipeline.py`, and uploads available
artifacts and reports even when a run fails. A pipeline-stage failure returns
a non-zero exit code and fails the Actions job.

## Local verification

The same pipeline can be run locally from the repository root:

```powershell
python src/mlops_pipeline/churn_prediction_pipeline.py
```

Confirm that the run log reports `"overall_status": "PASSED"` and that each
stage has a zero exit code. Model evaluation metrics are saved in
`reports/model_evaluation_report.json`; the configured quality threshold is
checked by the quality-gate stage.

The workflow uses the tracking URI in `config.yaml` by default. A repository
secret named `MLFLOW_TRACKING_URI` can override it when a shared tracking
server is intentionally configured.
