import time
from collections import deque
from datetime import datetime, timezone
import numpy as np


FS = 1_000_000
BLOCK = 2048
WINDOW = 20
THRESHOLD = 4.0
rng = np.random.default_rng(2)


def acquire_block(k):
    t = np.arange(BLOCK) / FS
    gain = 2.5 if k == 150 else 1.0        # injected event
    x = gain * np.exp(2j * np.pi * 150_000 * t)
    return x + 0.05 * (rng.standard_normal(BLOCK) + 1j *
rng.standard_normal(BLOCK))


def mean_power(x):
    x = x - np.mean(x)      # DC removal
    return float(np.mean(np.abs(x) ** 2))


history = deque(maxlen=WINDOW)
latencies_ms = []
for k in range(300):
    t0 = time.perf_counter()
    value = mean_power(acquire_block(k))
    score = 0.0
    if len(history) == history.maxlen:
          score = abs(value - np.mean(history)) / (np.std(history) + 1e-9)
    history.append(value)
    latencies_ms.append((time.perf_counter() - t0) * 1e3)
    if score > THRESHOLD:
          print("EDGE ALERT", datetime.now(timezone.utc).isoformat(),
                {"block": k, "mean_power": round(value, 3), "score":
round(float(score), 1)})


lat = np.array(latencies_ms)
print(f"per-block latency: median {np.median(lat):.3f} ms, "
      f"p99 {np.percentile(lat, 99):.3f} ms, max {lat.max():.3f} ms")
