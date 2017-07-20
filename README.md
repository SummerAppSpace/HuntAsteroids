# HuntAsteroids
There's over 700,000 discovered asteroids in our solar system. Because they are so small, and occupy a region so vast, it's often difficult to depict them visually. If asteroids are shown orbiting the Sun next to the planets, often the sizes of the asteroids have to be greatly exaggerated in order to be seen. This makes space seem more crowded then it actually is. A very popular asteroid depiction is by Scott Manley: https://www.youtube.com/watch?v=BKKg4lZ_o-Y

Active researchers struggle with this problem, as do science communicators trying to help others understand the layout of our solar system. Create one solution by depict the asteroids in our solar system. You can choose to try to show all the asteroids, or a small portion of them. 

 
## Tips:
* Eventually it would be great to create a movie, but start with a single image.
* With 700,000 asteroids, these plots can take a while to make. Start small while you're figuring things out, with just a few asteroids, and add the rest in later.

## Data Resources
* https://pythonhosted.org/OrbitalPy/
Consider using this code as a starting point. You'll want to modify it so that it produces plots that look the way you want, and then you'll want to modify it so that it can read in the orbital elements of actual asteroids (see below). Later you can use the animation.

* http://www.minorplanetcenter.net/iau/MPCORB.html
Each asteroid's path is described by six numbers, or orbital elements. These numbers are: eccentricity, semimajor axis, inclination, longitude of the ascending node, and argument of periapsis. If you know these six numbers, you know where the asteroid is going, and you can also plot it's orbit. The Minor Planet Center has orbital elements for all the known asteroids.

* These orbital elements are in a special format, you can read about the format here:
http://www.minorplanetcenter.net/iau/info/MPOrbitFormat.html

* https://github.com/astrofrog/mpl-scatter-density
Here's a density map package; density maps are good ways to plot lots of points.

* Google "point clouds" and data visualization to learn about clever ways to depict large numbers of points.

* [Resources listed on 2016 Space Apps Challenge Page](https://github.com/SpaceApps2016/Resources)
