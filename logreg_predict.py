import pandas as pd
import numpy as np
import csv


def _scaling(X):
        for i in range(len(X)):
            X[i] = (X[i] - X.mean())  / X.std()
        return X


def fill_na(data):
    for col in data.columns[5:19]:
        coll = []
        for mark in data[col]:
            if pd.notnull(mark):  # Vérifier si la valeur n'est pas NaN
                coll.append(mark)
        if coll:
            mean = sum(coll) / len(coll)
            data[col].fillna(mean, inplace=True)
    return data


def _processing(data):
    data = fill_na(data)
    data = data.dropna()
    features = ["Charms", "Herbology", "Ancient Runes", "Astronomy", "Divination"]
    hp_features = np.array(data[features])
    
    np.apply_along_axis(_scaling, 0, hp_features)
    return hp_features


def _predict_one(x, w):
    return max((x.dot(w), c) for w, c in w)[1]
    
def predict(data, w):
    X = _processing(data)
    return [_predict_one(i, w) for i in np.insert(X, 0, 1, axis=1)]


def accuracy():
    myfile = pd.read_csv("houses.csv", usecols=lambda column: column != 'Index')
    truth = pd.read_csv("dataset_truth.csv", usecols=lambda column: column != 'Index')
    return (len(myfile) - len(myfile.compare(truth))) / len(myfile) * 100


def main():
    try:
        filename = "dataset_test.csv"
        data = pd.read_csv(filename, usecols=lambda column: column != 'Hogwarts House')
        filename = "weights.npy"
        result = predict(data, np.load(filename, allow_pickle=True))
        filename = "houses.csv"
        with open(filename, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["Index", "Hogwarts House"])
            for i in range(len(result)):
                writer.writerow([i, result[i]])
        print("Result has been saved in houses.csv")
        print("The accuracy is " + str(accuracy()) + "%")
    except:
        print(filename + " not found.")

if __name__ == "__main__":
    main()