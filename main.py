import argparse
from math import pi
from math import sqrt

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--backend", help="Selects the backend for the graphics. Arguments: fbgraphics, imggraphics, simple, Tk.")
args = parser.parse_args()
if(args.backend=="fbgraphics"):
    import fbgraphics as graphics
elif (args.backend=="imggraphics"):
    import imggraphics as graphics
elif (args.backend=="simple"):
    import simplegraphics as graphics
elif (args.backend=="Tk"):
    import graphics2 as graphics
elif (args.backend):
    raise Exception('Invalid backend! Valid backends are "fbgraphics", "imggraphics", "simple", and "Tk"')
else :
    import imggraphics as graphics

import numpy as np
from numpy import radians
from scipy.constants import kilo

from orbital import earth, sun, KeplerianElements, Maneuver, plot, plot3d, plotting
m= (1.32712440018)*(10**20)
#help(KeplerianElements.with_period)
def plotAsteroid(eccentricity, inclination, argp, a):
    return KeplerianElements.with_period(2*pi*sqrt((a**3)/m),e=eccentricity,i=radians(inclination),arg_pe=radians(argp),body=earth)
help(KeplerianElements.with_period)


albert_e = 0.2225693 
albert_i = 10.82763
albert_a = 178.81528
a        = 218103219999.9997253
#inclination, argument of perihiliam is in degrees
#semi-major axis is in meteres converts from au
#ecceleration is in 


molniya_a = plotAsteroid(albert_e, albert_i, albert_a, a)
from orbital import earth_sidereal_day
molniya = KeplerianElements.with_period(
    earth_sidereal_day / 2 +27, e=0.741, i=radians(63.4), arg_pe=radians(270),
    body=earth)

#arg_pe


# Simple circular orbit
orbit = KeplerianElements.with_altitude(1000 * kilo, body=earth)

print(type(molniya))

#print(orbit)
#help(orbit)

N = 10000000
x = []
y = []

plotter=plotting.Plotter2D()
f = orbit.f
pos = plotter._perifocal_coords(molniya, f)
x = x+[pos[0]]
y = y+[pos[1]]
x = x+[plotter._perifocal_coords(molniya_a, f)[0]]
y = y+[plotter._perifocal_coords(molniya_a, f)[1]]
#print(plotter._perifocal_coords(molniya,orbit.f))
#print(plotter._plot_position(molniya))

graphics.plotAsteroids(pos[0],pos[1])
