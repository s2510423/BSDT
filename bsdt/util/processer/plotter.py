import matplotlib
import numpy
import os
from ..parcer import reader

def plotter(path,dataframe,x_key,y_key):
    dir = reader
    if not isinstance(
    x = dataframe[x_key]
    y = dataframe[y_key]
    matplotlib.plot(timelines_arr, drag_arr, label = "Drag", color = (0.0, 0.0, 0.0, 0.5), linestyle="-", marker="")
    matplotlib.axhline(y=float(686), label = "Gravity", color = (0.0, 0.0, 1.0, 0.7), linestyle=":")
    matplotlib.plot(timelines_arr, lift_arr, label = "Lift", color = (1.0, 0.0, 0.0, 1.0), linestyle="-", marker="")

    matplotlib.title(f"Lift and Drag of Human Body [ angle : {self.angle}deg ] [ Wind Velocity : 60m/s ]")
    matplotlib.xticks([])
    matplotlib.grid(axis='x', visible=False)
    matplotlib.xlabel("Time         [   s   ]")
    matplotlib.ylabel("Force        [   N   ]")
    matplotlib.grid(True)
    matplotlib.legend(
        loc       = "lower right",
        frameon   = True,
        edgecolor = "black",
        facecolor = "white",
        )

    matplotlib.savefig(f"single_forces_{self.angle}.png", dpi=300, bbox_inches='tight')
    timelines.clear()
    lift_list.clear()
    drag_list.clear()
    matplotlib.close()
