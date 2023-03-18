from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return launch.LaunchDescription()([
        launch_ros.actions.Node(
            package='demo_nodes_py',
            executable='listener'
        )

    ])

 