import numpy as np


FS = 1_000_000
N = 10_000
rng = np.random.default_rng(0)


def make_block(freq_hz, amp=1.0, noise=0.1):
    t = np.arange(N) / FS
    tone = amp * np.exp(2j * np.pi * freq_hz * t)
    return tone + noise * (rng.standard_normal(N) + 1j * rng.standard_normal(N))


def extract_features(x):
    p = np.abs(x) ** 2
    spec = np.abs(np.fft.fft(x * np.hanning(len(x)))) ** 2
    peak_khz = np.fft.fftfreq(len(x), 1 / FS)[np.argmax(spec)] / 1e3
    flatness = np.exp(np.mean(np.log(spec + 1e-20))) / np.mean(spec)
    return np.array([np.mean(p), np.var(p), peak_khz, flatness])


# 1. Learn "normal": a 100 kHz carrier with small drift and level changes.
normal = np.array([extract_features(make_block(rng.normal(100e3, 500),
                                                           amp=rng.uniform(0.9, 1.1)))
                         for _ in range(300)])
mu = normal.mean(axis=0)
inv_cov = np.linalg.pinv(np.cov(normal, rowvar=False))                # pinv: tolerates near-
def anomaly_score(features):
    d = features - mu
    return float(np.sqrt(d @ inv_cov @ d))


# 2. Score new observations.
cases = {
    "normal carrier":            make_block(100e3),
    "carrier moved to 300k": make_block(300e3),
    "noise floor raised":        make_block(100e3, noise=0.6),
}
for name, x in cases.items():
    print(f"{name:24s} score = {anomaly_score(extract_features(x)):8.1f}")
