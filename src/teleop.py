#! /usr/bin/env python3

import os
import inverse_kinematic
import movement
import rclpy
from math import pi
from pynput import keyboard
from time import sleep
from signal import signal, SIGINT
from sys import exit

os.system("stty -echo")
ik = inverse_kinematic.inverse_kinematic(40, 40)

print(
"""
to control the robot use:
----------------
         
    q   w   e

     a  s  d

ctrl  space
----------------
w: move forward
s: move backward
a: move to left
d: move to right
q: rotate left
e: rotate right
space: stand
ctrl: sit
"""
)

def handler(signal_received, frame):
    os.system("stty echo")
    exit(0)

def on_press(key):
    try:
        k = key.char
        if(k == 'w'):
            print("forward")
            rclpy.init()
            action_client=movement.SpyderActionClient()
            l1ax1, l1ax2, l1ax3 = ik.calc(50, 50, 20)
            l2ax1, l2ax2, l2ax3 = ik.calc(40, 40, 20)
            r1ax1, r1ax2, r1ax3 = ik.calc(40, 40, 20)
            r2ax1, r2ax2, r2ax3 = ik.calc(40, 40, 20)
            future = action_client.send_goal(l1ax1, l1ax2, l1ax3, 
                                             l2ax1, l2ax2, l2ax3, 
                                             r1ax1, r1ax2, r1ax3, 
                                             r2ax1, r2ax2, r2ax3, 0.1)
            rclpy.spin(action_client)
            
            rclpy.init()
            action_client=movement.SpyderActionClient()
            l1ax1, l1ax2, l1ax3 = ik.calc(50, 50, 20)
            l2ax1, l2ax2, l2ax3 = ik.calc(40, 40, 20)
            r1ax1, r1ax2, r1ax3 = ik.calc(40, 40, 20)
            r2ax1, r2ax2, r2ax3 = ik.calc(30, 30, 20)
            future = action_client.send_goal(l1ax1, l1ax2, l1ax3, 
                                             l2ax1, l2ax2, l2ax3, 
                                             r1ax1, r1ax2, r1ax3, 
                                             r2ax1, r2ax2, r2ax3, 0.1)
            rclpy.spin(action_client)
                        
            rclpy.init()
            action_client=movement.SpyderActionClient()
            l1ax1, l1ax2, l1ax3 = ik.calc(50, 50, 20)
            l2ax1, l2ax2, l2ax3 = ik.calc(40, 40, 20)
            r1ax1, r1ax2, r1ax3 = ik.calc(50, 50, 20)
            r2ax1, r2ax2, r2ax3 = ik.calc(30, 30, 20)
            future = action_client.send_goal(l1ax1, l1ax2, l1ax3, 
                                             l2ax1, l2ax2, l2ax3, 
                                             r1ax1, r1ax2, r1ax3, 
                                             r2ax1, r2ax2, r2ax3, 0.1)
            rclpy.spin(action_client)
                       
            rclpy.init()
            action_client=movement.SpyderActionClient()
            l1ax1, l1ax2, l1ax3 = ik.calc(50, 50, 20)
            l2ax1, l2ax2, l2ax3 = ik.calc(30, 30, 20)
            r1ax1, r1ax2, r1ax3 = ik.calc(50, 50, 20)
            r2ax1, r2ax2, r2ax3 = ik.calc(30, 30, 20)
            future = action_client.send_goal(l1ax1, l1ax2, l1ax3, 
                                             l2ax1, l2ax2, l2ax3, 
                                             r1ax1, r1ax2, r1ax3, 
                                             r2ax1, r2ax2, r2ax3, 0.1)
            rclpy.spin(action_client)

            rclpy.init()
            action_client=movement.SpyderActionClient()
            l1ax1, l1ax2, l1ax3 = ik.calc(50, 50, 20)
            l2ax1, l2ax2, l2ax3 = ik.calc(40, 40, 30)
            r1ax1, r1ax2, r1ax3 = ik.calc(50, 50, 20)
            r2ax1, r2ax2, r2ax3 = ik.calc(40, 40, 30)
            future = action_client.send_goal(l1ax1, l1ax2, l1ax3, 
                                             l2ax1, l2ax2, l2ax3, 
                                             r1ax1, r1ax2, r1ax3, 
                                             r2ax1, r2ax2, r2ax3, 0.1)
            rclpy.spin(action_client)
            """           
            rclpy.init()
            action_client=movement.SpyderActionClient()
            l1ax1, l1ax2, l1ax3 = ik.calc(50, 50, 20)
            l2ax1, l2ax2, l2ax3 = ik.calc(30, 30, 20)
            r1ax1, r1ax2, r1ax3 = ik.calc(50, 50, 20)
            r2ax1, r2ax2, r2ax3 = ik.calc(30, 30, 20)
            future = action_client.send_goal(l1ax1, l1ax2, l1ax3, 
                                             l2ax1, l2ax2, l2ax3, 
                                             r1ax1, r1ax2, r1ax3, 
                                             r2ax1, r2ax2, r2ax3, 0.1)
            rclpy.spin(action_client)
            """
        if(k == 's'):
            print("backward")
        if(k == 'a'):
            print("left")
        if(k == 'd'):
            print("right")
        if(k == 'q'):
            print("rotate left")
        if(k == 'e'):
            print("rotate right")

    except AttributeError:
        pass

    except Exception as e:
        print(e.args)

def on_release(key):
    
    try:
        if(key==key.space):
            print("stand")

            rclpy.init()
            action_client=movement.SpyderActionClient()
            ax1, ax2, ax3 = ik.calc(40, 40, -20)
            future = action_client.send_goal(ax1, ax2, ax3, 
                                             ax1, ax2, ax3, 
                                             ax1, ax2, ax3, 
                                             ax1, ax2, ax3, 2)
            rclpy.spin(action_client)

            rclpy.init()
            action_client=movement.SpyderActionClient()
            ax1, ax2, ax3 = ik.calc(40, 40, 20)
            future = action_client.send_goal(ax1, ax2, ax3, 
                                             ax1, ax2, ax3, 
                                             ax1, ax2, ax3, 
                                             ax1, ax2, ax3, 2)
            rclpy.spin(action_client)

        if(key==key.ctrl):
            print("sit")

            rclpy.init()
            action_client=movement.SpyderActionClient()

            future = action_client.send_goal(0.0, 0.0, 0.0, 
                                             0.0, 0.0, 0.0, 
                                             0.0, 0.0, 0.0, 
                                             0.0, 0.0, 0.0, 1)
            rclpy.spin(action_client)

    except AttributeError:
        pass

    except Exception as e:
        print(e.args)
    
lis = keyboard.Listener(on_press=on_press, on_release=on_release)
lis.start()

while True:
    signal(SIGINT, handler)    
    sleep(0.001)
