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
        

        mov_v = 0.300  # 0.300
        mov_a = 3.500  # 2.500


        start = time.time()
        gripper.grabScrewdriver(v=mov_v, a=mov_a)

        for x in range(0, 7):

            if pSS.screw(UR,screwdriver)==False:
                UR.close()
            else:
                pSS.unscrew(UR,screwdriver)
        
        gripper.releaseScrewdriver(v=mov_v, a=mov_a)
        stop = time.time()
        print("Elapsed time:", stop-start, "seconds")

        screwdriver.enable()







    finally:
        
        UR.close()