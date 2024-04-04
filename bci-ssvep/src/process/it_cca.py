import numpy as np
from sklearn.feature_selection import mutual_info_regression
from scipy.optimize import minimize


class ITCCA:
    def __init__(self, n_components=2, alpha=0.5):
        self.n_components = n_components
        self.alpha = alpha
        self.components_ = None
        self.correlation_ = None

    def objective_function(self, x, *args):
        X, Y, alpha = args
        n_samples = X.shape[0]
        X_proj = X.dot(x)
        Y_proj = Y.dot(x)
        corr = np.abs(np.corrcoef(X_proj, Y_proj, rowvar=False)[0, 1])
        mi_X = mutual_info_regression(X, X_proj) / np.log2(n_samples)
        mi_Y = mutual_info_regression(Y, Y_proj) / np.log2(n_samples)
        return -(1 - alpha) * corr + alpha * (mi_X + mi_Y)

    def fit(self, X, Y):
        # Ensure X and Y are NumPy arrays with appropriate data types
        X = np.array(X, dtype=float)
        Y = np.array(Y, dtype=float)

        # Ensure X and Y are 2D arrays
        if len(X.shape) == 1:
            X = np.expand_dims(X, axis=1)
        if len(Y.shape) == 1:
            Y = np.expand_dims(Y, axis=1)

        n_features = X.shape[1]
        init_x = np.random.randn(n_features)
        res = minimize(self.objective_function, init_x, args=(X, Y, self.alpha))
        self.components_ = res.x
        # Calculate correlation coefficient
        X_proj = X.dot(self.components_.reshape(-1, 1))  # Reshape components for proper alignment
        Y_proj = Y.dot(self.components_.reshape(-1, 1))  # Reshape components for proper alignment
        self.correlation_ = np.abs(np.corrcoef(X_proj.flatten(), Y_proj.flatten())[0, 1])

    def transform(self, X):
        # Ensure X is a NumPy array with appropriate data type
        X = np.array(X, dtype=float)

        # Ensure X is a 2D array
        if len(X.shape) == 1:
            X = np.expand_dims(X, axis=1)

        # Ensure components are reshaped properly
        components_reshaped = self.components_.reshape(-1, 1)

        # Perform dot product
        return X.dot(components_reshaped).flatten()