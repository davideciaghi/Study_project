# Import the urx and logging libraries
import urx    
import logging
from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper as Rq
from urx.robotiq_two_finger_gripper import RobotiqScript as Rs

def grabScrewdriver(v,a):

    gripper.gripper_action(0)

    jointSequence = {
        "centralpos":[-0.7125352064715784, -1.9114339987384241, -1.4501970450030726, -2.9188717047320765, -0.7277739683734339, -9.428933032343181],
        "midpoint":[0.5760637521743774, -2.065845314656393, -1.6096809546100062, -2.592222515736715, 0.7270185351371765, -9.421797879526409],
        "appBack":[0.40609559416770935, -3.3239977995501917, 0.35812854766845703, -3.3140061537372034, 0.3841108977794647, -9.424280532190593],
        "appHigh1":[0.30100327730178833, -3.36135703722109, 0.4381599426269531, -3.3559463659869593, 0.2793298065662384, -9.424927600214275],
        "appHigh2":[0.23586416244506836, -3.3844860235797327, 0.48784446716308594, -3.3819730917560022, 0.21454833447933197, -9.425323851892742],
        "grabPose1":[0.23884861171245575, -3.4401448408709925, 0.4514589309692383, -3.288023296986715, 0.2174455225467682, -9.429964907953533],
        "grabPose2":[0.24059905111789703, -3.4737160841571253, 0.4294261932373047, -3.2309072653399866, 0.2192293107509613, -9.432890542337688],
        "closeGripper": 255,
        "grabbedHigh1":[0.24064698815345764, -3.4649370352374476, 0.42821598052978516, -3.238678280507223, 0.2191813737154007, -9.432626851389202],
        "grabbedHigh2":[0.24144993722438812, -3.1574657599078577, 0.38404321670532227, -3.5075443426715296, 0.21888214349746704, -9.427242167780193]}

    for pose in jointSequence:

        if pose=="openGripper":
            gripper.gripper_action(0)
            print("Opening gripper")
        elif pose=="closeGripper":
            gripper.gripper_action(255)
            print("Closing gripper")
        else:
            print("Approaching position:",pose)
            UR.movej(jointSequence[pose], acc=a, vel=v)
            

    return print("Screw driver has been grabbed correctly.")



def releaseScrewdriver():

    dz = 0.01 #[1 cm]
    v = 0.05
    a = 0.3
    
    pose = UR.getl()
    pose[2] += dz   # Elevate z by dz

    pointSequence = {
        "centralpos":[0.14399096174567205, -0.5701271907177382, 0.24997350528014362, -0.0021609031633453893, 2.2206992704504036, -2.2205633485310026],
        "highPose":[],
        "releasePose":[],
        "openGripper":gripper.open_gripper(),
        "appHigh":[0.46399688577674664, -0.29997716581269485, 0.060031263254164656, -0.014747276861985101, 2.2105444084801285, -2.2107479026130066],
        "appBack":[0.46400239838184265, -0.2200169662179669, 0.060023600957931925, -0.014664490682634956, 2.2105937021495023, -2.210761078026726],
        "midpoint":[0.26627255497056584, -0.22330771092450646, 0.1700024990336996, -0.19309731464075824, -2.151371268066894, 2.1333976878513914],
        "centralpos":[0.14399096174567205, -0.5701271907177382, 0.24997350528014362, -0.0021609031633453893, 2.2206992704504036, -2.2205633485310026]}

    for pose in pointSequence:
        if pose=="centralpos" or pose=="midpoint" or pose=="highPose":
            UR.movej(pointSequence[pose], acc=a, vel=v)
        else:
            UR.movel(pointSequence[pose], acc=a, vel=v)
        print("Approaching position:",pose)

    return print("Screw driver has been released correctly.")   







if __name__ == "__main__":
    
    logging.basicConfig(level=logging.WARN)
    UR = urx.Robot("10.10.238.32")

    
    # Creazione di un'istanza per la glasse gripper
    gripper = Rq(UR) # L'argomento "robot" va passato perchè richiesto dalla functione __init__() 
    gr = Rs()

    

    try:

        v = 0.25
        a = 0.3

        grabScrewdriver(v,a)


        # pose = UR.getl() # Tool Center Pose of the robot

        # joints = UR.getj()
        # print(joints)

        # UR.movel(pose, acc=a, vel=v)

        #UR.movej(posej2, acc=a, vel=v)

              
    finally:

        UR.close()