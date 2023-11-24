# Import the urx and logging libraries
import urx    
import logging



if __name__ == "__main__":
    
    logging.basicConfig(level=logging.WARN)
    UR = urx.Robot("10.10.238.32")
    

    try:

        # Set a digital output
        UR.set_digital_out(0,True)

        # Get value of a digital input
        UR.get_digital_in(0)

              
    finally:

        UR.close()



    