# Lab 7.1 — Measure Your Own Latency

Run `python latency.py` three times. Record the median, 99th percentile and maximum. Repeat while another process is using CPU. Compare the tail with the baseline. For the stretch exercise change `BLOCK` to 8192 and compare latency per sample.

The injected event is block 150. Timing depends on the machine and current load. The script measures processing of simulated blocks.
