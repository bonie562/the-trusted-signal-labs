import numpy as np


f_sig = 50_000


for fs in (80_000, 500_000):
    t = np.arange(0, 0.001, 1 / fs)
    x = np.sin(2 * np.pi * f_sig * t)
    # Frequency that the samples appear to contain (folded into 0..fs/2)
    apparent = abs(f_sig - fs * round(f_sig / fs))
    print(f"fs = {fs:>7} Hz | Nyquist = {fs / 2:>7.0f} Hz | "
           f"apparent frequency = {apparent:>6.0f} Hz")
