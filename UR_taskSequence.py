# Import the urx and logging libraries
import urx    
import logging
import time

from screwdriverControl import Screwdriver
from grabControl import Handling



if __name__ == "__main__":
    
    logging.basicConfig(level=logging.WARN)

    UR = urx.Robot("10.10.238.32")
    gripper = Handling(UR)
    screwdriver = Screwdriver(UR)



    # robot = urx.Robot("10.10.238.32")
    # screwdriver = Screwdriver("10.10.238.32") # Istanza per a classe Screwdriver
    # gripper = Handling("10.10.238.32",robot) # Istanza per a classe Handling
    
    try:

        v = 0.5
        a = 0.3
        
        # gripper.releaseScrewdriver(v,a)
        # gripper.grabScrewdriver(v,a)
        # UR.movej(center, acc=a, vel=v)


        # screwdriver.setSpeed("Low")
        # screwdriver.tighten()
        
        # time.sleep(2)
        # screwdriver.stop()


        

        # gripper.grabScrewdriver(v,a)
        # gripper.releaseScrewdriver(v,a)




        
              
    finally:
        
        UR.close()