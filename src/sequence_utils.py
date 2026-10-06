"""Sequence utilities used by the forecasting notebooks."""

import numpy as np


def create_sequences(features, target, dates, lookback, train_end, val_end):
    """Create chronological train/validation/test sliding-window sequences."""
    X_train, y_train = [], []
    X_val, y_val = [], []
    X_test, y_test = [], []
    train_dates, val_dates, test_dates = [], [], []

    for i in range(lookback, len(features)):
        X = features[i - lookback:i]
        y = target[i]

        if i < train_end:
            X_train.append(X)
            y_train.append(y)
            train_dates.append(dates.iloc[i])
        elif i < val_end:
            X_val.append(X)
            y_val.append(y)
            val_dates.append(dates.iloc[i])
        else:
            X_test.append(X)
            y_test.append(y)
            test_dates.append(dates.iloc[i])

    return (
        np.array(X_train, dtype=np.float32),
        np.array(y_train, dtype=np.float32),
        np.array(X_val, dtype=np.float32),
        np.array(y_val, dtype=np.float32),
        np.array(X_test, dtype=np.float32),
        np.array(y_test, dtype=np.float32),
        np.array(train_dates),
        np.array(val_dates),
        np.array(test_dates),
    )
