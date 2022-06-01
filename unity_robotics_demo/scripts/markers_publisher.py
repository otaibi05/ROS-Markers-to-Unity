#!/usr/bin/env python

import rospy
import rosgraph
import time
from unity_robotics_demo_msgs.msg import MarkersType


TOPIC_NAME = 'markers'
NODE_NAME = 'markers_publisher'


def post_markers():
    pub = rospy.Publisher(TOPIC_NAME, MarkersType, queue_size=10)
    rospy.init_node(NODE_NAME, anonymous=True)

    c = 1
    s = 2
    m = 10
    markers = MarkersType(c, s, m)

    wait_for_connections(pub, TOPIC_NAME)
    pub.publish(markers)

    time.sleep(0.1)


def wait_for_connections(pub, topic):
    ros_master = rosgraph.Master('/rostopic')
    topic = rosgraph.names.script_resolve_name('rostopic', topic)
    num_subs = 0
    for sub in ros_master.getSystemState()[1]:
        if sub[0] == topic:
            num_subs+=1

    for i in range(10):
        if pub.get_num_connections() == num_subs:
            return
        time.sleep(0.1)
    raise RuntimeError("failed to get publisher")


if __name__ == '__main__':
    try:
        post_markers()
    except rospy.ROSInterruptException:
        pass
    
