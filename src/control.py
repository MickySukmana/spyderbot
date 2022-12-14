import math
import sys
import rclpy
from rclpy.duration import Duration
from rclpy.action import ActionClient
from rclpy.node import Node
from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

class SpyderActionClient(Node):

    def __init__(self):
        super().__init__('spyderbot_control_actionclient')
        self._action_client = ActionClient(self, FollowJointTrajectory, '/joint_trajectory_controller/follow_joint_trajectory')

    def send_goal(self, _position, time_s):
        goal_msg = FollowJointTrajectory.Goal()

        """
        joint_names = ["lleg1_ax1_joint", "lleg1_ax2_joint", "lleg1_ax3_joint",
                       "lleg2_ax1_joint", "lleg2_ax2_joint", "lleg2_ax3_joint",
                       "rleg1_ax1_joint", "rleg1_ax2_joint", "rleg1_ax3_joint",
                       "rleg2_ax1_joint", "rleg2_ax2_joint", "rleg2_ax3_joint"
                      ]
        """
        joint_names = ["rl1_joint", "rl2_joint", "rl3_joint",
                       "fl1_joint", "fl2_joint", "fl3_joint",
                       "rr1_joint", "rr2_joint", "rr3_joint",
                       "fr1_joint", "fr2_joint", "fr3_joint"
                      ]

        points = []
        point = JointTrajectoryPoint()
        point.time_from_start = Duration(seconds=time_s, nanoseconds=0).to_msg()
        point.positions = _position

        points.append(point)

        goal_msg.goal_time_tolerance = Duration(seconds=time_s, nanoseconds=0).to_msg()
        goal_msg.trajectory.joint_names = joint_names
        goal_msg.trajectory.points = points

        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)
    
    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: '+str(result))
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
