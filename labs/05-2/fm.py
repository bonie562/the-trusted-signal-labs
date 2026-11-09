import numpy as np


fs = 1_000_000
t = np.arange(0, 0.01, 1 / fs)


message = np.sin(2 * np.pi * 2_000 * t)
deviation = 25_000       # peak deviation (Hz)
phase = 2 * np.pi * deviation * np.cumsum(message) / fs                # integral of the message
fm = np.exp(1j * phase)         # complex FM baseband


# Instantaneous frequency from the angle between consecutive samples.
inst_hz = np.angle(fm[1:] * np.conj(fm[:-1])) * fs / (2 * np.pi)
recovered = inst_hz / deviation


r = np.corrcoef(recovered, message[1:])[0, 1]
print(f"correlation with the original message: {r:.3f}")
