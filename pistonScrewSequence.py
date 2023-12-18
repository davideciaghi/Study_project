
import time


def screw(robot,screwdriver):

    dz = 0.038 #[35 mm]     # z translation
    dx = 0.033 #[33 mm]   # x translation
    dy = 0.033 #[33 mm]   # y translation
    
    screwTime = 0.5
    approach_a=0.05     # acceleration to approach the screw
    approach_v=0.05     # speed to approach the screw
    mov_a=0.3           # accelaration to change screw
    mov_v=0.5           # speed to change screw

    centralPos=[-0.0977399984942835, -1.9357793966876429, -1.6275747458087366, -2.7103799025165003, -0.11339122453798467, -9.43454588253239]
    pistonCenter=[-0.43099671999086553, -1.223628346120016, -1.9635737578021448, -2.9373396078692835, -0.4659636656390589, -9.560112365076336]
    topLeftScrew = [-0.8720539251910608, -1.581639591847555, -1.6189454237567347, -3.080822769795553, -0.904036823903219, -9.419303782770427]

    robot.movej(centralPos, acc=mov_a, vel=mov_v)
    robot.movej(pistonCenter, acc=mov_a, vel=mov_v)
    robot.movej(topLeftScrew, acc=mov_a, vel=mov_v)

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
        screwdriver.tighten()
        print("Screwing ", i, "screw")
        time.sleep(screwTime)
        screwdriver.stop()
        robot.translate((0, 0, dz), acc=approach_a, vel=approach_v)


    robot.movej(topLeftScrew, acc=mov_a, vel=mov_v)
    robot.movej(pistonCenter, acc=mov_a, vel=mov_v)
    robot.movej(centralPos, acc=mov_a, vel=mov_v)


def unscrew(robot,screwdriver):

    dz = 0.040 #[35 mm]     # z translation
    dx = 0.033 #[33 mm]   # x translation
    dy = 0.033 #[33 mm]   # y translation
    
    screwTime = 0.5
    approach_a=0.05     # acceleration to approach the screw
    approach_v=0.05     # speed to approach the screw
    mov_a=0.3           # accelaration to change screw
    mov_v=0.5           # speed to change screw

    centralPos=[-0.0977399984942835, -1.9357793966876429, -1.6275747458087366, -2.7103799025165003, -0.11339122453798467, -9.43454588253239]
    pistonCenter=[-0.43099671999086553, -1.223628346120016, -1.9635737578021448, -2.9373396078692835, -0.4659636656390589, -9.560112365076336]
    topLeftScrew = [-0.8720539251910608, -1.581639591847555, -1.6189454237567347, -3.080822769795553, -0.904036823903219, -9.419303782770427]

    robot.movej(centralPos, acc=mov_a, vel=mov_v)
    robot.movej(pistonCenter, acc=mov_a, vel=mov_v)
    robot.movej(topLeftScrew, acc=mov_a, vel=mov_v)

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
        print("Unscrewing ", i, " screw")
        time.sleep(screwTime)
        screwdriver.stop()
        robot.translate((0, 0, dz), acc=approach_a, vel=approach_v)


    robot.movej(topLeftScrew, acc=mov_a, vel=mov_v)
    robot.movej(pistonCenter, acc=mov_a, vel=mov_v)
    robot.movej(centralPos, acc=mov_a, vel=mov_v)