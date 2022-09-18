import sys
import math
from launch import LaunchDescription
import launch.actions
import launch_ros.actions

angle = []

for arg in sys.argv:
    if arg.startswith("ax1:="):
        angle.append(float(arg.split(":=")[1]))
    
    if arg.startswith("ax2:="):
        angle.append(float(arg.split(":=")[1]))

    if arg.startswith("ax3:="):
        angle.append(float(arg.split(":=")[1]))

    if arg.startswith("ax4:="):
        angle.append(float(arg.split(":=")[1]))
    
    if arg.startswith("ax5:="):
        angle.append(float(arg.split(":=")[1]))

    if arg.startswith("ax6:="):
        angle.append(float(arg.split(":=")[1]))

    if arg.startswith("ax7:="):
        angle.append(float(arg.split(":=")[1]))
    
    if arg.startswith("ax8:="):
        angle.append(float(arg.split(":=")[1]))

    if arg.startswith("ax9:="):
        angle.append(float(arg.split(":=")[1])) 

    if arg.startswith("ax10:="):
        angle.append(float(arg.split(":=")[1]))
    
    if arg.startswith("ax11:="):
        angle.append(float(arg.split(":=")[1]))

    if arg.startswith("ax12:="):
        angle.append(float(arg.split(":=")[1]))

for x in range(len(angle)):
    angle[x] = angle[x] * (math.pi/180)

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='spyderbot',
            executable='angle_control.py',
            output='screen',
            arguments=[str(angle[0]), str(angle[1]), str(angle[2]), str(angle[3]), 
                       str(angle[4]), str(angle[5]), str(angle[6]), str(angle[7]), 
                       str(angle[8]), str(angle[9]), str(angle[10]), str(angle[11])
                      ])
    ])
