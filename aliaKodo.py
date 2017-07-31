import numpy as np
from astropy import units as u

from poliastro.bodies import Earth, Sun
from poliastro.twobody import Orbit
f=open("roid_info.txt")
read_lines=f.readlines()
from matplotlib import pylab as plt

#then plot
from poliastro.plotting import OrbitPlotter

#plot Icaurs and Mars
op = OrbitPlotter()

roid_orbits = []

for i in range(75):
    line = read_lines[i]
    # pull out the e, i, arg_p
    line_e = float(line[71:79]) * u.one
    line_inc= float(line[60:68]) * u.deg
    line_pera= float(line[38:46]) * u.deg
    line_semax = float(line[93:103]) * u.AU
    line_name=line[167:194]
    line_raan= float(line[49:57]) * u.deg
    line_ma= float(line[27:35]) * u.deg
    x = Orbit.from_classical(Sun, line_semax, line_e, line_inc, line_raan, line_pera, line_ma)
    roid_orbits.append(x)
    
    
for i in range(75):
    orb = roid_orbits[i]
    op.plot(orb)
    

# Data for Mars at J2000 from JPL HORIZONS



#op.plot(mars)
#op.plot(icarus,label="Icarus")

plt.show()
plt.savefig('asteroids.png')
