import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load Dataset
df = pd.read_csv("diabetes_data.csv")

# Features
X = df[
    ["Glucose",
     "BloodPressure",
     "Age"]
]

# Target
y = df["Diabetes"]

# Train Model
model = LogisticRegression()

model.fit(X, y)

# Sample Patient
patient = [[140, 88, 42]]

prediction = model.predict(patient)

if prediction[0] == 1:
    print("⚠️ Diabetes Detected")
else:
    print("✅ No Diabetes")