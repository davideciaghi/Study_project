# Import the urx and logging libraries
import urx    
import logging
import time



if __name__ == "__main__":
    
    logging.basicConfig(level=logging.WARN)
    UR = urx.Robot("10.10.238.32")
    

    try:

        UR.set_digital_out(2,True) # Disable emergency input if HIGH
        UR.set_digital_out(0,False) # Disable STOP Motor
        # Set a digital output
        UR.set_digital_out(1,True) # DO1 - Tightening
        time.sleep(2) # Wait 2 seconds
        UR.set_digital_out(1,False) # DO2 - Stop tightening(?)
        time.sleep(2)
        UR.set_digital_out(0,True) # Enable STOP Motor



        # Get value of a digital input
        # print(UR.get_digital_in(0))

              
    finally:

        UR.close()



    