from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    gazebo_path = get_package_share_directory('gazebo_ros')

    gazebo_launch_file = os.path.join(gazebo_path,'launch','gazebo.launch.py')

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_launch_file)
    )

    package_path = get_package_share_directory('robot_description')

    urdf_file = os.path.join(package_path,'urdf','first_robot.urdf')

    robot_description = open(urdf_file).read()

    robot_state_publisher_node =Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[
                {
                    'robot_description': robot_description,
                    'use_sim_time': True
                }
            ]
    )

    gazebo_ros = Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-topic',
                'robot_description',
                '-entity',
                'first_robot'
            ],
            output='screen'
    )
    return LaunchDescription([
        robot_state_publisher_node,
        gazebo_ros,
        gazebo
        

    ])