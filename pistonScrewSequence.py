import time

# Center screw offset in x and y
dx = 0.033  #[33 mm]
dy = 0.033  #[33 mm]

# Speeds and accelerations to apprach the head of the screw
approach_v = 0.300      # speed to approach the screw
approach_a = 2.500      # acceleration to approach the screw

# Speeds and accelerations to move from one screw to the other
mov_v = 0.300       # speed to change screw
mov_a = 3.500       # accelaration to change screw

# Sequence of Top screws' positions
screw_1 = [-0.7550748030291956, -1.610223118458883, -1.668037239705221, -2.971201244984762, -0.7872861067401331, -9.440565474817546]
screw_2 = [-0.9539592901812952, -1.7175362745868128, -1.549096409474508, -2.988899532948629, -0.9858043829547327, -9.432098992655071]
screw_3 = [-0.8659003416644495, -1.5699446837054651, -1.7088483015643519, -2.973780934010641, -0.8979075590716761, -9.436392434427532]
screw_4 = [-0.8515222708331507, -1.7539742628680628, -1.5071013609515589, -2.9929783979998987, -0.8833239714251917, -9.43558872539738]

sequence = {"topRight":screw_1,
                "bottomLeft":[screw_4,screw_2],
                "topLeft":screw_3,
                "bottomRight":[screw_1,screw_4]}

def screw(robot,screwdriver):

    dz_1 = 0.030            #[30 mm]     # Distanza per puntare la vite
    dz_2 = 0.036            #[36 mm]     # Distanza per fissare la vite
    screw_offset = 0.003    #[3 mm]      # Distance lower while screwing
    screwTime = 0.37        #[0.37 s]
    error = False                        # Flag variable to control free spinning

    # for cycle per impuntare le viti
    for i in sequence:

        if len(sequence[i])==2:
            robot.movejs(sequence[i], acc=mov_a, vel=mov_v, radius=0.004)
        else:
            robot.movej(sequence[i], acc=mov_a, vel=mov_v)

        robot.translate((0, 0, -dz_1), acc=approach_a, vel=approach_v) # Lower the bit to catch the head
        screwdriver.enable()
        screwdriver.tighten() # Start screwing
        time.sleep(screwTime) # Screw for 0.33 seconds
        screwdriver.stop()
        robot.translate((0, 0, 0.01), acc=approach_a, vel=approach_v) # Lift the bit to exit the head
        
    print("Screws almost fixed.")
        
    
    # for cycle per fissare le viti
    for i in sequence:
        
        if len(sequence[i])==2:
            robot.movejs(sequence[i], acc=mov_a, vel=mov_v, radius=0.007)
        else:
            robot.movej(sequence[i], acc=mov_a, vel=mov_v)

        robot.translate((0, 0, -dz_2), acc=approach_a, vel=approach_v) # Lower the bit to catch the head
        screwdriver.enable()
        screwdriver.tighten() # Start screwing

        start = time.time()
        robot.translate((0, 0, -screw_offset), acc=0.2, vel=0.1) # Lowering while fastening
        

        while screwdriver.clutch()==False and error==False:  # Control if the clutch is triggered
            time.sleep(0.05)
            
            stop = time.time()
            if (stop-start)>=4:
                print("Error, screw not fastened correctly, ")
                error = True
                break # exits from the while loop
        
        screwdriver.stop()
        robot.translate((0, 0, dz_2+screw_offset), acc=approach_a, vel=approach_v) # Elevate the tip

        if error==True:
            break # Break the main for loop


    if error==True:
        print("Screwing activity aborted.")
        return False
    else:
        return True


def unscrew(robot,screwdriver):

    dz = 0.041              #[41 mm]    # Distanza per entrare nela vite
    unscrew_offset = 0.008  #[8 mm]
    unscrewTime = 0.17      #[0.17 s]

    for i in sequence:

        if len(sequence[i])==2:
            robot.movejs(sequence[i], acc=mov_a, vel=mov_v, radius=0.004)
        else:
            robot.movej(sequence[i], acc=mov_a, vel=mov_v)

        robot.translate((0, 0, -dz), acc=approach_a, vel=approach_v) # Lower the bit to catch the head
        screwdriver.enable()
        screwdriver.untighten() # Start screwing
        robot.translate((0, 0, unscrew_offset), acc=0.400, vel=0.100) # Lifting while fastening
        time.sleep(unscrewTime) # Unfastening time
        screwdriver.stop()
        robot.translate((0, 0, 0.014), acc=approach_a, vel=approach_v) # Lift the bit to exit the head


        















# import time

# dx = 0.033 #[33 mm]   # x translation
# dy = 0.033 #[33 mm]   # y translation


# # Speeds and accelerations
# approach_v = 0.200     # speed to approach the screw
# approach_a = 0.800     # acceleration to approach the screw
# mov_v = 0.300 # prima 500         # speed to change screw
# mov_a = 1.200          # accelaration to change screw

# topLeftScrew = [-0.8581069151507776, -1.5621841589557093, -1.71669847169985, -2.973913017903463, -0.8904836813556116, -9.436416514704021]

# def screw(robot,screwdriver):

#     dz = 0.035            #[35 mm]     # z translation
#     screw_offset = 0.004  #[4 mm]

#     robot.movej(topLeftScrew, acc=mov_a, vel=mov_v)

#     translations = {"topLeft":[0,0,0],
#                     "topRight":[dx,0,0],
#                     "bottomRight":[0,-dy,0],
#                     "bottomLeft":[-dx,0,0]}


#     for i in translations:

#         x_trans = translations[i][0]
#         y_trans = translations[i][1]
#         z_trans = translations[i][2]

#         robot.translate((x_trans, y_trans, z_trans), acc=mov_a, vel=mov_v) # Move on the screw
#         robot.translate((0, 0, -dz), acc=approach_a, vel=approach_v) # Lower the tip
#         screwdriver.enable()
#         screwdriver.tighten() # Start screwing
#         print("Screwing ", i, " screw")

#         start = time.time()

#         robot.translate((0, 0, -screw_offset), acc=0.2, vel=0.1) # Lowering while fastening
        
        
#         error = False

#         while screwdriver.clutch()==False and error==False:  # Control if the clutch is triggered
#             time.sleep(0.05)
            
#             stop = time.time()
#             if (stop-start)>=4:
#                 screwdriver.stop()
#                 print("Error, screw not fastened correctly, ")
#                 error = True
#                 break # exits from the while loop
        
#         if error==False:

#             screwdriver.stop() # Stop screwdriver
#             robot.translate((0, 0, dz+screw_offset), acc=approach_a, vel=approach_v) # Elevate the tip
        
#         else:
#             robot.translate((0, 0, dz+screw_offset), acc=approach_a, vel=approach_v) # Elevate the tip
#             break # Break the main for loop

#     if error==True:
#         print("Screwing activity aborted.")
#         return False
#     else:
#         return True


# def unscrew(robot,screwdriver):

#     dz = 0.045             #[45 mm]     # z translation
#     unscrew_offset = 0.009 #[9 mm]
#     unscrewTime = 0.2

#     robot.movej(topLeftScrew, acc=mov_a, vel=mov_v)

#     translations = {"topLeft":[0,0,0],
#                     "topRight":[dx,0,0],
#                     "bottomRight":[0,-dy,0],
#                     "bottomLeft":[-dx,0,0]}

#     for i in translations:

#         x_trans = translations[i][0]
#         y_trans = translations[i][1]
#         z_trans = translations[i][2]

#         robot.translate((x_trans, y_trans, z_trans), acc=mov_a, vel=mov_v)
#         robot.translate((0, 0, -dz), acc=approach_a, vel=approach_v)
#         screwdriver.enable()
#         screwdriver.untighten()
#         print("Unscrewing ", i, " screw")
#         robot.translate((0, 0, unscrew_offset), acc=1.500, vel=0.200) # Lifting while fastening
#         time.sleep(unscrewTime)
#         screwdriver.stop()
#         robot.translate((0, 0, dz-unscrew_offset), acc=approach_a, vel=approach_v)

