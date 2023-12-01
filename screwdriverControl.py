# Import the urx and logging libraries
import urx    
import logging
import time

# logging.basicConfig(level=logging.WARN)
# UR = urx.Robot("10.10.238.32")


class Screwdriver(object):

    def __init__(self, robot):
        
        self.robot = robot

        self.robot.set_digital_out(2,True) # Disable emergency input
        self.robot.set_digital_out(0,False) # Disable STOP Motor


    def tighten(self):
        """
        Screwdriver tighten
        """
        if self.robot.get_digital_in(0)==1:

            print("Start tightening")
            self.robot.set_digital_out(1,True) # DO1 - Tightening

    
    def untighten(self):
        """
        Screwdriver untighten
        """
        if self.robot.get_digital_in(0)==1:

            print("Start tightening")
            self.robot.set_digital_out(3,True) # DO3 - Untighten
        

    def stop(self):

        print("Stopping screwdriver")
        self.robot.set_digital_out(2,False) # Emergency input enabled
        self.robot.set_digital_out(0,True)  # Enable STOP Motor
        self.robot.set_digital_out(1,False) # DO1 - Tightening
        self.robot.set_digital_out(3,False) # DO3 - Untighten


