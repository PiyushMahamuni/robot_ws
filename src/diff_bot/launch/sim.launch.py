import os
from launch import LaunchDescription
from launch.actions import TimerAction, IncludeLaunchDescription
from ament_index_python import get_package_share_directory
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    pkg_share = get_package_share_directory("diff_bot")
    rsp_launch_file = os.path.join(pkg_share, "launch", "rsp.launch.py")
    rsp_launch_description = IncludeLaunchDescription(rsp_launch_file)

    gazebo_share = get_package_share_directory("gazebo_ros")
    gazebo_launch_file = os.path.join(gazebo_share, "launch", "gazebo.launch.py")
    gazebo_launch_description = IncludeLaunchDescription(gazebo_launch_file)

    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-topic", "robot_description", "-entity", "ultron"],
    )

    delayed_spawner = TimerAction(
        period=10.0,
        actions=[spawn_entity]
    )

    return LaunchDescription(
        [rsp_launch_description, gazebo_launch_description, delayed_spawner]
    )
