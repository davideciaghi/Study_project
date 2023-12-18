# Import the urx and logging libraries
import urx    
import logging
import time

from screwdriverControl import Screwdriver
from grabControl import Handling

import pistonScrewSequence as pSS



if __name__ == "__main__":
    
    logging.basicConfig(level=logging.WARN)

    UR = urx.Robot("10.10.238.32") # Istanza per robot
    gripper = Handling(UR) # Istanza per afferrare l'avvitatore
    screwdriver = Screwdriver(UR) # Istanza per avvitatore


    try:

        v = 0.5
        a = 0.3
        
        pSS.screw(UR,screwdriver)
        pSS.unscrew(UR,screwdriver)

        # gripper.grabScrewdriver(v,a)
        # gripper.releaseScrewdriver(v,a)



    finally:
        
        UR.close()