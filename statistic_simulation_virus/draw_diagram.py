from typing import List

import matplotlib.pyplot as plt
import numpy as np


def plot(data: List):
    values = np.asarray(data)
    ## Plotten der drei Reihen
    plt.plot( values[:, 0], label="Sus")
    plt.plot( values[:, 1], label="Ill")
    plt.plot( values[:, 2], label="Rec")
    plt.plot( values[:, 3], label="Dead")

    # Diagramm anpassen
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.title("statistical virus simulation")
    plt.legend()
    plt.grid()

    plt.savefig(r"C:\Users\olive\OneDrive\Desktop\Skripte\Semester_5\Statistische_Methoden\Abgabe_Virussimulation/figure.png", dpi=300)
    # Diagramm anzeigen
    plt.show()

