import rclpy
from geometry_msgs.msg import Twist
import time

class Turtlesim2Drawer:
    def __init__(self):
        rclpy.init()

        self.node = rclpy.create_node('turtlesim_2_drawer')
        self.cmd_vel_pub = self.node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # Hareket komutlarını yayınlamadan önce biraz bekleyelim
        time.sleep(20)

        self.draw_2()

        rclpy.spin_once(self.node, timeout_sec=1.0)
        self.node.destroy_node()
        rclpy.shutdown()
        
    def rotate_turtle(self, angle):
        # angle: Radyan cinsinden döndürme açısı
        twist = Twist()
        twist.angular.z = angle
        self.cmd_vel_pub.publish(twist)
        time.sleep(1.0)

    def draw_2(self):
      
    
        #2 çizmek için hareket komutları
        self.move_turtle(0.0, 0.0, 0.0)   # Başlangıç
        time.sleep(1.0)
        self.move_turtle(0.7, -0.5, 2.7)
        time.sleep(1.0)
        self.rotate_turtle(-0.8)
        self.move_turtle(0.5, 0.0, 3.0)
        time.sleep(1.0)
        self.rotate_turtle(-0.4)
        time.sleep(1.0)
        self.move_turtle(0.0, 1.0, 2.0)
        time.sleep(1.0)
        self.move_turtle(0.5, 0.0, 3.0)
        

    def move_turtle(self, linear, angular, duration):
        twist = Twist()
        twist.linear.x = linear
        twist.angular.z = angular

        start_time = time.time()
        while time.time() - start_time < duration:
            self.cmd_vel_pub.publish(twist)
            time.sleep(0.1)

if __name__ == '__main__':
    drawer = Turtlesim2Drawer()



