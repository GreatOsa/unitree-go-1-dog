from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['ros2', 'launch', 'ros_ign_gazebo', 'empty_world.launch.py'],
            output='screen'
        ),
        ExecuteProcess(
            cmd=['ros2', 'run', 'ros_g', 'create',
                 '-file', '/path/to/unitreeDog.urdf',
                 '-name', 'unitree_go1'],
            output='screen'
        )
    ])