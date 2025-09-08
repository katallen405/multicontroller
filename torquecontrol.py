#! /usr/bin/env python3
# Kat Allen 2025, modified from Kinova gravity_compensated_mode.py

import roslib; roslib.load_manifest('kinova_demo')
import rospy
from kinova_msgs.srv import *
from kinova_demo.robot_control_modules import *

prefix = 'j2s7s300_'
nbJoints = 7
interactive = True
duration_sec = 10


if __name__ == '__main__':
  try:        
    prefix, nbJoints = argumentParser(None)
    rospy.init_node('torque_compensated_mode',log_level=rospy.DEBUG)
    if (interactive == True):
      nb = input("Moving robot to candle like position, and setting zero torques, press return to start, n to skip")
    if (nb != "n" and nb != "N"):

      result = joint_position_client([180]*7, prefix)

      if (interactive == True):
        nb = input('Setting torques to zero, press return')
      ZeroTorque(prefix)

    if (interactive == True):
      nb = input('Starting gravity compensation mode')

      publishTorqueCmd([0,0,0,0,0,0,0], duration_sec, prefix)
      print("torque command 0 sent")

    print("Enter new torque command as [a,b,c,d,e,f,g] or q to exit")
    command = [0,0,0,0,0,0,0]
    quitprogram = False
    while quitprogram == False:
      print("enter a new torque command")
      command = input()
      list_command = command.split(',')
      print(command, "is of type", type(command))
      command = [float(x) for x in list_command]
      if command=="q":
        quitprogram=True
      elif len(command) == 7:
        print("enter duration")
        duration = int(input())
        
        
        
        publishTorqueCmd(command, duration, prefix)
        print("published the torque command")
      else:
        print("wrong length")
    print("Done!")
  except rospy.ROSInterruptException:
    print("program interrupted before completion")
