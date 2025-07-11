# this is where we will translate from our arm-agnoxtic multimodal controller
# to the arm-specific code needed for each type of arm.

#Kinova Gen2 imports
import armpy.arm
import armpy.gripper

# UR3 imports

# Kinova Gen3 imports?

#MoveIt

def arm():
    """
    Returns an instance of the arm class based on the robot type.
    """
    # Here we can add logic to determine which arm to use based on configuration or environment
    return armpy.arm.Arm()  