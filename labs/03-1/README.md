# Lab 3.1 — Your First Flowgraph

Build a simulated complex tone and noise source in GNU Radio Companion 3.10. No SDR hardware is required.

Open `trusted_signal_alias.grc` in GNU Radio Companion to run the supplied graph. Start it, then stop it and change `tone_freq` to `600000` to repeat the test. To build it yourself, follow the steps below.

1. Create a QT GUI flowgraph. Set the `samp_rate` variable to `1e6`.
2. Add a **Signal Source**. Set Output Type to Complex, Sample Rate to `samp_rate`, Waveform to Cosine, Frequency to `100e3`, Amplitude to 1 and Offset to 0.
3. Add a **Noise Source**. Select Complex, Gaussian and amplitude 0.1. Connect the sources to the two ports of a complex **Add** block.
4. Connect Add to a complex **Throttle** with sample rate `samp_rate`, then connect Throttle to a complex **QT GUI Frequency Sink**. Set its FFT size to 1024, center frequency to 0 and bandwidth to `samp_rate`.
5. Run the graph and record the strongest peak. Stop, change the source frequency to `600e3`, rerun and record the new peak.

Expect peaks near +100 kHz and −400 kHz. The latter is the 600 kHz tone shifted by one sample rate into the displayed band. The exact peak cursor reading can vary by FFT bin. Throttle controls the simulated stream rate in the absence of a hardware clock.

Run `python verify_alias.py` for a numerical check. The Python check was run for this companion pack. The supplied flowgraph was compiled with GNU Radio Companion 3.10.12.0 and its Qt display ran in an offscreen Linux session. A probe on the same simulated stream measured +99.976 kHz and −400.024 kHz for the two settings.
