import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory


def generate_launch_description() -> LaunchDescription:
    pkg_share = get_package_share_directory("diff_bot")
    sim_launch_file = os.path.join(pkg_share, "launch", "sim.launch.py")
    sim_launch_description = IncludeLaunchDescription(sim_launch_file)

    rviz_launch_file = os.path.join(pkg_share, "launch", "rviz.launch.py")
    rviz_launch_description = IncludeLaunchDescription(rviz_launch_file)

    slam_share = get_package_share_directory("slam_toolbox")
    slam_launch_file = os.path.join(slam_share, "launch", "online_async_launch.py")
    params_file = os.path.join(pkg_share, "config", "mapper_params_online_async.yaml")
    arguments = {"params_file": params_file, "use_sim_time": "true"}
    slam_launch_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(slam_launch_file),
        launch_arguments=arguments.items(),
    )

    return LaunchDescription(
        [sim_launch_description, rviz_launch_description, slam_launch_description]
    )
