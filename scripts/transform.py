import pandas as pd

# Read the raw dataset
file_path = "data/raw/Electric_Vehicle_Population_Data.csv"
ev_data = pd.read_csv(file_path)

print("Original Shape:", ev_data.shape)

# Check missing values
print("\nMissing Values:")
print(ev_data.isnull().sum())

# Drop Legislative District column
ev_data = ev_data.drop(columns=["Legislative District"])

# Fill missing numerical values with the median
ev_data["Electric Range"] = ev_data["Electric Range"].fillna(
    ev_data["Electric Range"].median()
)

ev_data["Base MSRP"] = ev_data["Base MSRP"].fillna(
    ev_data["Base MSRP"].median()
)

# Remove rows with missing values in remaining columns
ev_data = ev_data.dropna()

print("\nShape After Cleaning:", ev_data.shape)

print("\nMissing Values After Cleaning:")
print(ev_data.isnull().sum())

# Save cleaned data
output_path = "data/processed/ev_data_cleaned.csv"

ev_data.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print(output_path)