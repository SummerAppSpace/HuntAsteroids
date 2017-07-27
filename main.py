import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-b", "--backend", help="Selects the backend for the graphics. Arguments: fbgraphics, imggraphics, simple, Tk.")
args = parser.parse_args()
if(args.backend=="fbgraphics"):
    import fbgraphics as graphics
elif (args.backend=="imggraphics"):
    import imggraphics as graphics
elif (args.backend=="simple"):
    import graphics as graphics
elif (args.backend=="Tk"):
    import graphics2 as graphics
elif (args.backend):
    raise Exception('Invalid backend! Valid backends are "fbgraphics", "imggraphics", "simple", and "Tk"')
else :
    import imggraphics as graphics

import numpy as np
from numpy import radians
from scipy.constants import kilo

from orbital import earth, KeplerianElements, Maneuver, plot, plot3d

#help(KeplerianElements.with_period)
from orbital import earth_sidereal_day
molniya = KeplerianElements.with_period(
    earth_sidereal_day / 2, e=0.741, i=radians(63.4), arg_pe=radians(270),
    body=earth)

print(molniya)

# Simple circular orbit
orbit = KeplerianElements.with_altitude(1000 * kilo, body=earth)

N = 10000000
x = np.random.normal(4, 2, N)
y = np.random.normal(3, 1, N)


graphics.plotAsteroids(x,y)
