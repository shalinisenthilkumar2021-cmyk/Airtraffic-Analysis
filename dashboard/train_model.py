import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("data/flights.csv")

X = df[["Passengers"]]
y = df["Delay_Minutes"]

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(
    model,
    "dashboard/ml_models/delay_model.pkl"
)

print("Model Saved Successfully")