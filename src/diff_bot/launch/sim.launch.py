import os
from launch import LaunchDescription
from launch.actions import TimerAction, IncludeLaunchDescription
from ament_index_python import get_package_share_directory
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description() -> LaunchDescription:
    pkg_share = get_package_share_directory("diff_bot")
    rsp_launch_file = os.path.join(pkg_share, "launch", "rsp.launch.py")
    rsp_launch_description = IncludeLaunchDescription(rsp_launch_file)

    gazebo_share = get_package_share_directory("gazebo_ros")
    gazebo_launch_file = os.path.join(gazebo_share, "launch", "gazebo.launch.py")
    world_file = os.path.join(pkg_share, "world", "house.world")
    arguments = {"world": world_file, "use_sim_time": "true"}
    gazebo_launch_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_launch_file),
        launch_arguments=arguments.items()
    )

    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-topic", "robot_description", "-entity", "ultron"],
    )

    delayed_spawner = TimerAction(
        period=6.0,
        actions=[spawn_entity]
    )

    return LaunchDescription(
        [rsp_launch_description, gazebo_launch_description, delayed_spawner]
    )
