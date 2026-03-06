import matplotlib
import numpy
import os
import pandas

def type_check(obj,obj_type):
    if not isinstance(obj,obj_type): raise TypeError(f'{obj} is required to be {obj_type}')

def plotter(dataframe,x_key,y_keys,y_colors,title='',x_label='',y_label=''):
    if not (dataframe and x_key and y_keys and y_colors): raise ValueError('from util/processer/plotter.py plotter: not enough arguments')
    args = {
        dataframe   :   pandas.DataFrame,
        x_key       :   str,
        y_keys      :   dict,
        title       :   str,
        x_label     :   str,
        y_label     :   str
        }
    for arg in args:
        if not type_check(arg, args[arg]): raise TypeError('from util/processer/plotter.py plotter: not proper argument detected')
    colors = {
        'black' :   (0.0,0.0,0.0,1.0),
        'red'   :   (1.0,0.0,0.0,1.0),
        'green' :   (0.0,1.0,0.0,1.0),
        'blue'  :   (0.0,0.0,1.0,1.0),
        'purple':   (1.0,0.0,1.0,1.0),
        'yellow':   (1.0,1.0,0.0,1.0),
        'cyan'  :   (0.0,1.0,1.0,1.0),
        'orange':   (1.0,0.5,1.0,1.0),
    }
    x = dataframe[x_key]
    y = []
    for y_key in y_keys:
        y.append(dataframe[y_key])
        i = 0
    while i < len(y):
        matplotlib.plot(x, y[i], label = y_key, color = y_colors[i], linestyle="-", marker="")

    matplotlib.title(title)
    matplotlib.xticks([])
    matplotlib.grid(axis='x', visible=False)
    matplotlib.xlabel(x_label)
    matplotlib.ylabel(y_label)
    matplotlib.grid(True)
    matplotlib.legend(
        loc       = "lower right",
        frameon   = True,
        edgecolor = "black",
        facecolor = "white",
        )

    matplotlib.savefig(f"{title}.png", dpi=300, bbox_inches='tight')
    matplotlib.close()
