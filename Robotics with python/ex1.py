from robot_control_class import RobotControl
import time

rc = RobotControl(robot_name="summit")
def move_robo(num =0):
    rc.move_straight()
    time.sleep(num)
    rc.stop_robot()

move_robo(5)