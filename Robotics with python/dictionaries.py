from robot_control_class import RobotControl

rc = RobotControl()
l = rc.get_laser_full()

dict_a = {
"Position 0":l[0],
"Position 100":l[100],
"Position 200":l[200],
"Position 300":l[300],
"Position 400":l[400],
"Position 500":l[500],
"Position 600":l[600],
"Position 719":l[719]
}

print(dict_a)
