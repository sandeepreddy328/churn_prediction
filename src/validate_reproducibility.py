from pathlib import Path
import hashlib
import joblib
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
def main():
    X_test = np.load(ROOT / "data/processed/X_test_final.npy")
    model = joblib.load(ROOT / "models/random_forest_mlflow.pkl")
    pred = model.predict(X_test)
    digest = hashlib.sha256(pred.tobytes()).hexdigest()
    print("Reproducibility check completed.")
    print("Prediction SHA-256:", digest)
    print("Prediction count:", len(pred))
if __name__ == "__main__":
    main()
