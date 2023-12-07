import urx    
import logging


if __name__ == "__main__":
    
    logging.basicConfig(level=logging.WARN)
    UR = urx.Robot("10.10.238.32")

    try:

        pose = UR.getj()

        # pose = UR.getl() # Tool Center Pose of the robot
        print("TCP robot pose:", pose)

        
    finally:
        UR.close()

