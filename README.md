# The Trusted Signal — Second Edition lab companion

Companion files for *The Trusted Signal* by Gavin M. Olivares. Start with Lab 2.1 or open the folder that matches your chapter.

| Lab | Exercise |
| --- | --- |
| [2.1](labs/02-1/) | Budget a Receive Link |
| [3.1](labs/03-1/) | Your First Flowgraph |
| [4.1](labs/04-1/) | Quality-Check a Capture |
| [5.1](labs/05-1/) | Aliasing and Spectral Leakage |
| [5.2](labs/05-2/) | Chirps, Windows, and FM |
| [6.1](labs/06-1/) | Evaluate a Detector Honestly |
| [7.1](labs/07-1/) | Measure Your Own Latency |
| [8.1](labs/08-1/) | Tune an Adaptive Alert |

Download the repository with **Code → Download ZIP** and extract it. Use Python 3.10 or later. Run the following from the extracted folder to install dependencies for Labs 3.1–8.1:

```text
python -m pip install -r requirements.txt
```

On Windows use `py` if `python` is unavailable. On macOS or Linux use `python3` if needed. Open each lab's README before running its files. Lab 2.1 requires only the standard library. Lab 3.1 also has a GNU Radio Companion exercise. All supplied Python examples use synthetic signals or data.
