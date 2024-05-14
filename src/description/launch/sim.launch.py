import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description() -> LaunchDescription:
    pkg_share = get_package_share_directory("description")
    abstract_launch_file = os.path.join(pkg_share, "launch", "abstract.launch.py")
    gazebo_launch_file = os.path.join(
        get_package_share_directory("gazebo_ros"), "launch", "gazebo.launch.py"
    )
    world_file = os.path.join(pkg_share, "worlds", "house.world")
    world = LaunchConfiguration("world", default=world_file)
    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        output="screen",
        arguments=["-topic", "robot_description", "-entity", "robot"],
    )

    diff_drive_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_cont"]
    )

    joint_broad_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_broad"]
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", pkg_share + "/config/simulation.rviz"],
    )

    return LaunchDescription(
        [
            IncludeLaunchDescription(abstract_launch_file),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(gazebo_launch_file),
                launch_arguments={"world": world}.items(),
            ),
            spawn_entity,
            diff_drive_controller_spawner,
            joint_broad_controller_spawner,
            rviz,
        ]
    )
