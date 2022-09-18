#Spyderbot
A simulation of quadruped robot using ROS2 and Gazebo.  
  
this package requires ros2_control, ros2_gazebo_control, ros2_controllers and pynput to be used
  
Currently the robot only able to stand and sit.

To open the model on rviz use:
```
ros2 launch spyderbot rviz.launch.py
```
  
to run the simulation use:
```
ros2 launch spyderbot launch_sim.launch.py
```

after running the simulation we can either control the angle(in degrees) of each individual axis by using this command:
```
ros2 launch spyderbot control.launch.py ax1:=0 ax2:=0 ax3:=0 ax4:=0 ax5:=0 ax6:=0 ax7:=0 ax8:=0 ax9:=0 ax10:=0 ax11:=0 ax12:=0
``` 

or move the robot by a set of motion(currently only able to sit and stand) using this command:
```
ros2 run spyderbot teleop.py
```

