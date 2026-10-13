# MLflow setup for local runs and GitHub Actions

## Local tracking

The default `mlflow.tracking_uri` in `config.yaml` uses the local SQLite
database `mlflow.db`. From the repository root, run the pipeline and inspect
experiments with:

```powershell
python src/mlops_pipeline/churn_prediction_pipeline.py
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Open the MLflow UI at `http://127.0.0.1:5000`. The database, run artifacts,
and registered models are local state and should not be committed.

## GitHub Actions

The CI workflows use the configured local SQLite tracking store by default;
no MLflow credential is needed for that mode. To use a shared tracking server,
add a repository Actions secret named `MLFLOW_TRACKING_URI` and ensure the
runner can reach and authenticate to that server. The training scripts use
this environment variable as an override to the configured URI.

The tracking server and artifact store must support model registration for
the registry and lifecycle stages. Keep credentials in Actions secrets, not
in `config.yaml` or workflow source.

## Troubleshooting

- Check the failing stage in `logs/churn_prediction_pipeline_run_log.json`.
- Verify the tracking URI and that the tracking backend is reachable.
- Confirm the configured model name and that a Production version exists
  before running the Lab 9 model-recovery scenario.
- Download CI reports from the workflow run's Artifacts section.
