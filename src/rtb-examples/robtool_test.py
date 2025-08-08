import numpy as np
import roboticstoolbox as rtb
from spatialmath import *
from math import pi
import matplotlib.pyplot as plt
from matplotlib import cm
np.set_printoptions(linewidth=100, formatter={'float': lambda x: f"{x:8.4g}" if abs(x) > 1e-10 else f"{0:8.4g}"})

block = False
robot = rtb.models.URDF.KinovaGen3()
obstacle = rtb.Box([1, 1, 1], SE3(1, 0, 0))
iscollision = robot.collided(obstacle) # boolean
iscollision = robot.links[0].collided(obstacle)