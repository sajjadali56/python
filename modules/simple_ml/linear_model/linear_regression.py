# simple_ml/linear_model/linear_regression.py
class LinearRegression:
    def __init__(self):
        self.coefficient_ = None
        self.intercept_ = None

    def fit(self, X, y):
        # Very simple linear fit calculation (mocked)
        self.coefficient_ = sum(X) / len(X)
        self.intercept_ = sum(y) / len(y) - self.coefficient_ * sum(X) / len(X)
        print("Fitting model...")

    def predict(self, X):
        if self.coefficient_ is None or self.intercept_ is None:
            raise ValueError("Model is not fitted yet.")
        return [self.coefficient_ * x + self.intercept_ for x in X]
