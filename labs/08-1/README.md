# Lab 8.1 — Tune an Adaptive Alert

Run `python adaptive_alert.py` with the default `SIGMA = 4`. Repeat with thresholds 2 and 6. Record whether the alert at sample 150 is retained and count any other alerts. To add slow drift, insert `stream += 0.002 * np.arange(stream.size)` after the outlier assignment, then run again and compare.

The baseline learns from recent observations. A drifting signal can move the baseline without creating a single large deviation.
