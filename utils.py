import csv, sys

def get_data_per_houses():
    house_dicts = [
        {
            "house": "Slytherin",
            "data": {
                "Arithmancy": [],
                "Astronomy": [],
                "Herbology": [],
                "Defense Against the Dark Arts": [],
                "Divination": [],
                "Muggle Studies": [],
                "Ancient Runes": [],
                "History of Magic": [],
                "Transfiguration": [],
                "Potions": [],
                "Care of Magical Creatures": [],
                "Charms": [],
                "Flying": []
            }
        },
        {
            "house": "Gryffindor",
            "data": {
                "Arithmancy": [],
                "Astronomy": [],
                "Herbology": [],
                "Defense Against the Dark Arts": [],
                "Divination": [],
                "Muggle Studies": [],
                "Ancient Runes": [],
                "History of Magic": [],
                "Transfiguration": [],
                "Potions": [],
                "Care of Magical Creatures": [],
                "Charms": [],
                "Flying": []
            }
        },
        {
            "house": "Ravenclaw",
            "data": {
                "Arithmancy": [],
                "Astronomy": [],
                "Herbology": [],
                "Defense Against the Dark Arts": [],
                "Divination": [],
                "Muggle Studies": [],
                "Ancient Runes": [],
                "History of Magic": [],
                "Transfiguration": [],
                "Potions": [],
                "Care of Magical Creatures": [],
                "Charms": [],
                "Flying": []
            }
        },
        {
            "house": "Hufflepuff",
            "data": {
                "Arithmancy": [],
                "Astronomy": [],
                "Herbology": [],
                "Defense Against the Dark Arts": [],
                "Divination": [],
                "Muggle Studies": [],
                "Ancient Runes": [],
                "History of Magic": [],
                "Transfiguration": [],
                "Potions": [],
                "Care of Magical Creatures": [],
                "Charms": [],
                "Flying": []
            }
        }
    ]

    length = 0
    try:
        with open("dataset_train.csv") as file:
            my_reader = csv.reader(file)
            for index, row in enumerate(my_reader):
                if all(map(len, row)):
                    if index == 0:
                        length = len(row)
                    elif len(row) == length:
                        for house_dict in house_dicts:
                            if row[1] == house_dict["house"]:
                                dict = house_dict["data"]
                                for column_index in range(6, 19):
                                    if row[column_index]:
                                        feature_name = list(dict.keys())[column_index - 6]
                                        dict[feature_name].append(float(row[column_index]))
    except IOError:
        print("The csv file has a problem.\n")
        sys.exit(1)
    except ValueError:
        print("One of the values is not correctly formatted as an int or a float.\n")
        sys.exit(1)
    return house_dicts


def get_data_from_csv(filename):
    data_dict = {
                "Arithmancy": [],
                 "Astronomy": [],
                 "Herbology": [],
                 "Defense Against the Dark Arts": [],
                 "Divination": [],
                 "Muggle Studies": [],
                 "Ancient Runes": [],
                 "History of Magic": [],
                 "Transfiguration": [],
                 "Potions": [],
                 "Care of Magical Creatures": [],
                 "Charms": [],
                 "Flying": []}
    length = 0
    try:
        with open(filename, "r") as file:
            my_reader = csv.reader(file)
            for index, row in enumerate(my_reader):
                if all(map(len, row)):
                    if index == 0:
                        length = len(row)
                    elif len(row) == length:
                        column_indices = range(6, 19)
                        for column_index in column_indices:
                            if row[column_index]:
                                feature_name = list(data_dict.keys())[column_index - 6]
                                data_dict[feature_name].append(float(row[column_index]))
    except IOError:
        print("The csv file has a problem.\n")
        sys.exit(1)
    except ValueError:
        print("One of the values is not correctly formated as an int or a float.\n")
        sys.exit(1)
    return data_dict


def min_max_scaling(data):
    min_val = minimum(data)
    max_val = maximum(data)
    scaled_data = []
    for value in data:
        try:
            scaled_value = (value - min_val) / (max_val - min_val)
        except ZeroDivisionError:
            print("Can't divide by 0.")
        scaled_data.append(scaled_value)
    return scaled_data


def ceil(x):
    return int(x) + 1


def sqrt(x):
    return x ** 0.5


def variance(liste):
    mean = sum(liste) / len(liste)
    var_sum = sum((value - mean) ** 2 for value in liste)
    return var_sum / len(liste)


def std_dev(liste):
    var = variance(liste)
    return sqrt(var)


def quartiles(liste):
    liste.sort()
    length = len(liste)
    quartile_1 = ceil(length / 4)
    quartile_2 = ceil(2 * length / 4)
    quartile_3 = ceil(3 * length / 4)
    return float(liste[quartile_1]), float(liste[quartile_2]), float(liste[quartile_3])


def minimum(liste):
    result = liste[0]
    for value in liste:
        if value < result:
            result = value
    return result


def maximum(liste):
    result = liste[0]
    for value in liste:
        if value > result:
            result = value
    return result


def median(liste):
    length = len(liste)
    if length > 0:
        if length % 2:
            return liste[length // 2]
        else:
            return (liste[length // 2 - 1] + liste[length // 2]) / 2


def abs(value):
    if value < 0:
        return -value
    return value


def var_coef(liste):
    mean = sum(liste) / len(liste)
    std = std_dev(liste)
    return (std / abs(mean)) * 100