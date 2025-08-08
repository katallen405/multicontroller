#!/usr/bin/env python3
print("Starting imports")
from visual_kinematics.RobotSerial import *
import numpy as np
from math import pi



def main():
    np.set_printoptions(precision=3, suppress=True)

    # based on parameters from https://www.universal-robots.com/articles/ur/application-installation/dh-parameters-for-calculations-of-kinematics-and-dynamics/
    dh_params = np.array([[0.15285, 0., 0.5 * pi, 0.],
                          [0., -0.24355, 0., 0.],
                          [0., -0.2132, 0., 0.],
                          [0.13105,0.,0.5 * pi, 0.],
                          [0.08535, 0., -0.5 * pi, 0.], 
                          [0.0921, 0., 0., 0.]])
    robot = RobotSerial(dh_params)

    # =====================================
    # forward
    # =====================================

    theta = np.array([pi, 0., -0.25 * pi, 0., 0., 0.])
    f = robot.forward(theta)

    print("-------forward-------")
    print("end frame t_4_4:")
    print(f.t_4_4)
    print("end frame xyz:")
    print(f.t_3_1.reshape([3, ]))
    print("end frame abc:")
    print(f.euler_3)
    print("end frame rotational matrix:")
    print(f.r_3_3)
    print("end frame quaternion:")
    print(f.q_4)
    print("end frame angle-axis:")
    print(f.r_3)

    robot.show()


if __name__ == "__main__":
    main()
