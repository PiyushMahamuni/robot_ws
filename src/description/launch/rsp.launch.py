import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import xacro


def generate_launch_description() -> LaunchDescription:
    use_sim_time = LaunchConfiguration("use_sim_time", default=True)

    pkg_path = get_package_share_directory("description")
    xacro_file = os.path.join(pkg_path, "urdf", "robot.urdf.xacro")
    robot_description = xacro.process_file(xacro_file).toxml()

    params={"robot_description": robot_description, "use_sim_time": use_sim_time}
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[params]
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d" ,pkg_path + "/config/view_bot.rviz"]
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            "use_sim_time",
            default_value="true",
            description="use sim time if true"
        ),
        robot_state_publisher,
        rviz
    ])