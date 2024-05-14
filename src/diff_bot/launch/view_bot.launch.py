import os
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python import get_package_share_directory


def generate_launch_description() -> LaunchDescription:
    pkg_share = get_package_share_directory("diff_bot")
    rsp_launch_file = os.path.join(pkg_share, "launch", "rsp.launch.py")
    rsp_launch = IncludeLaunchDescription(rsp_launch_file)
    rviz = Node(package="rviz2", executable="rviz2", output="screen")
    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        output="screen",
    )

    return LaunchDescription([rsp_launch, rviz, joint_state_publisher_gui])
