from pathlib import Path
import joblib

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from data_preprocessing import load_and_preprocess_data

# ======================================================
# Project Paths
# ======================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR.parent / "data" / "processed" / "ev_data_cleaned.csv"

MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

# ======================================================
# Load Dataset
# ======================================================

X_train, X_test, y_train, y_test, preprocessor = load_and_preprocess_data(DATA_PATH)

# ======================================================
# Define Models
# ======================================================

models = {
    "Linear Regression": LinearRegression(),

    "Decision Tree": DecisionTreeRegressor(
        random_state=42
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )
}

trained_models = {}

# ======================================================
# Train Models
# ======================================================

print("=" * 50)
print("Training Models...")
print("=" * 50)

for model_name, model in models.items():

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    pipeline.fit(X_train, y_train)

    trained_models[model_name] = pipeline

    print(f"✅ {model_name} trained successfully.")

# ======================================================
# Save All Models
# ======================================================

print("\nSaving models...")

for model_name, trained_model in trained_models.items():

    file_name = model_name.lower().replace(" ", "_") + ".pkl"

    joblib.dump(
        trained_model,
        MODEL_DIR / file_name
    )

print("✅ Individual models saved.")

# ======================================================
# Save Best Model
# ======================================================

best_model = trained_models["Random Forest"]

joblib.dump(
    best_model,
    MODEL_DIR / "best_model.pkl"
)

print("🏆 Best model saved successfully.")

print("\nProject completed successfully.")