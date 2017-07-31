import numpy as np
from astropy import units as u

from poliastro.bodies import Earth, Sun
from poliastro.twobody import Orbit

from matplotlib import pylab as plt
import mpl_scatter_density

# Data for Mars at J2000 from JPL HORIZONS
a = 1.523679 * u.AU
#a = 1.0779 * u.AU
ecc = 0.093315 * u.one
inc = 1.85 * u.deg
raan = 49.562 * u.deg #this is Right ascension of the ascending node
argp = 286.537 * u.deg
nu = 23.33 * u.deg #True anomaly 

mars = Orbit.from_classical(Sun, a, ecc, inc, raan, argp, nu)


#then plot
from poliastro.plotting import OrbitPlotter
#op = OrbitPlotter()
#op.plot(mars, label="Mars")

#-----------
#plot multiple

#redefining the elements here, sorry that's sloppy

a = 1.0779 * u.AU
ecc = 0.8268 * u.one
inc = 22.852 * u.deg
raan = 88.0822 * u.deg
argp = 31.297 * u.deg
nu = 346.34 * u.deg

#now i define a new orbit

icarus = Orbit.from_classical(Sun, a, ecc, inc, raan, argp, nu)

#plot Icaurs and Mars
op = OrbitPlotter(bgcolor=(0,0,0), linewidth=0.25, markersize=3, audivision=12)
op.plot(mars, label="Mars")
op.plot(icarus,label="Icarus")

plt.show()
plt.savefig('asteroids.png')
