import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from ament_index_python import get_package_share_directory
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
import xacro


def generate_launch_description() -> LaunchDescription:
    pkg_share = get_package_share_directory("diff_bot")
    gazebo_launch_file = os.path.join(pkg_share, "launch", "gazebo.launch.py")
    gazebo_launch = IncludeLaunchDescription(gazebo_launch_file)
    rsp_launch_file = os.path.join(pkg_share, "launch", "rsp.launch.py")
    rsp_launch_description = PythonLaunchDescriptionSource(rsp_launch_file)
    xacro_file = os.path.join(pkg_share, "urdf", "gazebo_sim.xacro")
    robot_description = xacro.process_file(xacro_file).toxml()
    args = {"robot_description": robot_description}
    rsp_launch = IncludeLaunchDescription(rsp_launch_description, launch_arguments=args.items())
    rviz_config = os.path.join(pkg_share, "config", "sim.rviz")
    rviz = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        arguments=["-d", rviz_config]
    )

    return LaunchDescription([
        rsp_launch,
        gazebo_launch,
        rviz
    ])