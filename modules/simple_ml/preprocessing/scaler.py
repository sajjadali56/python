# simple_ml/preprocessing/scaler.py
class StandardScaler:
    def __init__(self):
        self.mean_ = 0
        self.std_ = 1

    def fit(self, X):
        self.mean_ = sum(X) / len(X)
        self.std_ = (sum((x - self.mean_) ** 2 for x in X) / len(X)) ** 0.5
        print("Fitting scaler...")

    def transform(self, X):
        return [(x - self.mean_) / self.std_ for x in X]

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)
