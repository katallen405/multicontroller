#!/bin/env python3
# flexibleIK.py
# Kat Allen 2025
# kat.allen@tufts.edu

# place a user coordinate frame at their heart (defining manipulation workspace)
x_heart =
y_heart =
z_heart =
offset = 0 # this allows for the workspace to extend above the heart

# place a user coordinate frame at their eyes (defining visual workspace)
x_eyes =
y_eyes =
z_eyes =


# publish relations to world frame
#https://docs.ros.org/en/humble/Tutorials/Intermediate/Tf2/Writing-A-Tf2-Static-Broadcaster-Py.html

# EE position xyz needs to be inside a cone bounded by:

#z_heart + offset > z 
#z_eyes = x_eyes * tan(alpha)
# 0 < alpha < 30deg
# 500mm < x_eyes < 750mm
# theta is the rotation around the z axis (rotating x, the gaze axis, down)
# x_eyes * tan(theta) > y_eyes > x_eyes * -tan(theta) 
# -15deg < theta < 15deg

# EE orientation needs to orient one of the object's faces to the gaze axis
# current gaze frame = [0, -theta, alpha] from eyes frame
# object frame = EE_frame + rotations of n*(+/-90deg) in r, p, or y
# ROS defines euler angles from the original axes

#EE_frame = euler[0+l*pi/2, -theta+m*pi/2, alpha_n*(pi/2)]

#from an original frame offset only in translation from the eye frame.
#l,m,n are positive or negative whole numbers 0->4


# Collision prevention - hard constraints
# 

