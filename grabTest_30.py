import urx    
import logging
import time
import math

from screwdriverControl import Screwdriver
from grabControl import Handling

import pistonAssemblySequence as pAS
import pistonScrewSequence as pSS

from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper as Rq



if __name__ == "__main__":
    
    logging.basicConfig(level=logging.WARN)

    UR = urx.Robot("10.10.238.32",use_rt=True,urFirm=5.1) # Istanza per robot
    gripper = Handling(UR) # Istanza per afferrare l'avvitatore
    screwdriver = Screwdriver(UR) # Istanza per avvitatore

    gr = Rq(UR)


    try:
        

        mov_v = 0.500
        mov_a = 2.500
        
        for x in range (0, 30):

            gripper.grabScrewdriver(v=mov_v, a=mov_a)
            UR.translate((-0.10, 0, 0.10), acc=mov_a, vel=mov_v) # Move in casual position
            gripper.releaseScrewdriver(v=mov_v, a=mov_a)
            time.sleep(0.5)


    finally:
        
        UR.close()