import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = {
    'Month':[1,2,3,4,5,6],
    'Passengers':[1000,1200,1400,1500,1700,1900]
}

df = pd.DataFrame(data)

X = df[['Month']]
y = df['Passengers']

model = LinearRegression()

model.fit(X,y)

# joblib.dump(
#     model,
#     'dashboard/ml_models/passenger_model.pkl'
# )

print("Forecast Model Saved")