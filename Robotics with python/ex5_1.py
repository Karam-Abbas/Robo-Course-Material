from robot_control_class import RobotControl

rc = RobotControl(robot_name="summit")

class robo_motion:
    def __init__(self,motion,rotation_direction,speed,time,square_Size=1):
        self.motion=motion
        self.rotation_direction=rotation_direction
        self.speed=speed
        self.time=time
        self.square_Size=square_Size
    
    def make_square(self,r_c):
        for i in range(2):
            r_c.move_straight_time(self.motion,self.speed,self.time*self.square_Size)
            r_c.turn(self.rotation_direction,self.speed,self.time*self.square_Size)
        

    def set_square_size(self,num):
        self.square_Size = num

rc.move_straight_time("forward",0.5,4)
print("start\n")
rm = robo_motion("forward","clockwise",0.3,3)
rm.make_square(r_c=rc)
print("motion 1 done")
rm.set_square_size(2)
rm.make_square(r_c=rc)
print("motion 2 done")


