from collections import deque
import numpy as np


WINDOW = 50
SIGMA = 4.0
history = deque(maxlen=WINDOW)


def compute_alert(value):
    """Return (alert, z-score) relative to the recent baseline."""
    if len(history) < WINDOW:
         history.append(value)
         return False, 0.0
    mean, std = np.mean(history), np.std(history) + 1e-9
    z = abs(value - mean) / std
    history.append(value)
    return z > SIGMA, float(z)


rng = np.random.default_rng(8)
stream = rng.normal(1.0, 0.05, 200)
stream[150] = 1.8       # inject one outlier
for i, v in enumerate(stream):
    alert, z = compute_alert(v)
    if alert:
         print(f"sample {i}: value={v:.2f} z={z:.1f} -> ALERT")
