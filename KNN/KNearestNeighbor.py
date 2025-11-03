import numpy as np
from collections import Counter


class KNearestNeighbors:
    """A very small KNN implementation for educational/demo use.

    Notes:
    - Expects X_train and X_test to be array-like with shape (n_samples, n_features).
    - predict returns a 1-D numpy array of predicted labels.
    """

    def __init__(self, k=3):
        self.k = int(k)

    def fit(self, X_train, y_train):
        self.X_train = np.asarray(X_train)
        self.y_train = np.asarray(y_train)
        return self

    def predict(self, X_test):
        X_test = np.asarray(X_test)
        results = []

        for x in X_test:
            # compute distances to all training points
            distances = []
            for idx, train_row in enumerate(self.X_train):
                dist = np.linalg.norm(x - train_row)
                distances.append((idx, dist))

            # sort by distance and take k nearest
            distances = sorted(distances, key=lambda t: t[1])
            k_nearest = distances[: self.k]

            # determine label
            label = self.classify(k_nearest)
            results.append(label)

        return np.array(results)

    def classify(self, distance):
        """distance: iterable of (index, distance) tuples for nearest neighbours"""
        labels = []
        for idx, _ in distance:
            labels.append(self.y_train[idx])

        return Counter(labels).most_common(1)[0][0]
