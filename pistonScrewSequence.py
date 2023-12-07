        
z_trans = 0.025  #[25mm]
x_trans = 0.0328 #[32.8mm]
y_trans = 0.0328 #[32.8mm]

central=[-0.7125352064715784, -1.9114339987384241, -1.4501970450030726, -2.9188717047320765, -0.7277739683734339, -9.428933032343181]
center=[-0.9217456022845667, -1.8078010717975062, -1.2727444807635706, -3.1993778387652796, -0.9343703428851526, -9.431319840738567]
poseH = [-0.9469202200519007, -1.6808937231646937, -1.5996974150287073, -2.9231680075274866, -0.9795783201800745, -9.462740548441204]

UR.movej(center, acc=a, vel=v)
UR.movej(central, acc=a, vel=v)
UR.movej(center, acc=a, vel=v)
UR.movej(poseH, acc=a, vel=v)

UR.translate((0, 0, -z_trans), acc=0.05, vel=0.05)
screwdriver.tighten()
time.sleep(0.5)
screwdriver.stop()
UR.translate((0, 0, z_trans), acc=0.05, vel=0.05)


UR.translate((x_trans, 0, 0), acc=0.05, vel=0.05)
UR.translate((0, 0, -z_trans), acc=0.05, vel=0.05)
screwdriver.tighten()
time.sleep(0.5)
screwdriver.stop()
UR.translate((0, 0, z_trans), acc=0.05, vel=0.05)


UR.translate((0, -y_trans, 0), acc=0.05, vel=0.05)
UR.translate((0, 0, -z_trans), acc=0.05, vel=0.05)
screwdriver.tighten()
time.sleep(0.5)
screwdriver.stop()
UR.translate((0, 0, z_trans), acc=0.05, vel=0.05)


UR.translate((-x_trans, 0, 0), acc=0.05, vel=0.05)
UR.translate((0, 0, -z_trans), acc=0.05, vel=0.05)
screwdriver.tighten()
time.sleep(0.5)
screwdriver.stop()
UR.translate((0, 0, z_trans), acc=0.05, vel=0.05)