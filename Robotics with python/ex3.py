from robot_control_class import RobotControl
rc= RobotControl(robot_name="summit")

mov_A = rc.move_straight_time("forward",0.3,4)
print(mov_A)

mov_B = rc.turn("counter-clockwise",0.3,8)
print(mov_B)

mov_A = rc.move_straight_time("forward",0.3,7)
print(mov_A)
mov_B = rc.turn("counter-clockwise",0.3,8)
print(mov_B)
mov_A = rc.move_straight_time("forward",0.3,5)
print(mov_A)

