from scatter_plot import pair_scatter_plot
from histogram import pair_histogram
import matplotlib.pyplot as plt


def main():
    Courses = ["Arithmancy", "Astronomy", "Herbology", "Defense Against the Dark Arts", "Divination", "Muggle Studies", "Ancient Runes", "History of Magic", "Transfiguration", "Potions", "Care of Magical Creatures", "Charms", "Flying"]

    # Créer la grille de sous-graphiques
    _, ax = plt.subplots(nrows=len(Courses), ncols=len(Courses))
    plt.subplots_adjust(wspace=0.15, hspace=0.15)
    for i, Xcourse in enumerate(Courses):
        for j, Ycourse in enumerate(Courses):

            # Choisir l'axe approprié dans la grille
            if Xcourse == Ycourse:
                pair_histogram(Ycourse, ax[i, j])
            else:
                pair_scatter_plot(Xcourse, Ycourse, ax[i, j])
            if ax[i, j].get_subplotspec().is_last_row():
                ax[i, j].set_xlabel(Courses[j].replace(' ', '\n'), fontsize=8)
            else:
                ax[i, j].tick_params(labelbottom=False)

            if ax[i, j].get_subplotspec().is_first_col():
                ax[i, j].set_ylabel(Courses[i].replace(' ', '\n'), fontsize=8)
            else:
                ax[i, j].tick_params(labelleft=False)

            # ax[i, j].spines['right'].set_visible(False)
            # ax[i, j].spines['top'].set_visible(False)
    plt.legend(loc='center left', frameon=False, bbox_to_anchor=(1, 0.5))
    plt.show()

if __name__ == "__main__":
    main()