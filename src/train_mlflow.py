from pathlib import Path
import json
import joblib
import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

ROOT = Path(__file__).resolve().parents[1]

def run_training_with_mlflow():
    print("Starting MLflow experiment tracking...")
    X_train = np.load(ROOT / "data/processed/X_train_final.npy")
    y_train = np.load(ROOT / "data/processed/y_train.npy")
    X_test = np.load(ROOT / "data/processed/X_test_final.npy")
    y_test = np.load(ROOT / "data/processed/y_test.npy")
    tracking_db = ROOT / "mlflow.db"
    mlflow.set_tracking_uri("sqlite:///" + tracking_db.as_posix())
    mlflow.set_experiment("Telco-Churn-Prediction")
    params = {"n_estimators": 100, "max_depth": 10, "random_state": 42, "class_weight": "balanced"}
    with mlflow.start_run(run_name="random_forest_baseline") as run:
        model = RandomForestClassifier(**params, n_jobs=-1)
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        prob = model.predict_proba(X_test)[:, 1]
        metrics = {
            "accuracy": accuracy_score(y_test, pred),
            "precision": precision_score(y_test, pred, zero_division=0),
            "recall": recall_score(y_test, pred, zero_division=0),
            "f1_score": f1_score(y_test, pred, zero_division=0),
            "roc_auc": roc_auc_score(y_test, prob),
        }
        mlflow.log_params(params)
        mlflow.log_metrics(metrics)
        mlflow.log_artifact(str(ROOT / "data/processed/dataset_metadata.json"))
        mlflow.sklearn.log_model(
        sk_model=model,
        name="model",
        skops_trusted_types=["sklearn.tree._tree.Tree"]
)
        joblib.dump(model, ROOT / "models/random_forest_mlflow.pkl")
        with open(ROOT / "outputs/mlflow_run.json", "w", encoding="utf-8") as f:
            json.dump({"run_id": run.info.run_id, "metrics": metrics}, f, indent=4)
        print("Run ID:", run.info.run_id)
        print("Metrics:", {k: round(v, 4) for k, v in metrics.items()})

if __name__ == "__main__":
    run_training_with_mlflow()
