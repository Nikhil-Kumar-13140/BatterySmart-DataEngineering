from pathlib import Path
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from data_preprocessing import load_and_preprocess_data

# ======================================================
# Paths
# ======================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR.parent / "data" / "processed" / "ev_data_cleaned.csv"

MODEL_DIR = BASE_DIR / "models"

PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

# ======================================================
# Load Data
# ======================================================

X_train, X_test, y_train, y_test, preprocessor = load_and_preprocess_data(DATA_PATH)

# ======================================================
# Load Best Model
# ======================================================

model = joblib.load(MODEL_DIR / "best_model.pkl")

predictions = model.predict(X_test)

# ======================================================
# 1. Actual vs Predicted
# ======================================================

plt.figure(figsize=(8, 6))

plt.scatter(y_test, predictions, alpha=0.5)

plt.xlabel("Actual Electric Range")
plt.ylabel("Predicted Electric Range")
plt.title("Actual vs Predicted Electric Range")

plt.tight_layout()

plt.savefig(PLOTS_DIR / "actual_vs_predicted.png")

plt.close()

# ======================================================
# 2. Residual Plot
# ======================================================

residuals = y_test - predictions

plt.figure(figsize=(8, 6))

plt.scatter(predictions, residuals, alpha=0.5)

plt.axhline(y=0, color="red", linestyle="--")

plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residual Plot")

plt.tight_layout()

plt.savefig(PLOTS_DIR / "residual_plot.png")

plt.close()

# ======================================================
# 3. Feature Importance
# ======================================================

rf_model = model.named_steps["model"]

feature_names = model.named_steps[
    "preprocessor"
].get_feature_names_out()

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": rf_model.feature_importances_
})

importance_df = importance_df.sort_values(
    "Importance",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    importance_df["Feature"],
    importance_df["Importance"]
)

plt.gca().invert_yaxis()

plt.xlabel("Importance")
plt.title("Top 10 Feature Importances")

plt.tight_layout()

plt.savefig(PLOTS_DIR / "feature_importance.png")

plt.close()

# ======================================================
# 4. Model Comparison
# ======================================================

metrics_df = pd.read_csv(
    RESULTS_DIR / "model_metrics.csv"
)

plt.figure(figsize=(8, 5))

plt.bar(
    metrics_df["Model"],
    metrics_df["R2 Score"]
)

plt.ylabel("R² Score")
plt.title("Model Comparison (R² Score)")

plt.tight_layout()

plt.savefig(PLOTS_DIR / "model_comparison.png")

plt.close()

# ======================================================
# Metrics
# ======================================================

mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

print("=" * 50)
print("Random Forest Performance")
print("=" * 50)

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

print("\n✅ All plots generated successfully.")