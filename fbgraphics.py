#import matplotlib
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
#import plotly.plotly as py
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
import mpl_scatter_density


from matplotlib.figure import Figure

import sys

import subprocess

def plotAsteroids(x,y):

    #f = Figure(figsize=(5, 4), dpi=100)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='scatter_density')

    #a.plot(x,y,"o")
    ax.scatter_density(x,y)
    ax.set_xlim(-5, 10)
    ax.set_ylim(-5, 10)

    plt.savefig("imggraphics.png")
    subprocess.call(["fbi","imggraphics.png"])
