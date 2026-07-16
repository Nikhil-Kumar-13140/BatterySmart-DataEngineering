from pathlib import Path

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def load_and_preprocess_data(file_path):
    """
    Load the dataset and prepare it for model training.
    """

    df = pd.read_csv(file_path)

    # Drop unnecessary columns
    columns_to_drop = [
        "VIN (1-10)",
        "DOL Vehicle ID",
        "Vehicle Location",
        "Electric Utility",
        "2020 Census Tract",
        "Postal Code",
        "Base MSRP"
    ]

    df = df.drop(columns=columns_to_drop)

    # Remove missing values
    df = df.dropna()

    # Separate target
    X = df.drop("Electric Range", axis=1)
    y = df["Electric Range"]

    # Identify categorical columns
    categorical_columns = X.select_dtypes(include=["object"]).columns.tolist()

    # Build preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_columns
            )
        ],
        remainder="passthrough"
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        preprocessor
    )