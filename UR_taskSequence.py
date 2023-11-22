# Import the urx and logging libraries
import urx    
import logging 


if __name__ == "__main__":
    
    logging.baseConfig(level=logging.WARN)
    UR = urx.Robot("")

    UR.set_tcp((0,0,0,0,0,0)) # Set robot-flange to tool-tip transformation
    UR.set_payload(0.5,(0,0,0)) # [Kg]

    try:

        l = 0.05  # [m] I guess
        v = 0.05
        a = 0.3
        
        pose = UR.getl() # Tool Center Pose of the robot
        print("TCP robot pose:", pose)

        pose[2] += l
        
       
        print(UR.movej(pose,acc=a,vel=v)) # It seems to return something

        UR.movel(pose, acc=a, vel=v)



    finally:
        UR.close()