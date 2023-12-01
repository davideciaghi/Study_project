# Import the urx and logging libraries
import urx    
import logging

from screwdriverControl import Screwdriver
from grabControl import Handling



if __name__ == "__main__":
    
    logging.basicConfig(level=logging.WARN)
    
    UR = urx.Robot("10.10.238.32") # Istanza per a classe Robot
    

    try:

        v = 0.5
        a = 0.3

        Handling.grabScrewdriver(v,a,UR)
        Screwdriver.untighten(UR)
        Handling.releaseScrewdriver(v,a,UR)


        #pose = UR.getl() # Tool Center Pose of the robot

        #joints = UR.getj()
        #print(joints)

        # UR.movel(pose, acc=a, vel=v)

        #UR.movej(posej2, acc=a, vel=v)

              
    finally:

        UR.close()