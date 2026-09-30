from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    package_path = get_package_share_directory('robot_description')

    urdf_file = os.path.join(package_path, 'urdf', 'first_robot.urdf')

    robot_description = open(urdf_file).read()  

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[
            {
                'robot_description': robot_description
            }
        ]
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2'
    )

    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_node,
        rviz_node
    ])



































# from launch import LaunchDescription
# from launch_ros.actions import Node
# from ament_index_python.packages import get_package_share_directory
# import os


# def generate_launch_description():

#     package_path = get_package_share_directory('robot_description')

#     urdf_file = os.path.join(
#         package_path,
#         'urdf',
#         'first_robot.urdf'
#     )

#     robot_description = open(urdf_file).read()

#     return LaunchDescription([

#         Node(
#             package='robot_state_publisher',
#             executable='robot_state_publisher',
#             parameters=[
#                 {
#                     'robot_description': robot_description
#                 }
#             ]
#         ),

#         Node(
#             package='joint_state_publisher_gui',
#             executable='joint_state_publisher_gui'
#         )

#         # Node(
#         #     package='rviz2',
#         #     executable='rviz2'
#         # )

#     ])







