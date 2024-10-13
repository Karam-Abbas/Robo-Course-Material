from robot_control_class import RobotControl

rc = RobotControl()

num = int(input("enter angle:"))

a = rc.get_laser(num)

print("Your ans:",a)