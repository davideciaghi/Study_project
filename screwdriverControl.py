import urx
import logging
import time



class Screwdriver():

    def __init__(self,robot):
        
        self.robot = robot
 
        self.robot.set_digital_out(2,True) # Disable emergency input
        self.robot.set_digital_out(0,False) # Disable STOP Motor
        

    def tighten(self):
        """
        Screwdriver tighten1
        """
        if self.robot.get_digital_in(0)==0:

            print("Start tightening")
            self.robot.set_digital_out(1,True) # DO1 - Tightening

    
    def untighten(self):
        """
        Screwdriver untighten
        """
        if self.robot.get_digital_in(0)==0:

            print("Start tightening")
            self.robot.set_digital_out(3,True) # DO3 - Untighten
        

    def stop(self):
        """
        Stop the robot
        """
        print("Stopping screwdriver")
        self.robot.set_digital_out(2,False) # Emergency input enabled
        self.robot.set_digital_out(0,True)  # Enable STOP Motor
        self.robot.set_digital_out(1,False) # DO1 - Tightening
        self.robot.set_digital_out(3,False) # DO3 - Untighten


