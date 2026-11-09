import numpy as np


fs = 1_000_000
N = 5000
t = np.arange(N) / fs
x = np.exp(2j * np.pi * 100_000 * t) + 0.5 * np.exp(2j * np.pi * 250_000 * t)


freqs = np.fft.fftshift(np.fft.fftfreq(N, d=1 / fs))


mag_rect = np.abs(np.fft.fftshift(np.fft.fft(x)))          # no window
mag_hann = np.abs(np.fft.fftshift(np.fft.fft(x * np.hanning(N))))            # Hann window


print("strongest component (Hz):", freqs[np.argmax(mag_hann)])
print("bin spacing (Hz):", fs / N)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))
for label, magnitude in (("Rectangular", mag_rect), ("Hann", mag_hann)):
    relative_db = 20 * np.log10(np.maximum(magnitude / magnitude.max(), 1e-6))
    plt.plot(freqs / 1000, relative_db, label=label)
plt.xlim(95, 106)
plt.ylim(-110, 5)
plt.xlabel("Frequency (kHz)")
plt.ylabel("Magnitude (dB relative to peak)")
plt.legend()
plt.tight_layout()
plt.savefig("leakage.png", dpi=150)
