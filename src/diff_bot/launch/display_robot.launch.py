import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from ament_index_python import get_package_share_directory
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    pkg_share = get_package_share_directory("diff_bot")
    rsp_launch_file = os.path.join(pkg_share, "launch", "rsp.launch.py")
    rsp_launch_description = IncludeLaunchDescription(rsp_launch_file)

    rviz_config = os.path.join(pkg_share, "config", "display_bot.rviz")
    rviz2 = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        arguments=["-d", rviz_config]
    )

    jsp_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        output="screen"
    )

    # you can still set launch configurations that you set in the launch files you have included
    # in this launch file from CLI
    return LaunchDescription([rsp_launch_description, rviz2, jsp_gui])