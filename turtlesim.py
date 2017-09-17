import math
from time import sleep

import rospy
from geometry_msgs.msg import Twist

class Turtle(object):
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=25)
    vel_msg = Twist()
    def move(self,distance):
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
        angular_speed = 1.0
        relative_angle = math.radians(angle)

        self.vel_msg.linear.x = 0
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0

        self.vel_msg.angular.z = abs(angular_speed)
        t0 = rospy.Time.now().to_sec()
        current_angle = 0

        while (current_angle < relative_angle):
            self.velocity_publisher.publish(self.vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed * (t1 - t0)

        #detener a la tortuga
        self.stop_moving()

    def forward(self,distancia):
        self.move(distancia)

    def stop_moving(self):
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0
        self.vel_msg.linear.x = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = 0
        self.velocity_publisher.publish(self.vel_msg)

def draw_pentagram(sides,size=1.8):
    tortu = Turtle()
    tortu.forward(0)
    for side in range(sides):
        sleep(0.5)
        tortu.forward(size)
        tortu.rotate(180)
        tortu.rotate(360/(sides*2))

def draw_cute_star(size=1.8):
    tortu = Turtle()
    tortu.forward(0)
    for side in range(5):
        tortu.forward(size)
        tortu.rotate(36)
        tortu.forward(size)
        tortu.rotate(252)

if __name__ == '__main__':
    try:
        #draw_pentagram(6)
        draw_cute_star(1.5)

            # except rospy.ROSInterruptException:
        #     pass
    except:
        pass
