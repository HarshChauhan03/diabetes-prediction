import pandas as pd

# Sample Diabetes Dataset

data = {
    "Glucose": [120, 150, 95, 180, 130],
    "BloodPressure": [80, 90, 70, 95, 85],
    "Age": [25, 45, 30, 55, 40],
    "Diabetes": [0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

print(df)

df.to_csv(
    "diabetes_data.csv",
    index=False
)

print("Dataset Saved Successfully")