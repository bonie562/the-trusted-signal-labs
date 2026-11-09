import numpy as np
from scipy.signal import stft


WINDOW = 1024
fs = 1_000_000
T = 0.01
t = np.arange(0, T, 1 / fs)


f0, f1 = 100_000, 300_000       # sweep from 100 kHz to 300 kHz
k = (f1 - f0) / T       # sweep rate (Hz per second)
phase = 2 * np.pi * (f0 * t + 0.5 * k * t**2)          # integral of f(t), not f(t) * t
x = np.exp(1j * phase)


f, tt, Z = stft(x, fs=fs, nperseg=WINDOW, noverlap=WINDOW // 2, return_onesided=False)
f, Z = np.fft.fftshift(f), np.fft.fftshift(Z, axes=0)


ridge = f[np.argmax(np.abs(Z), axis=0)]         # strongest frequency in each frame
print(f"ridge starts near {ridge[0]:.0f} Hz and ends near {ridge[-1]:.0f} Hz")
