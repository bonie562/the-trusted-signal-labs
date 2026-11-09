# Lab 5.2 — Chirps, Windows, and FM

1. Run `python chirp.py`. Record the first and last frequency-ridge estimates. Change `WINDOW` to 128 and rerun. Overlap follows the window size automatically. Compare the change in time and frequency resolution.
2. Run `python fm.py`, then change `deviation` from 25000 to 5000 and rerun. Record the recovered signal correlation for both values.

A shorter window improves time localization and widens frequency bins. The clean FM simulation recovers the original message with a correlation near 1.000 at both settings.
