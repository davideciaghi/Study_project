
import time

# import urx
# import screwdriverControl as sC


def screw(robot,screwdriver):

    z_trans = 0.025  #[25mm]     # z translation
    x_trans = 0.0328 #[32.8mm]   # x translation
    y_trans = 0.0328 #[32.8mm]   # y translation
    screwTime = 0.5
    approach_a=0.05     # acceleration to approach the screw
    approach_v=0.05     # speed to approach the screw
    mov_a=0.3           # accelaration to change screw
    mov_v=0.5           # speed to change screw


    centralPos=[-0.7125352064715784, -1.9114339987384241, -1.4501970450030726, -2.9188717047320765, -0.7277739683734339, -9.428933032343181]
    pistonCenter=[-0.9217456022845667, -1.8078010717975062, -1.2727444807635706, -3.1993778387652796, -0.9343703428851526, -9.431319840738567]
    topLeftScrew = [-0.9469202200519007, -1.6808937231646937, -1.5996974150287073, -2.9231680075274866, -0.9795783201800745, -9.462740548441204]

    robot.movej(pistonCenter, acc=mov_a, vel=mov_v)
    robot.movej(centralPos, acc=mov_a, vel=mov_v)
    robot.movej(pistonCenter, acc=mov_a, vel=mov_v)
    robot.movej(topLeftScrew, acc=mov_a, vel=mov_v)

    robot.translate((0, 0, -z_trans), acc=approach_a, vel=approach_v)
    screwdriver.tighten()
    time.sleep(screwTime)
    screwdriver.stop()
    robot.translate((0, 0, z_trans), acc=approach_a, vel=approach_v)


    robot.translate((x_trans, 0, 0), acc=mov_a, vel=mov_v)
    robot.translate((0, 0, -z_trans), acc=approach_a, vel=approach_v)
    screwdriver.tighten()
    time.sleep(screwTime)
    screwdriver.stop()
    robot.translate((0, 0, z_trans), acc=approach_a, vel=approach_v)


    robot.translate((0, -y_trans, 0), acc=mov_a, vel=mov_v)
    robot.translate((0, 0, -z_trans), acc=approach_a, vel=approach_v)
    screwdriver.tighten()
    time.sleep(screwTime)
    screwdriver.stop()
    robot.translate((0, 0, z_trans), acc=approach_a, vel=approach_v)


    robot.translate((-x_trans, 0, 0), acc=mov_a, vel=mov_v)
    robot.translate((0, 0, -z_trans), acc=approach_a, vel=approach_v)
    screwdriver.tighten()
    time.sleep(screwTime)
    screwdriver.stop()
    robot.translate((0, 0, z_trans), acc=approach_a, vel=approach_v)

    robot.movej(centralPos, acc=mov_a, vel=mov_v)