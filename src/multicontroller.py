#!/bin/env python3
# multicontroller.py
# Kat Allen 2025
# kat.allen@tufts.edu

from hapticcomm import waypointgathering
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir
import csv
import armpy.arm
import armpy.gripper
import pickle
# stuff for speech
import rospy
import smach
import smach_ros
import actionlib
import sys

# A multimodal controller for close-contact HRI with a robot arm

class multimodal_controller():
    def __init__(self, arm, gripper):
        self.arm = arm
        self.gripper = gripper
        self.mode = 'manual'  # default mode
        self.location = None  # current location of the arm
        self.arm_type = None  # type of the arm (e.g., Kinova, UR3, etc.)

    def set_mode(self, mode):
        self.mode = mode
        print(f"Mode set to {self.mode}")

    def get_mode(self):
        return self.mode

    def manual_control(self):
        # Implement manual control logic here
        pass

    def autonomous_control(self, target_position=None)
        # In autonomous mode, the arm goes to a known position
        # to retrieve an object and bring it back to the workspace. The planner is
        # aware of objects in the workspace and plans around them.
        if target_position is None:
            print("No target position provided for autonomous control.")
            return
        try:

    def force_control(self):
        # Implement force control logic here
        pass

    def support_user(self):
        # Implement support user logic here
        pass
    def reconfigure_null_space(self):
        # Implement null space reconfiguration logic here
        pass    



def force_control_mode():
# In FC mode, the arm holds position against gravity but can be moved
# out of the way or into a particular position by the operator pushing
# on the joints. This is just Kinova's KT mode or UR3's freedrive
# mode


def support_user_mode():
# In this mode, the robot arm holds not just itself against gravity
# but supports the user's arm so they can rest on the robot (possibly
# while the robot is also holding something for them

def reconfigure_null_space():
# Move the robot arm without moving the end effector 
