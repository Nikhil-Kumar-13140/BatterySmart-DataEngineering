from pathlib import Path
import joblib
import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from data_preprocessing import load_and_preprocess_data

# ======================================================
# Paths
# ======================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR.parent / "data" / "processed" / "ev_data_cleaned.csv"

MODEL_DIR = BASE_DIR / "models"

RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

# ======================================================
# Load Data
# ======================================================

X_train, X_test, y_train, y_test, preprocessor = load_and_preprocess_data(DATA_PATH)

# ======================================================
# Models to Evaluate
# ======================================================

model_files = {
    "Linear Regression": "linear_regression.pkl",
    "Decision Tree": "decision_tree.pkl",
    "Random Forest": "random_forest.pkl"
}

results = []

print("=" * 60)
print("Evaluating Models")
print("=" * 60)

for model_name, model_file in model_files.items():

    model = joblib.load(MODEL_DIR / model_file)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)

    results.append({
        "Model": model_name,
        "MAE": round(mae, 2),
        "RMSE": round(rmse, 2),
        "R2 Score": round(r2, 4)
    })

results_df = pd.DataFrame(results)

results_df.to_csv(
    RESULTS_DIR / "model_metrics.csv",
    index=False
)

print(results_df)

print("\n✅ Results saved successfully.")