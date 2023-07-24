import numpy as np
import pandas as pd
import warnings
import time

warnings.filterwarnings('ignore')


class LogisticRegression(object):
    def __init__(self, w=[], eta=0.001, n_iter=100):
        self.eta = eta
        self.n_iter = n_iter
        self.w = w

    def _scaling(self, X):
        for i in range(len(X)):
            X[i] = (X[i] - X.mean()) / X.std()
        return X

    def _processing(self, data):
        data = data.dropna()
        features = ["Charms", "Herbology", "Ancient Runes", "Astronomy", "Divination"]
        hp_features = np.array(data[features])
        hp_labels = np.array(data.loc[:, "Hogwarts House"])

        np.apply_along_axis(self._scaling, 0, hp_features)
        return hp_features, hp_labels

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def fit(self, data, batch_size=1):
        X, y = self._processing(data)
        X = np.insert(X, 0, 1, axis=1)

        for i in np.unique(y):
            y_copy = np.where(y == i, 1, 0)
            w = np.ones(X.shape[1])
            for _ in range(self.n_iter):
                indices = np.random.choice(len(X), size=batch_size, replace=False)
                X_batch = X[indices]
                y_batch = y_copy[indices]

                output = X_batch.dot(w)
                errors = y_batch - self._sigmoid(output)
                gradient = np.dot(X_batch.T, errors)

                w += self.eta * gradient
            self.w.append((w, i))
        return self.w

    def _predict_one(self, x):
        return max((x.dot(w), c) for w, c in self.w)[1]

    def predict(self, X):
        return [self._predict_one(i) for i in np.insert(X, 0, 1, axis=1)]

    def score(self, data):
        X, y = self._processing(data)
        return sum(self.predict(X) == y) / len(y)


if __name__ == "__main__":
    start_time = time.time()
    try:
        data = pd.read_csv("dataset_train.csv", index_col = "Index")
    except:
        print("dataset_train.csv not found.")
    weights = LogisticRegression().fit(data, batch_size=32)
    np.save("weights", weights)
    print("Poids sauvegardés dans weights.npy, accuracy :", LogisticRegression().score(data))
    print("Temps d'exécution : {:.3f} secondes".format(time.time() - start_time))