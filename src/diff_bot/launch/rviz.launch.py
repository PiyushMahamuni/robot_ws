import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument


def generate_launch_description() -> LaunchDescription:
    pkg_share = get_package_share_directory("diff_bot")
    rviz_config = os.path.join(pkg_share, "config", "sim.rviz")
    use_sim_time = LaunchConfiguration("use_sim_time", default=True)
    params = {"use_sim_time": use_sim_time}

    rviz2 = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        arguments=["-d", rviz_config],
        parameters=[params]
    )

    return LaunchDescription([
        DeclareLaunchArgument("use_sim_time", default_value="true",
                              description="use gazebo clock if true"),
        rviz2])
