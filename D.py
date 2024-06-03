
import rclpy
import time
from geometry_msgs.msg import Twist


class TurtlesimDDrawer:
    def __init__(self):
        rclpy.init()

        self.node = rclpy.create_node('turtlesim_d_drawer')
        self.cmd_vel_pub = self.node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # Hareket komutlarını yayınlamadan önce biraz bekleyelim
        time.sleep(1)

        self.draw_d()

        rclpy.spin_once(self.node, timeout_sec=1.0)
        self.node.destroy_node()
        rclpy.shutdown()
        
    def rotate_turtle(self, angle):
        # angle: Radyan cinsinden döndürme açısı
        twist = Twist()
        twist.angular.z = angle
        self.cmd_vel_pub.publish(twist)
        time.sleep(1.0)



    def draw_d(self):
        # D harfini çizmek için hareket komutları
        self.move_turtle(2.0, 1.0, 2.2)   
        time.sleep(2.0)

        # İkinci hareket: Solda dur
        self.move_turtle(-2.0, 0.5, 0.0)
        time.sleep(1.0)
        
        self.rotate_turtle(1.5700)  # 90 derece radyan cinsinden
        time.sleep(1.0)

      
        # Üçüncü hareket: Sağa gidip uzun bir dikey çizgi çiz
        self.move_turtle(0.5, 0.0, 7.6)  # Dikey çizgi
        time.sleep(1.0)
        
        
        
    
    # Dördüncü hareket: Dur
        self.move_turtle(0.0, 0.0, 0.0)
        time.sleep(1.0)

        

    def move_turtle(self, linear, angular, duration):
        twist = Twist()
        twist.linear.x = linear
        twist.angular.z = angular

        start_time = time.time()
        while time.time() - start_time < duration:
            self.cmd_vel_pub.publish(twist)
            time.sleep(0.1)

if __name__ == '__main__':
    d_drawer = TurtlesimDDrawer()



