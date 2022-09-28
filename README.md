# Spyderbot
Work in progress.  
  
A simulation of quadruped robot using ROS2 and Gazebo.  
  
this package requires ros2_control, ros2_gazebo_control and ros2_controllers to be used

## Launching simulation  
To open the model on rviz use:
```
ros2 launch spyderbot rviz.launch.py
```
  
to run the simulation use:
```
ros2 launch spyderbot launch_sim.launch.py
```

## control
after running the simulation we can either control the angle(in degrees) of each individual axis by using this command:
```
ros2 launch spyderbot angle_control.launch.py ax1:=0 ax2:=0 ax3:=0 ax4:=0 ax5:=0 ax6:=0 ax7:=0 ax8:=0 ax9:=0 ax10:=0 ax11:=0 ax12:=0
```

or you can make the robot walk forward by using this command:
```
ros2 run spyderbot walk.py
```  
although there's still an issue that the robot just walk in place without moving forward. currently trying to fix it  
28 sep 2022. the robot is now able to move slightly forward from adjusting the controllers gain.

## Custom model
![alt text](https://github.com/MickySukmana/spyderbot/blob/main/img/custom_model.png?raw=true)  
![alt text](https://github.com/MickySukmana/spyderbot/blob/main/img/custom_model.gif?raw=true)  
## Dummy model
![alt text](https://github.com/MickySukmana/spyderbot/blob/main/img/stand.gif?raw=true)
![alt text](https://github.com/MickySukmana/spyderbot/blob/main/img/sit.gif?raw=true)
![alt text](https://github.com/MickySukmana/spyderbot/blob/main/img/lr.png?raw=true)
