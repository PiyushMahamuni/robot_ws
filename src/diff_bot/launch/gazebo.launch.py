import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory
from launch.actions import IncludeLaunchDescription


def generate_launch_description() -> LaunchDescription:
    gazebo_share = get_package_share_directory("gazebo_ros")
    gazebo_launch_file = os.path.join(gazebo_share, "launch", "gazebo.launch.py")
    gazebo_launch = IncludeLaunchDescription(gazebo_launch_file)
    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-topic", "robot_description", "-entity", "robot_diff"],
    )

    return LaunchDescription([
        gazebo_launch,
        spawn_entity
    ])
