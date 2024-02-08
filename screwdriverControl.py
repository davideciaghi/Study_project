import urx
import logging
import time

from timeit import default_timer as timer



class Screwdriver():

    

    def __init__(self,robot):
        
        self.robot = robot
        self.robot.set_digital_out(2,True) # Emergency input disabled
        self.robot.set_digital_out(0,True) # Enable STOP Motor
        self.screwdriver_state = False
        
        
    def emergency(self):
        """
        Eneable the emergency stop in case of faults
        """
        self.robot.set_digital_out(2,False) # Emergency input enabled

    def stop(self):
        """
        Stops the screwdriver
        """
        self.robot.set_digital_out(0,True)  # Enable STOP Motor
        self.robot.set_digital_out(1,False) # DO1 - Tightening
        self.robot.set_digital_out(3,False) # DO3 - Untighten
        self.screwdriver_state = False
        print("Screwdriver stopped")

    def enable(self):
        """
        Enables the screwdriver
        """
        self.robot.set_digital_out(0,False) # Disable STOP Motor
        self.robot.set_digital_out(2,True) # Emergency input disabled
        self.screwdriver_state = True
        print("Screwdriver enabled")


    def tighten(self):
        """
        Screwdriver tighten
        """
        if self.robot.get_digital_in(0)==0 and self.screwdriver_state==True:
            print("Start tightening")
            self.robot.set_digital_out(1,True) # DO1 - Tightening
        elif self.screwdriver_state==False:
            print("Screwdriver is not activated")
    

    def untighten(self):
        """
        Screwdriver untighten
        """
        if self.robot.get_digital_in(0)==0 and self.screwdriver_state==True:
            print("Start untightening")
            self.robot.set_digital_out(3,True) # DO3 - Untighten
        elif self.screwdriver_state==False:
            print("Screwdriver is not activated")


    def clutch(self):
        """
        It returns True if the clutch is triggered, False otherwise
        """
        if self.robot.get_digital_in(2)==True: # DI2 - Clutch trigger
            print("Clutch triggered")
            return True
        else:
            return False


    


    def setSpeed(self,flag):
        """
        Set the speed to HIGH or LOW
        """
        if flag=="Low":
            self.robot.set_digital_out(4,True) # Set speed LOW
            print("Set speed to LOW")
        elif flag=="High":
            self.robot.set_digital_out(4,False) # Set speed HIGH
            print("Set speed to HIGH")


