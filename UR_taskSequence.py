import urx    
import logging
import time
import math

from screwdriverControl import Screwdriver
from grabControl import Handling

import pistonAssemblySequence as pAS
import pistonScrewSequence as pSS

from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper as Rq



def detectForce(robot):
        force = robot.get_tcp_force()
        module1 = abs(math.sqrt(force[0]**2 + force[1]**2 + force[2]**2))
        while True:
            force = robot.get_tcp_force()
            module2 = abs(math.sqrt(force[0]**2 + force[1]**2 + force[2]**2))
            if module2 > module1*1.3:
                print("Force detected")
                break
            time.sleep(0.5)
        
        return True



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

        if pSS.screw(UR,screwdriver)==False:
            UR.close()
        else:
            pSS.unscrew(UR,screwdriver)
            gripper.releaseScrewdriver(v=mov_v, a=mov_a)
             
        stop = time.time()
        print("Elapsed time:", stop-start, "seconds")

        screwdriver.enable()



        # Tempo persona avvitamento senso orario: 11/12 s
        # Tempo persona avvitamento incorciato: 20.31 s
        
        # Tempi con velocità 300mm/s e accelerazione 2500mm/s^2
        # 1° Tempo: 37.2 s
        # 2° Tempo: 36.8 s
        # 3° Tempo: 34.2 s
        # 4° Tempo: 33.2 s
        # 5° Tempo: 33.7 s
        # 6° Tempo: 33.4 s



        # Tempi con velocità 500mm/s e accelerazione 1500mm/s^2
        # 1° Tempo: 35 s
        # 2° Tempo: 33 s
        # 3° Tempo: 31 s
        # 4° Tempo: 30 s
        # 5° Tempo: 29 s
        # 6° Tempo: 27 s con diminuzione tempo gripper
        # 7° Tempo: 24.84 s con tolto un waypoint
        # 8° Tempo: 23.53 s accelerando le traslazioni 
        # 9° Tempo: 23.33 s accelerando le traslazioni

    


        # Tempi con velocità 300mm/s e accelerazione 3500mm/s^2
        # Tempo 1: 38.2 s
        # Tempo 2: 42.83 s
        # Tempo 3: 31.77 s
        # Tempo 4: 23.6 s
        # Tempo 5: 24.33 s
        # Tempo 6: 22.5 s


        # Tempi con velocità 300mm/s e accelerazione 3500mm/s^2




        # pAS.pistonRod(UR,gr)
        # pAS.screw(UR,gr)
        
        # if detectForce(UR) == True:
        #     pAS.cylinder(UR,gr)

        # if detectForce(UR) == True:
        #     pAS.top_cap(UR, gr)





    finally:
        
        UR.close()