import sys
import csv
from utils import maximum, variance, minimum, std_dev, quartiles, get_data_from_csv, median, var_coef


def analyze_data(data_dict):
    describe_dict = {"Arithmancy": [],
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
    for key, value in data_dict.items():
        count = len(value)
        mean = sum(value) / count
        var = variance(value)
        std = std_dev(value)
        mini = minimum(value)
        qrt_1, qrt_2, qrt_3 = quartiles(value)
        maxi = maximum(value)
        med = median(value)
        iqr = qrt_3 - qrt_1
        var_coeff = var_coef(value)
        my_list = [count, mean, var, std, mini, qrt_1, qrt_2, qrt_3, maxi, med, iqr, var_coeff]
        describe_dict[key].extend(my_list)
    return describe_dict


def display_data(describe_dict):
    spaces = 20
    type_list = ["Count",
                 "Mean",
                 "Var",
                 "Std",
                 "Min",
                 "25%",
                 "50%",
                 "75%",
                 "Max",
                 "Median",
                 "IQR",
                 "Var Coef."]
    first_line = " " * spaces
    for key in describe_dict.keys():
        if len(key) <= spaces:
            actual_case = " " * (spaces - len(key)) + key
        else:
            actual_case = 2 * " " + key[:spaces - 3] + "."
        first_line += actual_case
    result = first_line + "\n"
    length = len(describe_dict["Arithmancy"])
    for index in range(length):
        type_of_data = type_list[index] + " " * (spaces - len(type_list[index]))
        line = type_of_data
        for value in describe_dict.values():
            info_value = f"{value[index]:.6f}"
            line += " " * (spaces - len(info_value)) + info_value
        result += line + "\n"
    print(result)


def main(argv):
    if len(argv) != 2:
        print("Usage: describe.py [dataset]\n")
        sys.exit(1)
    data_dict = get_data_from_csv(argv[1])
    describe_dict = analyze_data(data_dict)
    display_data(describe_dict)


if __name__ == "__main__":
    main(sys.argv)