# ROS Markers to Unity

**About**

Sending a message to display markers from ROS, then receiving the message in Unity and displaying the markers.

**Demo**

https://user-images.githubusercontent.com/98209046/171490465-a0afd854-9237-4327-add7-79b922543e39.mp4

**Installation**

1\. If you don't already have a ROS environment, [set up a ROS environment](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment).

2\. Follow [this setup tutorial for ROS-Unity Integration](https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/ros_unity_integration/setup.md). Setup for Unity except for setting the `ROS IP Address` and `ROS Port` should be avoided since the Unity project in the repository is already set up.

3\. Change the network adapter setting to `Bridged Adapter` and enter `ifconfig` on the Ubuntu terminal to get the `ROS IP Address` from `enp0s3`.

4\. Replace `unity_robotics_demo` and `unity_robotics_demo_msgs` from `tutorials/ros_unity_integration/ros_packages` with `unity_robotics_demo` and `unity_robotics_demo_msgs` from this repository in your Catkin workspace.

5\. Open the Unity project from this repository with Unity and follow the demo video. Use [ROS–Unity Demo Setup](https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/ros_unity_integration/setup.md) and [ROS–Unity Integration: Subscriber](https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/ros_unity_integration/subscriber.md) for reference.
