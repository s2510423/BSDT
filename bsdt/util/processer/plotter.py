import matplotlib.pyplot as plt
import numpy
import os
import pandas

def type_check(obj,obj_type):
    if not isinstance(obj,obj_type): raise TypeError(f'{obj} is required to be {obj_type}')

def plotter(dataframe,path,x_key,y_keys,y_colors,title='',x_label='',y_label='',xticks=True,yticks=True):
    if not (dataframe and x_key and y_keys and y_colors): raise ValueError('from util/processer/plotter.py plotter: not enough arguments')
    args = {
        'dataframe' :   pandas.DataFrame,
        'path'      :   list, 
        'x_key'     :   str,
        'y_keys'    :   list,
        'y_colors'  :   list,
        'title'     :   str,
        'x_label'   :   str,
        'y_label'   :   str
    }
    for arg in args: type_check(locals()[arg], args[arg])
    colors = {
        'black' :   (0.0,0.0,0.0,1.0),
        'red'   :   (1.0,0.0,0.0,1.0),
        'green' :   (0.0,1.0,0.0,1.0),
        'blue'  :   (0.0,0.0,1.0,1.0),
        'purple':   (1.0,0.0,1.0,1.0),
        'yellow':   (1.0,1.0,0.0,1.0),
        'cyan'  :   (0.0,1.0,1.0,1.0),
        'orange':   (1.0,0.5,0.0,1.0),
    }
    x = dataframe[x_key]
    y = []
    for y_key in y_keys:
        y.append(dataframe[y_key])
    for i, y_key in enumerate(y):
        plt.plot(x, y_key, label = y_keys[i], color = colors[y_colors[i]], linestyle="-", marker="")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    if xticks == False:
        plt.xticks([])
    if yticks == False:
        plt.yticks([])
    plt.legend(
        loc       = "lower right",
        frameon   = True,
        edgecolor = "black",
        facecolor = "white",
        )

    plt.savefig(f"{os.path.join(path)}{title}.png", dpi=300, bbox_inches='tight')
    plt.close()
