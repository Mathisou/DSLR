import matplotlib.pyplot as plt
from histogram import get_data_per_houses
from utils import get_data_per_houses
import itertools


def pair_scatter_plot(XCourse, YCourse, ax):
    house_dict = get_data_per_houses()
    # houses = ["Hufflepuff", "Ravenclaw", "Gryffindor", "Slytherin"]
    # house_colors = ["yellow", "blue", "red", "green"]
    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
    house_colors = ["red", "green", "blue", "yellow"]
    for house,color in zip(houses, house_colors):
        XMarks = list(itertools.chain.from_iterable([d["data"][XCourse] for d in house_dict if d["house"] == house]))
        YMarks = list(itertools.chain.from_iterable([d["data"][YCourse] for d in house_dict if d["house"] == house]))
        if len(XMarks) > len(YMarks):
            XMarks = XMarks[:len(YMarks)]
        elif len(YMarks) > len(XMarks):
            YMarks = YMarks[:len(XMarks)]
        ax.scatter(XMarks, YMarks, color=color, s=2, alpha=0.5)
    ax.tick_params(labelsize=6)


def scatter_plot(XCourse, YCourse):
    house_dict = get_data_per_houses()
    houses = ["Hufflepuff", "Ravenclaw", "Gryffindor", "Slytherin"]
    house_colors = ["yellow", "blue", "red", "green"]
    for house,color in zip(houses, house_colors):
        XMarks = list(itertools.chain.from_iterable([d["data"][XCourse] for d in house_dict if d["house"] == house]))
        YMarks = list(itertools.chain.from_iterable([d["data"][YCourse] for d in house_dict if d["house"] == house]))
        if len(XMarks) > len(YMarks):
            XMarks = XMarks[:len(YMarks)]
        elif len(YMarks) > len(XMarks):
            YMarks = YMarks[:len(XMarks)]
        plt.scatter(XMarks, YMarks, color=color, label=house, alpha=0.5)
    plt.xlabel(XCourse)
    plt.ylabel(YCourse)
    plt.legend()


def main():
    scatter_plot("Astronomy", "Defense Against the Dark Arts")
    plt.show()


if __name__ == "__main__":
    main()