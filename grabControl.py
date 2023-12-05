import urx    
import logging
import time

from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper as Rq
from urx.robotiq_two_finger_gripper import RobotiqScript as Rs



class Handling():

    def __init__(self,robot):

        self.robot = robot
        self.gr = Rq(self.robot)


    def grabScrewdriver(self,v,a):
        """
        Sequence of actions to grab the screwdriver, starting from a central point
        """
        # gr._set_gripper_speed(200)
        self.gr.gripper_action(0)

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

            if pose=="openGripper" or pose=="closeGripper":
                self.gr.gripper_action(jointSequence[pose])
                print(pose)
            else:
                print("Approaching position:",pose)
                self.robot.movej(jointSequence[pose], acc=a, vel=v)
                
        print("Screw driver has been grabbed correctly.")



    def releaseScrewdriver(self,v,a):
        """
        Sequence of actions to realease the screwdriver, starting from a central point
        """
        # gr._set_gripper_speed(50)
        jointSequence = {
            "centralpos":[-0.7125352064715784, -1.9114339987384241, -1.4501970450030726, -2.9188717047320765, -0.7277739683734339, -9.428933032343181],
            "grabbedHigh2":[0.24144993722438812, -3.1574657599078577, 0.38404321670532227, -3.5075443426715296, 0.21888214349746704, -9.427242167780193],
            "grabbedHigh3":[0.24083873629570007, -3.454433266316549, 0.44026899337768555, -3.2615225950824183, 0.2194809764623642, -9.432315238306316],
            "releasePose":[0.2407548427581787, -3.476398770009176, 0.44449806213378906, -3.243415180836813, 0.21946899592876434, -9.432638772318157],
            "openGripper": 0,
            "appHigh2":[0.23586416244506836, -3.3844860235797327, 0.48784446716308594, -3.3819730917560022, 0.21454833447933197, -9.425323851892742],
            "appHigh1":[0.30100327730178833, -3.36135703722109, 0.4381599426269531, -3.3559463659869593, 0.2793298065662384, -9.424927600214275],
            "appBack":[0.40609559416770935, -3.3239977995501917, 0.35812854766845703, -3.3140061537372034, 0.3841108977794647, -9.424280532190593],
            "midpoint":[0.5760637521743774, -2.065845314656393, -1.6096809546100062, -2.592222515736715, 0.7270185351371765, -9.421797879526409],
            "centralpos":[-0.7125352064715784, -1.9114339987384241, -1.4501970450030726, -2.9188717047320765, -0.7277739683734339, -9.428933032343181]}

        for pose in jointSequence:

            if pose=="openGripper" or pose=="closeGripper":
                self.gr.gripper_action(jointSequence[pose])
                print(pose)
            else:
                print("Approaching position:",pose)
                self.robot.movej(jointSequence[pose], acc=a, vel=v)

        print("Screw driver has been released correctly.")   