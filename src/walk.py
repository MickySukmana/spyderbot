#! /usr/bin/env python3

import os
from inverse_kinematic import inverse_kinematic
import control
import rclpy
from math import pi
from time import sleep

class walk():
    def __init__(self):
        ik = inverse_kinematic(40, 40)

        self.fs = ik.calc(30, 40, 5)	#move front leg 10cm forward
        self.fd = ik.calc(30, 40, 20)	#drop front leg
        self.rs = ik.calc(30, 20, 5)	#move rear leg 10cm forward
        self.rd = ik.calc(30, 20, 20)	#drop rear leg
        self.ip = ik.calc(30, 30, 20)	#return to initial position

    def forward(self):
        movement = [
            self.ip + self.ip + self.ip + self.ip,
            self.ip + self.fs + self.ip + self.ip,
            self.ip + self.fd + self.rs + self.ip,
            self.ip + self.fd + self.rd + self.ip,
        ]
        
        for angle in movement:   
            rclpy.init()
            action_client=control.SpyderActionClient()
            action_client.send_goal(angle, 1)
            rclpy.spin(action_client)

def main():
    mov = walk()
    mov.forward()

if __name__=="__main__":
    main()
