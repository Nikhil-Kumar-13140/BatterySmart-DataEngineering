from pathlib import Path
import pandas as pd
import joblib
import streamlit as st

# ===================================
# Page Configuration
# ===================================

st.set_page_config(
    page_title="Battery Smart EV Predictor",
    page_icon="⚡",
    layout="wide"
)

# ===================================
# Title
# ===================================

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric("Dataset", "134K+")

kpi2.metric("Features", "16")

kpi3.metric("Best R²", "0.9974")

kpi4.metric("ML Model", "Random Forest")

st.title("⚡ Battery Smart EV Analytics Platform")

st.markdown("""
### End-to-End Data Engineering • Machine Learning • Power BI

Predict the electric driving range of Electric Vehicles using a
Random Forest Machine Learning model trained on the
Electric Vehicle Population Dataset.

---
""")

st.markdown("---")

# ===================================
# Load Dataset
# ===================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "ev_data_cleaned.csv"

df = pd.read_csv(DATA_PATH)

MODEL_PATH = BASE_DIR / "ml" / "models" / "ev_range_predictor.pkl"

ml_model = joblib.load(MODEL_PATH)

# ===================================
# Sidebar
# ===================================

st.sidebar.title("⚡ About Project")

st.sidebar.markdown("""
### Battery Smart EV Analytics

This application demonstrates an end-to-end Data Engineering and Machine Learning workflow.

### Technologies

- Python
- Pandas
- MySQL
- Power BI
- Scikit-learn
- Streamlit
- Git & GitHub

### Model

Random Forest Regressor

R² Score: **0.9974**

### Developer

**Nikhil Kumar**

B.Tech CSE
""")

# ===================================
# Input Section
# ===================================

col1, col2 = st.columns(2)

with col1:

    county = st.selectbox(
        "County",
        sorted(df["County"].dropna().unique())
    )

    city = st.selectbox(
        "City",
        sorted(df["City"].dropna().unique())
    )

    state = st.selectbox(
        "State",
        sorted(df["State"].dropna().unique())
    )

    model_year = st.selectbox(
        "Model Year",
        sorted(df["Model Year"].unique(), reverse=True)
    )

with col2:

    make = st.selectbox(
        "Manufacturer",
        sorted(df["Make"].dropna().unique())
    )

    model = st.selectbox(
        "Model",
        sorted(df["Model"].dropna().unique())
    )

    vehicle_type = st.selectbox(
        "Vehicle Type",
        sorted(df["Electric Vehicle Type"].dropna().unique())
    )

    cafv = st.selectbox(
        "CAFV Eligibility",
        sorted(df["Clean Alternative Fuel Vehicle (CAFV) Eligibility"].dropna().unique())
    )

st.markdown("---")

predict = st.button(
    "🚗 Predict Electric Range",
    use_container_width=True
)

if predict:

    input_df = pd.DataFrame({

        "VIN (1-10)": ["Unknown"],

        "County": [county],

        "City": [city],

        "State": [state],

        "Postal Code": [0],

        "Model Year": [model_year],

        "Make": [make],

        "Model": [model],

        "Electric Vehicle Type": [vehicle_type],

        "Clean Alternative Fuel Vehicle (CAFV) Eligibility": [cafv],

        "Base MSRP": [0],

        "DOL Vehicle ID": [0],

        "Vehicle Location": ["Unknown"],

        "Electric Utility": ["Unknown"],

        "2020 Census Tract": [0]

    })

    prediction = ml_model.predict(input_df)

    st.success("Prediction Completed Successfully!")

    st.markdown("## 🚗 Estimated Electric Range")

    st.metric(
    label="Predicted Range",
    value=f"{prediction[0]:.2f} Miles"
    )

    st.info(
    "This prediction is generated using the tuned Random Forest model."
    )

st.markdown("---")

st.caption(
    "Developed by Nikhil Kumar • Battery Smart EV Analytics Platform • 2026"
)