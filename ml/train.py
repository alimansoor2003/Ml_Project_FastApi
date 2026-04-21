import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# You can replace this with ANY dataset (Kaggle, CSV, etc.)
# Just make sure columns match
data = pd.DataFrame({
    "area": [50, 60, 80, 100, 120],
    "bedrooms": [1, 2, 2, 3, 3],
    "price": [100000, 150000, 200000, 250000, 300000]
})

X = data[["area", "bedrooms"]]
y = data["price"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "ml/model.pkl")

print("Model trained and saved!")