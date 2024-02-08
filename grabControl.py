import urx    
import logging
import time

from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper as Rq
from urx.robotiq_two_finger_gripper import RobotiqScript as Rs


class Handling():

    def __init__(self,robot):

        # Istances
        self.robot = robot
        self.gr = Rq(self.robot)
        self.gr2 = Rs()

        # Positions (only position to set -> back e top)
        self.center = [-0.11641914049257451, -1.3727925459491175, -1.8117697874652308, -3.11692983308901, -0.15058595338930303, -9.388534196207317]
        self.top = [-0.250190560017721, -2.183692280446188, -1.221069637929098, -2.7701953093158167, -0.2605660597430628, -9.50395096142033]
        self.middle = [0.15335127711296082, -1.8405798117267054, -1.8547752539264124, -2.511691395436422, 0.44445034861564636, -9.45027960140446]
        self.back = [-0.011515442525045216, -2.1941121260272425, -1.9637892881976526, -1.2956550757037562, -0.03163034120668584, -10.228317864725383]

        # Distances for translations
        self.z_trans = 0.10  #[10 cm]
        self.y_trans = 0.08  #[8 cm]
        
        # Speed and acceleration for translations
        self.mov_v = 0.300 # prima 150
        self.mov_a = 1.200

    def grabScrewdriver(self,v,a):
        """
        Sequence of actions to grab the screwdriver, starting from a central point
        """        
        self.gr2._set_gripper_speed(100)
        print("Going to grab the screwdriver")
        self.gr.gripper_action(0) # Open gripper
        # self.robot.movejs([self.center, self.middle, self.back], acc=a, vel=v, radius=0.10) # Approach back
        self.robot.movej(self.back, acc=a, vel=v)
        self.robot.translate((0, -self.y_trans, 0), acc=self.mov_a, vel=self.mov_v) # Reach grab pose
        self.gr.gripper_action(255) # Close gripper
        self.robot.translate((0, 0, self.z_trans), acc=self.mov_a, vel=self.mov_v) # Lift the screwdriver
        print("Screw driver has been grabbed correctly.")


    def releaseScrewdriver(self,v,a):
        """
        Sequence of actions to realease the screwdriver, starting from a central point
        """
        self.gr2._set_gripper_speed(200)
        print("Going to release the screwdriver")
        self.robot.movej(self.top, acc=a, vel=v) # Approach top
        self.robot.translate((0, 0, -self.z_trans), acc=self.mov_a, vel=self.mov_v) # Low the screwdriver to release pose
        self.gr.gripper_action(0) # Open gripper
        self.robot.translate((0, self.y_trans, 0), acc=self.mov_a, vel=self.mov_v) # Back pose
        # self.robot.movejs([self.middle, self.center], acc=a, vel=v, radius=0.03) # Approach center pose
        print("Screw driver has been released correctly.")