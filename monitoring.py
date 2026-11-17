
import numpy as np
from sklearn.ensemble import IsolationForest

# Server CPU and Memory usage
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

model = IsolationForest(contamination=0.25, random_state=42)
model.fit(data)

results = model.predict(data)

print("AI DevOps Monitoring Report")

for i, result in enumerate(results):
    status = "ANOMALY" if result == -1 else "NORMAL"
    print(f"Server {i+1}: CPU={data[i][0]}%, Memory={data[i][1]}% - {status}")
