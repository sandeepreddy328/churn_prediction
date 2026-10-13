# Lab 9: Failure handling and recovery

## Purpose

The Lab 9 runner injects controlled faults to check that invalid inputs stop
the pipeline and that a missing local model can be recovered from the MLflow
Production registry.

## Run

First run the normal pipeline to create the processed data and register a
Production model. Then run:

```powershell
python src/mlops_pipeline/10_failure_injection.py
```

The repetition count is configured by `lab9.repetitions` in `config.yaml`.
Results are written to `reports/failure_report.json`.

## Scenarios

1. Rename the raw dataset temporarily; validation must fail.
2. Replace a numeric value with invalid text; schema validation must fail.
3. Remove a required column; schema validation must fail.
4. Inject a `NaN` into processed training features; output validation must fail.
5. Remove the local model; evaluation must fail, after which the runner
   downloads the Production model from MLflow and evaluation must pass.

Each fault-injection scenario restores its original input or model in a
`finally` block. Run the test only when no other process is using the same
working files. A scenario that cannot be tested or recovered causes a non-zero
exit status.

## CI

`.github/workflows/lab9_failure_tests.yml` first runs the normal pipeline,
then the failure/recovery runner. It uploads the Lab 9 report and pipeline log
as workflow artifacts for inspection.
