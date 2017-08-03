import numpy as np
from astropy import units as u
from astropy import time
import datetime

from poliastro.bodies import Earth, Sun
from poliastro.twobody import Orbit
f=open("roid_info.txt")
read_lines=f.readlines()
from matplotlib import pylab as plt
import argparse

#then plot
from poliastro.plotting import OrbitPlotter

parser = argparse.ArgumentParser()
parser.add_argument("--asteroids", "-n", help="changes the number of asteroids")
args=parser.parse_args()
print(type(args.asteroids))
if not args.asteroids:
    asteroids=75
else:
    asteroids=int(args.asteroids)

tempo=datetime.datetime(2000,1,1,0,0,0)
#help(Orbit.from_classical)

offset=float(0)

for frame in range(60*60):
    offset=offset+1
    astratempo = time.Time(tempo, scale='utc')#, value=J2000.000)
    print("Rendering frame "+str(frame)+" for "+str(astratempo)+"...")
    
    #plot Icaurs and Mars
    op = OrbitPlotter(bgcolor=(0,0,0), linewidth=0.01, markersize=3, audivision=12)

    roid_orbits = []

    for i in range(asteroids):
        line = read_lines[i]
        # pull out the e, i, arg_p
        line_e = float(line[71:79]) * u.one
        line_inc= float(line[60:68]) * u.deg
        line_pera= float(line[38:46]) * u.deg
        line_semax = float(line[93:103]) * u.AU
        line_name=line[167:194]
        line_raan= float(line[49:57]) * u.deg
        line_ma= (float(line[27:35])+offset) * u.deg
        #x = Orbit.from_classical(Sun, line_semax, line_e, line_inc, line_raan, line_pera, line_ma, epoch=astratempo)
        x = Orbit.from_classical(Sun, line_semax, line_e, line_inc, line_raan, line_pera, line_ma)#, astratempo)
        roid_orbits.append(x)


    for i in range(75):
        orb = roid_orbits[i]
        op.plot(orb)


    # Data for Mars at J2000 from JPL HORIZONS



    #op.plot(mars)
    #op.plot(icarus,label="Icarus")

    plt.savefig('Frames/asteroids'+str(frame)+'.png')
    plt.close()

    tempo=tempo+datetime.timedelta(days=150)
