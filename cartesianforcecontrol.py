#! /usr/bin/env python3
# Kat Allen 2025, modified from Kinova gravity_compensated_mode.py

import roslib; roslib.load_manifest('kinova_demo')
from tf.transformations import quaternion_from_euler
import kinova_msgs.srv
import kinova_demo.robot_control_modules as rcm
import rospy
import numpy as np
prefix = 'j2s7s300_'
nbJoints = 7
interactive = True
duration_sec = 10

def cartesianpositionstart(): # this kind of works but the cartesian solver
    # is not very good
    initialpositionentered = False
    # keyboard entry of initial position and orientation
    while initialpositionentered == False:
        print("Enter initial end effector position as x,y,z or enter to use `deskside' (-0.178,-0.674,0.171)")
        position_string = input()
        if position_string == "": # use the preset "deskside helper" position
            position_string = "-0.1782289445400238,-0.6746525168418884,0.17110002040863037"
        position_list = position_string.split(',')
        position_list = [float(x) for x in position_list]
        
        print("Initial positions", position_list)
        
        print("Enter initial orientation as euler (rot around x, rot around y, rot around z) or enter for deskside preset")
        rotation_string = input()
        if rotation_string =='':
            print("using default orientation")
            rotation_string = "1.24627,-1.363314,2.858888"
        else: pass
        
        rotation_list = rotation_string.split(',')
        rotation_list = [float(x) for x in rotation_list]
        quaternion_list = quaternion_from_euler(rotation_list[0],rotation_list[1],rotation_list[2])
        print("Rotation entered was ", rotation_list)
        print("Quaternion calculated is", quaternion_list)
        
        print("Enter to continue or n to try again")
        result = input()
        if result == "":
            initialpositionentered = True
        else:
            pass
    # cartesian execution, tries for about a minute and then fails and crashes
    rcm.cartesian_pose_client(position_list, quaternion_list, prefix)

if __name__ == '__main__':
  try:
    prefix, nbJoints = rcm.argumentParser(None)
  except:
    pass #use defaults from above
  try:
    rospy.init_node('cartesian_force_mode',log_level=rospy.DEBUG)
    print("homing robot, no collision scene awareness")
    rcm.homeRobot(prefix)  #home robot for cartesian control to work
    help_position = [1.1344166095289108, 1.9797486806263742, 3.382395413038649, 1.2493353395171924, -1.9042559200478435, 1.7800001472777442, 3.231052761979408]
    help_degrees = np.degrees(help_position)

    rcm.joint_position_client(help_degrees, prefix)
    
    rcm.



  except rospy.ROSInterruptException:
        print("program interrupted before completion")
