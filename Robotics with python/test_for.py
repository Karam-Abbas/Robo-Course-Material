from robot_control_class import RobotControl

rc = RobotControl()

l = rc.get_laser_full()
a = 0
for point in l:
    if point>a:
        a = point
    
print("Highest value:",a)