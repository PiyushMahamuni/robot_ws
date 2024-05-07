import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
import xacro


def generate_launch_description() -> LaunchDescription:

    pkg_path = get_package_share_directory("description")
    abstract_launch_file = os.path.join(pkg_path, "launch", "abstract.launch.py")

    joint_state_publisher = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d" ,pkg_path + "/config/view_bot.rviz"]
    )

    return LaunchDescription([
        IncludeLaunchDescription(abstract_launch_file),
        joint_state_publisher,
        rviz
    ])