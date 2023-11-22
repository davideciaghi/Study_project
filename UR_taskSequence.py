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

        grabScrewdriver()

        
        

    finally:
        UR.close()




    def grabScrewdriver():

        dz = 0.01 #[1 cm]
        v = 0.05
        a = 0.3

        pose = UR.getl()

        pose[2] += dz   # Elevate z by dz

        pointSequence = {"centralpos":[],
                  "openGripper": 2,
                  "midpoint":[],
                  "backpoint":[],
                  "high":[],
                  "low":[],
                  "closeGripper": 5,
                  "elevate":[]}

        for pose in pointSequence:
            
            if pose=="centralpos" or pose=="midpoint" or pose=="backpoint":
                UR.movej(pointSequence[pose], acc=a, vel=v)
            else:
                UR.movel(pointSequence[pose], acc=a, vel=v)
            
            print("Approaching position:",pose)

        return print("Screw driver has been grabbed correctly.")
