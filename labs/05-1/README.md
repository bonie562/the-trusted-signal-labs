# Lab 5.1 — Aliasing and Spectral Leakage

1. Run `python aliasing.py`. The 50 kHz tone appears at 30 kHz for an 80 kHz sample rate and at 50 kHz for 500 kHz. Change `f_sig` to 120000 and the first sample rate to 200000. Predict the resulting frequency, then rerun.
2. Run `python leakage.py` and open `leakage.png`. Change the first tone from 100000 to 100500 Hz, rerun, and compare the two window curves. Record the effect on distant sidelobes and main-lobe width.

The modified alias is 80 kHz. For the off-bin tone the Hann window spreads the main lobe over more bins and reduces distant sidelobes.
