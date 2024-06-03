import rclpy
from geometry_msgs.msg import Twist
import time

class Turtlesim_C_Drawer:
    def __init__(self):
        rclpy.init()

        self.node = rclpy.create_node('turtlesim_c_drawer')
        self.cmd_vel_pub = self.node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # Hareket komutlarını yayınlamadan önce biraz bekleyelim
        time.sleep(1)

        self.draw_c()

        rclpy.spin_once(self.node, timeout_sec=1.0)
        self.node.destroy_node()
        rclpy.shutdown()

    def draw_c(self):
        # C harfini çizmek için hareket komutları
        self.move_turtle(0.0, -0.5, 0.5)
        time.sleep(1.0)
        self.move_turtle(-1.3, 0.5, 8.0)

    def move_turtle(self, linear, angular, duration):
        twist = Twist()
        twist.linear.x = linear
        twist.angular.z = angular

        start_time = time.time()
        while time.time() - start_time < duration:
            self.cmd_vel_pub.publish(twist)
            time.sleep(0.1)

if __name__ == '__main__':
    drawer = Turtlesim_C_Drawer()

