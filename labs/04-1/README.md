# Lab 4.1 — Quality-Check a Capture

Run `python capture_quality.py` for the simulated baseline. Record the six indicators. For the next run add `x = 4 * x` just before the loop printing the indicators. Look for a nonzero clipping fraction. Then replace the gain change with `x = x + 0.1` and compare the DC offset with the baseline. The clipping indicator counts samples close to or beyond the assumed component full scale.

Optional hardware path. Load a compatible authorized capture and call `check_capture(samples, fs)` with the capture's recorded sample rate and correctly normalized I/Q samples. The supplied script simulates the input.
