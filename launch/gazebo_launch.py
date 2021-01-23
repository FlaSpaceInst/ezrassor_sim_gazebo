"""Launch Gazebo with the specified world file (empty world by default)."""
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
import os


def generate_launch_description():
    """Spawn a new instance of Gazebo Classic with an optional world file."""

    pkg_gazebo_ros = get_package_share_directory("gazebo_ros")
    pkg_ezrassor_sim_gazebo = get_package_share_directory("ezrassor_sim_gazebo")

    world_argument = DeclareLaunchArgument(
        "world",
        default_value=[
            os.path.join(pkg_ezrassor_sim_gazebo, "worlds", "base.world"),
            "",
        ],
        description="Gazebo world file (full path)",
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, "launch", "gazebo.launch.py")
        ),
        launch_arguments={"world": LaunchConfiguration("world")}.items(),
    )

    return LaunchDescription([world_argument, gazebo])
