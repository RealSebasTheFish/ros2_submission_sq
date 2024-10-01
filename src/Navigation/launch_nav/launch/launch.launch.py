from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    check = Node(
        package="gps_distance",
        executable="gps_distance"
    )
    ld.add_action(check)
    # This is an example of the proper structure
    # check = Node(
    #     package="gps_distance",
    #     executable="completeSoftwareOnboarding",
    # )

    # ld.add_action(check)
    
    # Your code here

    return ld