
import numpy as np
from sklearn.ensemble import IsolationForest

# Sample server performance data
data = np.array([
    [20, 30],
    [25, 35],
    [22, 32],
    [28, 40],
    [90, 95],
    [24, 34],
    [85, 90],
    [26, 36]
])

# AI anomaly detection model
model = IsolationForest(contamination=0.25, random_state=42)
model.fit(data)

predictions = model.predict(data)

print("AI-Powered DevOps Monitoring Report")

for i, result in enumerate(predictions):
    if result == -1:
        print(f"Alert: Unusual server activity detected: {data[i]}")
    else:
        print(f"Normal server activity: {data[i]}")
