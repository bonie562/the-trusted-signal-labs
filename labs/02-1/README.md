# Lab 2.1 — Budget a Receive Link

Estimate how much receiver bandwidth a weak signal can tolerate. This companion exercise follows Listing 2.1 of *The Trusted Signal*, second edition.

You need Python 3.10 or later. Allow about 15 minutes. The exercise uses the Python standard library and a receiver noise model, so it runs without SDR hardware or captured data.

## 1. Run the baseline

Open a terminal in the extracted lab folder. On Windows, run:

```powershell
py receive_link_budget.py
```

On macOS or Linux, use `python3` in place of `py`.

Record the estimated noise floor and minimum signal at all four bandwidths. The final column adds the 10 dB signal-to-noise ratio (SNR) required for this exercise.

## 2. Change the receiver noise figure

```powershell
py receive_link_budget.py --noise-figure-db 3
py receive_link_budget.py --noise-figure-db 12
```

Compare the 2 MHz row across all three runs. Explain how each change in receiver noise figure affects the minimum signal.

## 3. Choose a bandwidth

Using the 6 dB noise-figure run, find the widest modeled bandwidth at which a −100 dBm signal still meets the 10 dB SNR requirement. Then identify the widest of the four listed bandwidths that qualifies.

## Check your result

| Noise figure | Estimated noise floor at 2 MHz |
| --- | --- |
| 3 dB | −108.0 dBm |
| 6 dB | −105.0 dBm |
| 12 dB | −99.0 dBm |

The widest modeled bandwidth is about 631 kHz. Of the four listed settings, 200 kHz is the widest one that qualifies. These values come from the exercise’s receiver noise model. A physical receiver can also be affected by interference, front-end loss, and its actual noise figure.
