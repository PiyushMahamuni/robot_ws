import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description() -> LaunchDescription:
    gazebo_share = get_package_share_directory("gazebo_ros")
    gazebo_launch_file = os.path.join(gazebo_share, "launch", "gazebo.launch.py")
    pkg_share = get_package_share_directory("diff_bot")
    world_file = os.path.join(pkg_share, "worlds", "house.world")
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_launch_file),
        launch_arguments={"world": world_file}.items(),
    )
    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-topic", "robot_description", "-entity", "robot_diff"],
    )

    return LaunchDescription([gazebo_launch, spawn_entity])
