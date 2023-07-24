import csv, sys
import matplotlib.pyplot as plt
from utils import std_dev, get_data_per_houses, get_data_from_csv


def pair_histogram(Course, ax):
    house_dict = get_data_per_houses()

    # houses = ["Hufflepuff", "Ravenclaw", "Gryffindor", "Slytherin"]
    # house_colors = ["yellow", "blue", "red", "green"]
    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
    house_colors = ["red", "green", "blue", "yellow"]
    for house,color in zip(houses, house_colors):
        notes = [d["data"][Course] for d in house_dict if d["house"] == house]
        ax.hist(notes, color=color, alpha=0.5, label=house)
    ax.tick_params(labelsize=6)


def histogram(Course):
    house_dict = get_data_per_houses()

    houses = ["Hufflepuff", "Ravenclaw", "Gryffindor", "Slytherin"]
    house_colors = ["yellow", "blue", "red", "green"]
    for house,color in zip(houses, house_colors):
        notes = [d["data"][Course] for d in house_dict if d["house"] == house]
        plt.hist(notes, label=house, alpha=0.5, color=color)
    plt.legend(fontsize=8)
    plt.ylabel("Number of students")
    plt.xlabel("Marks")


def main():
    data_dict = get_data_from_csv("dataset_train.csv")
    courses = []
    std = []
    for key, value in data_dict.items():
        if len(key) > 15:
            key = key[:-(len(key)-15)] + '.'
        courses.append(key)
        std.append(std_dev(value))

    plt.style.use("ggplot")
    fig1 = plt.figure()
    plt.bar(courses, std, width=0.5)
    plt.yscale('log')
    plt.ylabel("Standard Deviation (log)")
    plt.tick_params(axis='x', rotation=25, labelsize=6)
    fig1.tight_layout()
    fig2 = plt.figure()
    histogram("Care of Magical Creatures")
    plt.show()


if __name__ == "__main__":
    main()