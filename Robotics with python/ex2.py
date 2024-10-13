from robot_control_class import RobotControl
rc = RobotControl(robot_name="summit")
def method(a,b,c):
    return [rc.get_laser_summit(a),rc.get_laser_summit(b),rc.get_laser_summit(c)]

print(method(0,360,719))