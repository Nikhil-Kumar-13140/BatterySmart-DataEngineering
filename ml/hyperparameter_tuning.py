from pathlib import Path
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from data_preprocessing import load_and_preprocess_data

# ======================================================
# Paths
# ======================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR.parent / "data" / "processed" / "ev_data_cleaned.csv"

MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

# ======================================================
# Load Data
# ======================================================

X_train, X_test, y_train, y_test, preprocessor = load_and_preprocess_data(DATA_PATH)

# ======================================================
# Pipeline
# ======================================================

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(random_state=42))
])

# ======================================================
# Parameters
# ======================================================

param_grid = {
    "model__n_estimators": [100, 200, 300],
    "model__max_depth": [10, 20, 30, None],
    "model__min_samples_split": [2, 5, 10],
    "model__min_samples_leaf": [1, 2, 4]
}

search = RandomizedSearchCV(
    pipeline,
    param_distributions=param_grid,
    n_iter=10,
    cv=5,
    scoring="r2",
    random_state=42,
    n_jobs=-1
)

print("Training tuned Random Forest...")

search.fit(X_train, y_train)

print("\nBest Parameters:")
print(search.best_params_)

print("\nBest CV Score:")
print(round(search.best_score_, 4))

joblib.dump(
    search.best_estimator_,
    MODEL_DIR / "best_random_forest.pkl"
)

print("\n✅ Tuned model saved successfully.")