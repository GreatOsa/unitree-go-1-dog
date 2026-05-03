import os
from ament_index_python.packages import get_package_share_directory
# import joint_state_publisher
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.actions import TimerAction
import xacro


def generate_launch_description():
    pkg_share = get_package_share_directory('unitreedog_description')

    # Paths
    xacro_file = os.path.join(pkg_share, 'urdf', 'unitreeDog.urdf.xacro')
    rviz_config_file = os.path.join(
        pkg_share, 'rviz', 'urdf_config.rviz')  # create/config this file

    # Process URDF
    robot_description_config = xacro.process_file(xacro_file)
    robot_desc = robot_description_config.toxml()

    # 1. Gazebo Launch (Ignition/Gazebo Sim)
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]),
        launch_arguments={'gz_args': '-r empty.sdf --verbose 4'}.items(),
    )

    # 2. Robot State Publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc, 'use_sim_time': True}]
    )

    # 3. Spawn the robot in Gazebo
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'UnitreeDog',
            '-topic', 'robot_description',
            '-x', '0',
            '-y', '0',
            '-z', '1.5'
        ],
        output='screen',
    )

    # 4. Bridge (ROS 2 <-> Gazebo)
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            # '/model/UnitreeDog/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V]',
            '/model/UnitreeDog/joint_state@sensor_msgs/msg/JointState[gz.msgs.Model]',
            '/world/empty/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock]'
        ],
        output='screen'
    )

    # joint_state_publisher = Node(
    #     package='joint_state_publisher_gui',
    #     executable='joint_state_publisher_gui',
    #     name='joint_state_publisher_gui'
    # )

    # 5. RViz Node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        output='screen',
        parameters=[{'use_sim_time': True}]
    )



    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_robot,
        # joint_state_publisher,
        bridge,
        rviz_node,
        
        TimerAction(
            period=5.0,
            actions=[
                Node(
                    package="controller_manager",
                    executable="spawner",
                    arguments=["joint_state_broadcaster"],
                ),
               

                Node(
                    package="controller_manager",
                    executable="spawner",
                    arguments=["joint_trajectory_controller"],
                )
            ]
        )
  
    ])

