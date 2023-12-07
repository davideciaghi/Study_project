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


        
        screwdriver.setSpeed("Low")
        screwdriver.tighten()
        time.sleep(5)
        screwdriver.stop()

        # gripper.grabScrewdriver(v,a)
        # gripper.releaseScrewdriver(v,a)




        # [0.054883857422612, -0.5615868095298993, 0.30497810762320915, -1.4476742030846678e-05, -2.221505493847803, 2.2212030426272915]

              
    finally:
        
        UR.close()