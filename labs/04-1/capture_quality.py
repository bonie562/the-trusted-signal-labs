import numpy as np


def check_capture(samples, fs, full_scale=1.0):
    """Return a dictionary of acquisition-quality indicators for complex
samples."""
    x = np.asarray(samples)
    i, q = x.real, x.imag
    clip = float(np.mean((np.abs(i) > 0.98 * full_scale) |
                             (np.abs(q) > 0.98 * full_scale)))
    dc = complex(np.mean(x))
    # Image-rejection proxy: power ratio of I and Q and their correlation
    pi, pq = np.mean(i**2), np.mean(q**2)
    gain_imb_db = 10 * np.log10(pi / pq)
    phase_corr = float(np.mean(i * q) / np.sqrt(pi * pq))
    # Noise-floor estimate: median PSD bin (robust to a few strong carriers)
    n = 4096
    segs = x[: len(x) // n * n].reshape(-1, n) * np.hanning(n)
    spec = np.abs(np.fft.fft(segs, axis=1)) ** 2
    psd = np.mean(spec, axis=0) / (fs * np.sum(np.hanning(n) ** 2))
    floor_db = 10 * np.log10(np.median(psd))
    return {
         "clipping_fraction": clip,
         "dc_offset_magnitude": abs(dc),
         "iq_gain_imbalance_db": float(gain_imb_db),
         "iq_correlation": phase_corr,
         "noise_floor_dbfs_per_hz": float(floor_db),
         "mean_power": float(np.mean(np.abs(x) ** 2)),
    }


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    fs, n = 2e6, 400_000
    t = np.arange(n) / fs
    noise = 0.02 * (rng.standard_normal(n) + 1j * rng.standard_normal(n))
    x = 0.3 * np.exp(2j * np.pi * 250e3 * t) + noise
    x = x + (0.01 + 0.005j)     # injected DC offset
    for k, v in check_capture(x, fs).items():
         print(f"{k:32s} {v:.5g}")
