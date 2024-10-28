# main.py
from simple_ml.linear_model import LinearRegression
from simple_ml.preprocessing import StandardScaler

# Sample data
X = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Initialize and use the scaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("Scaled X:", X_scaled)

# Initialize and use linear regression
model = LinearRegression()
model.fit(X_scaled, y)
predictions = model.predict(X_scaled)
print("Predictions:", predictions)
