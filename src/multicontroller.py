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
import hlpr_dialogue_production.msg as dialogue_msgs
import sys

# A multimodal controller for close-contact HRI with a robot arm

def autonomous_mode():
# In autonomous mode, the arm goes to a known position
# to retrieve an object and bring it back to the workspace. The planner is
# aware of objects in the workspace and plans around them. (How?)
# Is this the same or different than "move out of my way" mode?


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
