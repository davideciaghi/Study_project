import urx    
import logging
import time


if __name__ == "__main__":
    
    logging.basicConfig(level=logging.WARN)
    UR = urx.Robot("10.10.238.32")

    try:

        mov_v = 0.300
        mov_a = 2.500

        pose1 = [-0.8654330412494105, -1.5700767675982874, -1.7088359037982386, -2.9739487806903284, -0.8976915518390101, -9.436176665613445]
        UR.movej(pose1, acc=mov_a, vel=mov_v)

        pose = UR.getj()
        print("Pose1:", pose)
        
        UR.translate((0.033, 0, 0), acc=mov_a, vel=mov_v)
        pose = UR.getj()
        print("Pose2:", pose)
        time.sleep(0.5)

        UR.translate((0, -0.033, 0), acc=mov_a, vel=mov_v)
        pose = UR.getj()
        print("Pose3:", pose)
        time.sleep(0.5)

        UR.translate((-0.033, 0, 0), acc=mov_a, vel=mov_v)
        pose = UR.getj()
        print("Pose4:", pose)

        
    finally:
        UR.close()

