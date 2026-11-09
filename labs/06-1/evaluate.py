import numpy as np
from sklearn.metrics import (average_precision_score, roc_auc_score,
                                 precision_recall_curve, confusion_matrix)
from sklearn.model_selection import GroupKFold
from sklearn.ensemble import RandomForestClassifier


rng = np.random.default_rng(11)


# Synthetic feature table: 6 capture sessions, 100 windows each, 5 % anomalies.
sessions = np.repeat(np.arange(6), 100)
y = (rng.random(sessions.size) < 0.05).astype(int)
session_bias = rng.normal(0, 0.5, size=6)[sessions]         # per-session "environment"
X = np.column_stack([rng.normal(0, 1, sessions.size) + 2.0 * y + session_bias,
                       rng.normal(0, 1, sessions.size) + 1.0 * y])


# Split by SESSION, never by window: neighbouring windows are near-duplicates.
scores = np.zeros(len(y))
for train, test in GroupKFold(n_splits=3).split(X, y, groups=sessions):
    clf = RandomForestClassifier(n_estimators=200, class_weight="balanced",
                                      random_state=0).fit(X[train], y[train])
    scores[test] = clf.predict_proba(X[test])[:, 1]


print("ROC AUC:               ", round(roc_auc_score(y, scores), 3))
print("Average precision: ", round(average_precision_score(y, scores), 3),
      "(baseline = prevalence =", round(y.mean(), 3), ")")


# Choose an operating point from a false-alarm budget, not from 0.5.
prec, rec, thr = precision_recall_curve(y, scores)
ok = np.where(prec[:-1] >= 0.5)[0]        # want >= 50 % precision
t_star = thr[ok[0]] if ok.size else 0.5
tn, fp, fn, tp = confusion_matrix(y, scores >= t_star).ravel()
print(f"threshold={t_star:.2f}       TP={tp} FP={fp} FN={fn} TN={tn}")
