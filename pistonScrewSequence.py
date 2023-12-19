
import time

dx = 0.033 #[33 mm]   # x translation
dy = 0.033 #[33 mm]   # y translation
unscrewTime = 0.3
approach_a=0.05     # acceleration to approach the screw
approach_v=0.05     # speed to approach the screw
mov_a=0.3           # accelaration to change screw
mov_v=0.5           # speed to change screw



def screw(robot,screwdriver):

    dz = 0.042 #[35 mm]     # z translation
    offset=0.002 #[1.5 mm]

    centralPos=[-0.0977399984942835, -1.9357793966876429, -1.6275747458087366, -2.7103799025165003, -0.11339122453798467, -9.43454588253239]
    pistonCenter=[-0.43099671999086553, -1.223628346120016, -1.9635737578021448, -2.9373396078692835, -0.4659636656390589, -9.560112365076336]
    topLeftScrew = [-0.8720539251910608, -1.581639591847555, -1.6189454237567347, -3.080822769795553, -0.904036823903219, -9.419303782770427]

    robot.movejs([centralPos,pistonCenter,topLeftScrew], acc=mov_a, vel=mov_v, radius=0.025)

    translations = {"topLeft":[0,0,0],
                    "topRight":[dx,0,0],
                    "bottomRight":[0,-dy,0],
                    "bottomLeft":[-dx,0,0]}

    for i in translations:

        x_trans = translations[i][0]
        y_trans = translations[i][1]
        z_trans = translations[i][2]

        robot.translate((x_trans, y_trans, z_trans), acc=mov_a, vel=mov_v) # Move on the screw
        robot.translate((0, 0, -dz), acc=approach_a, vel=approach_v) # Lower the tip
        screwdriver.tighten() # Start screwing
        robot.translate((0,0,-offset), acc=0.02, vel=0.01) # Lowering while fastening
        print("Screwing ", i, " screw")
        while robot.get_digital_in(2)==False:  # Control if the clutch is triggered
            time.sleep(0.1)
        screwdriver.stop() # Stop screwdriver
        robot.translate((0, 0, dz+offset), acc=approach_a, vel=approach_v) # Elevate the tip


    robot.movejs([topLeftScrew,pistonCenter,centralPos], acc=mov_a, vel=mov_v, radius=0.025)

    


def unscrew(robot,screwdriver):

    dz = 0.045 #[35 mm]     # z translation
    offset=0.005 #[2mm]

    centralPos=[-0.0977399984942835, -1.9357793966876429, -1.6275747458087366, -2.7103799025165003, -0.11339122453798467, -9.43454588253239]
    pistonCenter=[-0.43099671999086553, -1.223628346120016, -1.9635737578021448, -2.9373396078692835, -0.4659636656390589, -9.560112365076336]
    topLeftScrew = [-0.8720539251910608, -1.581639591847555, -1.6189454237567347, -3.080822769795553, -0.904036823903219, -9.419303782770427]

    robot.movejs([centralPos,pistonCenter,topLeftScrew], acc=mov_a, vel=mov_v, radius=0.02)

    translations = {"topLeft":[0,0,0],
                    "topRight":[dx,0,0],
                    "bottomRight":[0,-dy,0],
                    "bottomLeft":[-dx,0,0]}

    for i in translations:

        x_trans = translations[i][0]
        y_trans = translations[i][1]
        z_trans = translations[i][2]

        robot.translate((x_trans, y_trans, z_trans), acc=mov_a, vel=mov_v)
        robot.translate((0, 0, -dz), acc=approach_a, vel=approach_v)
        screwdriver.untighten()
        robot.translate((0,0,offset), acc=0.05, vel=0.05) # Lowering while fastening
        print("Unscrewing ", i, " screw")
        # time.sleep(unscrewTime)
        screwdriver.stop()
        robot.translate((0, 0, dz-offset), acc=approach_a, vel=approach_v)


    robot.movejs([topLeftScrew,pistonCenter,centralPos], acc=mov_a, vel=mov_v, radius=0.02)