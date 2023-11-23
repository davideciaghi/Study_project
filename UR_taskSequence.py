# Import the urx and logging libraries
import urx    
import logging
from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper as Rq
from urx.robotiq_two_finger_gripper import RobotiqScript


def grabScrewdriver():

    dz = 0.01 #[1 cm]
    v = 0.05
    a = 0.3
    
    pose = UR.getl()
    pose[2] += dz   # Elevate z by dz

    pointSequence = {"centralpos":[0.14399096174567205, -0.5701271907177382, 0.24997350528014362, -0.0021609031633453893, 2.2206992704504036, -2.2205633485310026],
                  "openGripper": Rq.open_gripper(),
                  "midpoint":[0.26627255497056584, -0.22330771092450646, 0.1700024990336996, -0.19309731464075824, -2.151371268066894, 2.1333976878513914],
                  "appBack":[0.46400239838184265, -0.2200169662179669, 0.060023600957931925, -0.014664490682634956, 2.2105937021495023, -2.210761078026726],
                  "appHigh":[0.46399688577674664, -0.29997716581269485, 0.060031263254164656, -0.014747276861985101, 2.2105444084801285, -2.2107479026130066],
                  "grabPose":[0.4634921672570897, -0.2979917645786146, 0.007989129348451102, -0.01916847105868526, 2.212717494917562, -2.2126966418911715],
                  "closeGripper": Rq.close_gripper(),
                  "grabbedHigh":[0.4630317844491301, -0.29798699935952866, 0.1399852406807909, -0.01963029037007349, 2.2126360393302718, -2.2127382625853818]}

    for pose in pointSequence:
        if pose=="centralpos" or pose=="midpoint" or pose=="appBack":
            UR.movej(pointSequence[pose], acc=a, vel=v)
        else:
            UR.movel(pointSequence[pose], acc=a, vel=v)
        print("Approaching position:",pose)



    return print("Screw driver has been grabbed correctly.")    






if __name__ == "__main__":
    
    logging.basicConfig(level=logging.WARN)
    UR = urx.Robot("10.10.238.32")
    
    # Creazione di un'istanza per la glasse gripper
    gripper = Rq(UR) # L'argomento "robot" va passato perchè richiesto dalla functione __init__() 
    

    # UR.set_tcp((0,0,0,0,0,0)) # Set robot-flange to tool-tip transformation
    # UR.set_payload(0.5,(0,0,0)) # [Kg]

    try:

        l = 0.05  # [m] I guess
        v = 0.05
        a = 0.3
        
        pose = UR.getl() # Tool Center Pose of the robot
        print("TCP robot pose:", pose)

        pose[2] += l
        
        # print(UR.movej(pose,acc=a,vel=v)) # It seems to return something
        UR.movel(pose, acc=a, vel=v)


        gripper.gripper_action(0)

              



        
    finally:

        UR.close()



    
