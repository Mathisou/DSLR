from tracemalloc import start
import numpy as np
import pandas as pd
import warnings
import time
import matplotlib.pyplot as plt

# warnings.filterwarnings('ignore')


class LogisticRegression(object):
    def __init__(self, w=[], eta=0.0005, n_iter=300):
        self.eta = eta
        self.n_iter = n_iter
        self.w = w


    def _scaling(self,X):
        for i in range(len(X)):
            X[i] = (X[i] - X.mean())  / X.std()
        return X

        
    def _processing(self,data):
        data = data.dropna()
        features = ["Charms", "Herbology", "Ancient Runes", "Astronomy", "Divination"]
        hp_features = np.array(data[features])
        hp_labels = np.array(data.loc[:,"Hogwarts House"])
        
        hp_features = np.apply_along_axis(self._scaling, 0, hp_features)
        return hp_features, hp_labels
        
        
    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    

    def _cost(self,theta, x, y):
        h = self._sigmoid(np.dot(x, theta.T))
        m = len(y)
        cost = 1 / m * np.sum(
            -y * np.log(h) - (1 - y) * np.log(1 - h)
        )
        return cost


    def fit(self, data):
        X, y = self._processing(data)
        X = np.insert(X, 0, 1, axis=1)
        # steps = [i for i in range(0, self.n_iter)]
        for i in np.unique(y):
            y_copy = np.where(y == i, 1, 0)
            w = np.ones(X.shape[1])
            cost = []
            for _ in range(self.n_iter):
                output = X.dot(w)
                error = y_copy - self._sigmoid(output)
                gradient = np.dot(X.T, error)
                # j = self._cost(w, X, y_copy)
                w += self.eta * gradient
                # print(j)
                # cost.append(j)
            # print(cost)
            # plt.plot(steps, cost, label=i)
            self.w.append((w, i))
        # plt.xlabel("epoch")
        # plt.ylabel("cost")
        # plt.legend()
        # plt.show()
        return self.w

    
    def _predict_one(self, x):
        return max((x.dot(w), c) for w, c in self.w)[1]


    def predict(self, X):
        return [self._predict_one(i) for i in np.insert(X, 0, 1, axis=1)]
    
    
    def score(self,data):
        X, y = self._processing(data)
        return sum(self.predict(X) == y) / len(y)   
    



    
    
if __name__ == "__main__":
    start_time = time.time()
    try:
        data = pd.read_csv("dataset_train.csv", index_col = "Index")
    except:
        print("dataset_train.csv not found.")
    weights = LogisticRegression().fit(data)
    np.save("weights", weights)
    print("Poids sauvegardés dans weights.npy, accuracy :", LogisticRegression().score(data))
    print("Temps d'exécution : {:.3f} secondes".format(time.time() - start_time))
