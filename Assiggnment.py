# Anomaly-Based Fraud Detection using Linear Regression Residuals.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

file_name = "new_transaction_data.csv"
print(f"Loading dataset from {file_name}...")
df = pd.read_csv(file_name)

# Extract underlying numpy arrays for significantly faster processing
y = df["Amount"].values  # y is the actual amount

# x is the 30 other variables\features associated with that transiction.
X = df.drop(columns=["Amount", "Actual_Label"], errors="ignore").values

# 2. Training and Predicting
print("Training Linear Regression...")
regression_model = LinearRegression().fit(X, y)
# Predict directly into a numpy array
preds = regression_model.predict(X)
# Calculate the Residual Error using vectorized numpy subtraction
residuals = np.abs(y - preds)

# 3. Anomaly Detection (Boolean Masking)
print("Flagging anomalies based on regression errors...")
# Find the threshold error that separates the top 1% worst predictions
threshold_error = np.percentile(residuals, 99)
# Create a boolean mask (True for anomaly, False for normal)
is_anomaly = residuals > threshold_error
print(f"Total Transactions: {len(y)}")
print(f"Detected Anomalies: {is_anomaly.sum()}")

# 4. Visualization
print("Rendering plot...")
plt.figure(figsize=(8, 5))
# Plot normal transactions by inverting the mask (~is_anomaly)
plt.scatter(
    preds[~is_anomaly],
    y[~is_anomaly],
    color="steelblue",
    alpha=0.4,
    label="Normal Transactions",
    s=25,)
# Plot detected anomalies using the mask
plt.scatter(
    preds[is_anomaly],
    y[is_anomaly],
    color="crimson",
    edgecolors="black",
    label="Detected Fraud (Anomalies)",
    s=75,)
# Draw a perfect prediction line (y=x) for reference
max_val = np.maximum(preds.max(), y.max())
plt.plot(
    [0, max_val],
    [0, max_val],
    color="black",
    linestyle="--",
    alpha=0.5,
    label="Perfect Prediction Line",)

plt.title("Fraud Detection", fontsize=14)
plt.xlabel("Predicted Transaction Amount ($)")
plt.ylabel("Actual Transaction Amount ($)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()  # Ensures labels don't get cut off
plt.show()
