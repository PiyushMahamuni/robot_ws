import os
import xacro
from launch import LaunchDescription
from ament_index_python import get_package_share_directory
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    pkg_share = get_package_share_directory("diff_bot")
    urdf_file = os.path.join(pkg_share, "urdf", "robot.urdf.xacro")
    robot_description = xacro.process_file(urdf_file).toxml()
    use_sim_time = LaunchConfiguration("use_sim_time", default=True)
    params = {"robot_description": robot_description, "use_sim_time": use_sim_time}
    rsp = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=params.items(),
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "use_sim_time",
                use_sim_time,
                description="use gazebo clock if set to true",
            ),
            rsp
        ]
    )
