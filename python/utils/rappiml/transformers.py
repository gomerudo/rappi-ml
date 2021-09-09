import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class DateTimeTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, onehot=True):
        self.onehot = onehot

    def fit(self, X, y=None):
        self.months = 12
        self.days = 30
        self.hours = 24
        return self

    def transform(self, X):
        # This has to be iterative
        res = []
        for dt_date in X:

            # Values
            month = dt_date.month
            day = dt_date.day
            hour = dt_date.hour
            hhalf = int(dt_date.minute >= 30)

            # Example: month = 8, day = 30, hour = 0, hhalf = 1
            # [
            #   0 0 0 0 0 0 0 1 0 0 0 0
            #   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
            #   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
            #   1
            # ]
            # Build row accordingly
            if self.onehot:
                row = np.zeros(self.months + self.days + self.hours + 1)
                row[month - 1] = 1  # Shift -1: month starts at 1
                row[self.months + day - 1] = 1  # Shift -1: day starts at 1
                row[self.months + self.days + hour] = 1
                row[-1] = hhalf
            else:
                row = [month, day, hour, hhalf]

            res.append(row)

        res = np.array(res)
        return np.squeeze(res)


class DropColumnsTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, cols):
        if not isinstance(cols, list):
            self.cols = [cols]
        else:
            self.cols = cols

    def fit(self, X, y=None):
        # there is nothing to fit
        return self

    def transform(self, X):
        X = X.copy()
        return X.drop(self.cols, axis=1)
