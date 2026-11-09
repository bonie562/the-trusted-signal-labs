"""Measure the two peaks from the companion flowgraph in a numerical check."""

import numpy as np

SAMPLE_RATE = 1_000_000
FFT_SIZE = 1024

rng = np.random.default_rng(3)
t = np.arange(FFT_SIZE) / SAMPLE_RATE
bins = np.fft.fftfreq(FFT_SIZE, 1 / SAMPLE_RATE)
for source in (100_000, 600_000):
    noise = 0.1 * (rng.standard_normal(FFT_SIZE) + 1j * rng.standard_normal(FFT_SIZE))
    signal = np.exp(2j * np.pi * source * t) + noise
    peak = bins[np.argmax(np.abs(np.fft.fft(signal * np.hanning(FFT_SIZE))))]
    target = (source + SAMPLE_RATE / 2) % SAMPLE_RATE - SAMPLE_RATE / 2
    assert abs(peak - target) <= SAMPLE_RATE / FFT_SIZE
    print(f"Source {source / 1000:.0f} kHz | FFT peak {peak / 1000:+.2f} kHz")
