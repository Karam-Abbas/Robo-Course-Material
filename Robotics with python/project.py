from robot_control_class import RobotControl
import time
rc = RobotControl()
i=0
while(1):
    rc.move_straight()
    a = rc.get_laser(360)
    if a<1:
        rc.stop_robot()
        rc.rotate(270)
        rc.move_straight()

rc.stop_robot()

