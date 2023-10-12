import math
from math import radians
import rospy
from geometry_msgs.msg import Twist
import time

class TurtlebotDriving:
    def __init__(self):
        rospy.init_node('turtlebot_square', anonymous = True)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        r = rospy.Rate(10)
        t = rospy.Time.now().to_sec()
        
        while not rospy.is_shutdown():
             velocity = Twist()
             velocity.linear.x = 0.2
             for i in range(10):
                  self.pub.publish(velocity)
                  r.sleep()
        
        velocity = Twist()
        velocity.angular.z = 1.57/2
        for i in range(10):
             self.pub.publish(velocity)
             r.sleep

    def stop(self):
         velocity = Twist()
         self.pub.publish(velocity)
        
if __name__ == '__main__':
     rospy.init_node('turtlebot_square')
     TurtlebotDriving()



    
    