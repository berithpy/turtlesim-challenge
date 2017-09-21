import math
from time import sleep

import rospy
import std_srvs.srv
from geometry_msgs.msg import Twist

reset = rospy.ServiceProxy('reset', std_srvs.srv.Empty())


class Turtle(object):
    rospy.init_node('robot_cleaner', anonymous=True)

    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=25)
    vel_msg = Twist()

    def move(self, distance):
        """
        Moves the turtle in a straight line.
        :param distance: unit of distance traveled
        """
        speed = 1

        self.vel_msg.linear.x = abs(speed)
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = 0

        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while (current_distance < distance):
            self.velocity_publisher.publish(self.vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = speed * (t1 - t0)
        self.stop_moving()

    def rotate(self, angle):
        """
        Rotate the turtle.
        :param angle: degrees to rotate, positive or negative to move either left or right
        :return: 
        """
        angular_speed = 1.0
        relative_angle = math.radians(abs(angle))

        self.vel_msg.linear.x = 0
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0

        if (angle>0):
            self.vel_msg.angular.z = angular_speed
        else:
            self.vel_msg.angular.z = -angular_speed
        t0 = rospy.Time.now().to_sec()
        current_angle = 0

        while (current_angle < relative_angle):
            self.velocity_publisher.publish(self.vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed * (t1 - t0)

        self.stop_moving()

    def forward(self, distancia):
        self.move(distancia)

    def stop_moving(self):
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0
        self.vel_msg.linear.x = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = 0
        self.velocity_publisher.publish(self.vel_msg)

    def __init__(self):
        pass


def draw_pentagram(tortu, size=1.8):
    for side in range(5):
        tortu.forward(size)
        tortu.rotate(-144)


def draw_cute_star(tortu, size=1.8):
    for side in range(5):
        tortu.forward(size)
        tortu.rotate(36)
        tortu.forward(size)
        tortu.rotate(-108)


if __name__ == '__main__':
    try:
        turtle = Turtle()
        reset()
        draw_cute_star(turtle, 1.5)
        print("Drawing cute star!")
        sleep(4)
        reset()
        draw_pentagram(turtle,1.8)
        print("Drawing pentagram.")

    except rospy.ROSInterruptException:
        pass
