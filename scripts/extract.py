import pandas as pd

file_path = "data/raw/Electric_Vehicle_Population_Data.csv"

ev_data = pd.read_csv(file_path)

print("First 5 Rows")
print(ev_data.head())

print("\nDataset Shape")
print(ev_data.shape)

print("\nColumn Names")
print(ev_data.columns)

print("\nDataset Information")
ev_data.info()

print("\nNull Values")
null_values = ev_data.isnull().sum()
print(null_values)