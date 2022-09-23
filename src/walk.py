#! /usr/bin/env python3

import os
from inverse_kinematic import inverse_kinematic
import control
import rclpy
from math import pi
from time import sleep

class walk():
    def __init__(self):
        ik = inverse_kinematic(8, 6.8)
        """
        swing = 5
        drop = 20

        self.fs = ik.calc(30, 40, swing)	
        self.fd = ik.calc(30, 40, drop)		
        self.rs = ik.calc(30, 20, swing)	
        self.rd = ik.calc(30, 20, drop)		
        self.ip = ik.calc(30, 30, drop)		
        self.ll = ik.calc(30, 50, drop)
        self.ips = ik.calc(30, 30, swing)
        """
        swing = 2
        drop = 5

        self.fs = ik.calc(5, 6, swing)	
        self.fd = ik.calc(5, 6, drop)		
        self.rs = ik.calc(5, 4, swing)	
        self.rd = ik.calc(5, 4, drop)		
        self.ip = ik.calc(5, 5, drop)		
        self.ll = ik.calc(5, 7, drop)
        self.ips = ik.calc(5, 5, swing)

    def forward(self):
        movement = [
            self.ip + self.rd + self.ip + self.ip,
            self.ip + self.fs + self.ip + self.ip,
            self.ip + self.fd + self.ip + self.ip,
            self.fd + self.ip + self.fd + self.rd,
            self.fd + self.ip + self.rs + self.rd,
            self.fd + self.ip + self.rd + self.rd,
            self.fd + self.ip + self.rd + self.fs,
            self.fd + self.ip + self.rd + self.fd,
            self.ll + self.rd + self.ip + self.ip,
            self.ips + self.rd + self.ip + self.ip,
            self.ip + self.rd + self.ip + self.ip
        ]
        
        for angle in movement:   
            rclpy.init()
            action_client=control.SpyderActionClient()
            action_client.send_goal(angle, 0.5)
            rclpy.spin(action_client)

def main():
    mov = walk()
    while True:
        mov.forward()

if __name__=="__main__":
    main()
