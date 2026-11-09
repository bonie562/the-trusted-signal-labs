# Lab 6.1 — Evaluate a Detector Honestly

1. Run `python distance.py` and compare the three scores. Add a fourth case to `cases` using `make_block(100e3) + 0.2 * np.exp(2j * np.pi * 250e3 * np.arange(N) / FS)` as its value. Explain whether the score changes.
2. Run `python evaluate.py`. Compare average precision to prevalence and record the confusion counts.
3. To try a window-level split, import `StratifiedKFold` from `sklearn.model_selection` and replace the `GroupKFold(...).split(...)` expression with `StratifiedKFold(n_splits=3, shuffle=True, random_state=0).split(X, y)`. Compare the metrics. The direction of the change can vary on these synthetic inputs.

The confusion counts demonstrate a threshold chosen on the same out-of-fold scores. Use a separate final test set for an independent operating-point evaluation.

Reference run with scikit-learn 1.8.0, NumPy 2.3.5 and SciPy 1.17.0 returned ROC AUC 0.887, average precision 0.475 and prevalence 0.063. At threshold 0.40, the counts were 11 true positives, 11 false positives, 27 false negatives and 551 true negatives. These results differ slightly from the printed example.
