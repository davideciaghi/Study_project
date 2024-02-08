import time

from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper as Rq
from urx.robotiq_two_finger_gripper import RobotiqScript as Rs


trasl_v = 0.1 
trasl_a = 0.1

mov_v = 0.45
mov_a = 0.2

side = [4.793690095539205e-05, -2.0387075583087366, -2.4825483004199427, -1.7656925360309046, -1.6043241659747522, -9.422937281915935]


def pistonRod(robot,gripper):
    """
    Function to take pistonRod
    """
    gr2 = Rs(robot)
    gr2._set_gripper_speed(100)
    # Back position
    back = [0.3291153013706207, -2.1772893110858362, -2.115119282399313, -1.925495449696676, -2.827756706868307, -12.502889425048622]
    robot.movej(back, acc=mov_a, vel=mov_v)
    gripper.gripper_action(120) # Open gripper
    robot.translate((0, 0.06, -0.03), acc=trasl_a, vel=trasl_v) # Reach grab pose
    gripper.gripper_action(255) # Close gripper
    robot.translate((0, 0, 0.09), acc=trasl_a, vel=trasl_v)
    robot.movej(side, acc=mov_a, vel=mov_v)
    back_insert = [-1.5708096663104456, -2.0387194792376917, -2.482476298009054, -1.7657044569598597, -1.6043599287616175, -9.422889121362957]
    robot.movej(back_insert, acc=mov_a, vel=mov_v)
    robot.translate((0, 0, 0.05), acc=trasl_a, vel=trasl_v)
    top_insert = [-1.6784303824054163, -1.9136045614825647, -1.7188680807696741, -2.654797379170553, -1.7136371771441858, -9.42985666591862]
    robot.movej(top_insert, acc=mov_a, vel=mov_v)
    robot.translate((0, 0, -0.17), acc=trasl_a, vel=trasl_v)
    gripper.gripper_action(120) # Open gripper
    robot.movej(back_insert, acc=mov_a, vel=mov_v)


def screw(robot,gripper):
    """
    Function to take the little screw
    """
    gr2 = Rs(robot)
    gripper.gripper_action(120) # Open gripper
    top = [1.0190616846084595, -1.8788850943194788, -2.3247230688678187, -2.3251574675189417, -1.6384847799884241, -9.502823718378338]
    robot.movej(top, acc=mov_a, vel=mov_v)
    robot.translate((0, 0, -0.03), acc=trasl_a, vel=trasl_v)
    gripper.gripper_action(255) # Close gripper
    robot.translate((0, 0, 0.06), acc=trasl_a, vel=trasl_v)
    robot.movej(side, acc=mov_a, vel=mov_v)
    catch_screw = [-0.8927996794330042, -2.240321938191549, -2.475175682698385, -1.4151609579669397, -1.534276310597555, -10.341869242975505]
    robot.movej(catch_screw, acc=mov_a, vel=mov_v)
    gripper.gripper_action(208) # Gripper slightly opened


def cylinder(robot, gripper):

    back = [0.38403525948524475, -2.402138058339254, -1.6658204237567347, -2.2002957502948206, -2.764996115361349, -9.402395375559124]
    robot.movej(back, acc=mov_a, vel=mov_v)
    gripper.gripper_action(0) # Open gripper
    robot.translate((0, 0.1, 0), acc=trasl_a, vel=trasl_v)
    gripper.gripper_action(255) # Close gripper
    robot.translate((0, 0, 0.03), acc=trasl_a, vel=trasl_v)
    midpoint =  [-0.8452852408038538, -2.0386717955218714, -2.4825602213488978, -1.7656925360309046, -1.6043241659747522, -9.42290128071049]
    catch_cyclinder = [-1.180812184010641, -2.3042500654803675, -1.7791197935687464, -2.093959633504049, -2.3221872488604944, -10.818015940973552]
    robot.movejs([side, midpoint, catch_cyclinder], acc=mov_a, vel=mov_v, radius=0.005)
    gripper.gripper_action(110) # Gripper slightly opened

# def top_cap(robot, gripper):

#     back = [0.9504284858703613, -2.217325035725729, -1.153661076222555, -3.7534759680377405, -2.0314329306231897, -9.918255217859539] 
#     robot.movejs([side, back], acc=mov_a, vel=mov_v, radius=0.005)
#     gripper.gripper_action(55)
#     approach = [1.0208616256713867, -2.39054519334902, -1.0861581007586878, -3.622847382222311, -1.98486835161318, -9.85932410557011]
#     robot.movej(approach, acc=mov_a, vel=mov_v)
#     gripper.gripper_action(255) # Close gripper
#     robot.translate((0, 0, 0.05), acc=trasl_a, vel=trasl_v)
#     # Punto dove prendere cap, evitare avvitatore
#     catch_cap = 
#     robot.movejs([side, catch_cap], acc=mov_a, vel=mov_v, radius=0.005)
#     gripper.gripper_action(60)

