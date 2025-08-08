#!/usr/bin/env python3

from visual_kinematics.RobotSerial import *
from visual_kinematics.RobotTrajectory import *
import numpy as np
from math import pi


def main():
    np.set_printoptions(precision=3, suppress=True)

    dh_params = np.array([[0.15285, 0., 0.5 * pi, 0.],
                          [0., -0.24355, 0., 0.],
                          [0., -0.2132, 0., 0.],
                          [0.13105,0.,0.5 * pi, 0.],
                          [0.08535, 0., -0.5 * pi, 0.], 
                          [0.0921, 0., 0., 0.]])
  
    robot = RobotSerial(dh_params)

    # =====================================
    # trajectory
    # =====================================

    frames = [Frame.from_euler_3(np.array([0.5 * pi, 0., pi]), np.array([[0.2], [0.223], [0.243]])),
              Frame.from_euler_3(np.array([0.25 * pi, 0., 0.75 * pi]), np.array([[-0.28], [0.2], [0.2]])),
              Frame.from_euler_3(np.array([0.5 * pi, 0., pi]), np.array([[0.28], [0.2], [0.23182]]))]
    time_points = np.array([0., 2., 10.])
    trajectory = RobotTrajectory(robot, frames, time_points)
    trajectory.show(motion="p2p")


if __name__ == "__main__":
    main()
