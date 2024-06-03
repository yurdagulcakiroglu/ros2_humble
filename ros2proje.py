import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import threading
import time

def run_turtlesim_node(namespace):
    import subprocess
    subprocess.run(["ros2", "run", "turtlesim", "turtlesim_node", "--ros-args", "--remap", f"__ns:={namespace}"])

def draw_D(node, publisher_D):
    msg = Twist()
    time.sleep(13)  

    
    msg.linear.x = 0.0
    msg.linear.y = -3.1
    publisher_D.publish(msg)
    time.sleep(2)
    
    for a in range(18):  
    
        msg.linear.x = 20 * math.sin(math.radians(a * 10))
        msg.linear.y = 0.0 * math.cos(math.radians(a * 100))
        msg.angular.z = 15.0 * math.sin(math.radians(a * 10))
        publisher_D.publish(msg)

    msg.linear.x = 0.0
    msg.linear.y = 0.0
    msg.angular.z = 0.0
    time.sleep(2)
    publisher_D.publish(msg)
   
def draw_C(node, publisher_C):
    msg = Twist()
    time.sleep(13)  

   
    for a in range(18):  
    
        msg.linear.x = -25 * math.sin(math.radians(a * 10))
        msg.linear.y = 0.0 * math.cos(math.radians(a * 100))
        msg.angular.z = 17.0 * math.sin(math.radians(a * 10))
        publisher_C.publish(msg)

    msg.linear.x = 0.0
    msg.linear.y = 0.0
    msg.angular.z = 0.0
    time.sleep(2)
    publisher_C.publish(msg)


def draw_3(node, publisher_3):
    msg = Twist()
    time.sleep(13)
    
   
    
    
    for a in range(18):
        msg.linear.x = 2.0 * math.sin(math.radians(a * 20))
        msg.linear.y = 2.0 - 2.0 * math.cos(math.radians(a * 20))
        msg.angular.z = 0.5  
        publisher_3.publish(msg)
        time.sleep(0.1)
    
    for a in range(18):
        msg.linear.x = 1.0 * math.sin(math.radians(a * 20))
        msg.linear.y = 2.0 - 2.0 * math.cos(math.radians(a * 20))
        msg.angular.z = 0.5  
        publisher_3.publish(msg)
        time.sleep(0.1)



def draw_2(node, publisher_2):
    msg = Twist()
    time.sleep(20)  
    for a in range(18):
        msg.linear.x = 2.0 * math.sin(math.radians(a * 20))
        msg.linear.y = 2.0 - 2.0 * math.cos(math.radians(a * 20))
        msg.angular.z = 0.5  
        publisher_2.publish(msg)
        time.sleep(0.1)
    

    msg.linear.x =2.0
    msg.linear.y = -2.0
    time.sleep(1.5)
    publisher_2.publish(msg)

    msg.linear.x = 2.0
    msg.linear.y = 0.0
    time.sleep(1)
    publisher_2.publish(msg)

   

def main():
    rclpy.init()

    # Dört Turtlesim düğümünü ayrı thread'lerde başlat
    thread1 = threading.Thread(target=run_turtlesim_node, args=("/turtlesim1",))
    thread2 = threading.Thread(target=run_turtlesim_node, args=("/turtlesim2",))
    thread3 = threading.Thread(target=run_turtlesim_node, args=("/turtlesim3",))
    thread4 = threading.Thread(target=run_turtlesim_node, args=("/turtlesim4",))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # ROS node oluştur ve yayınlayıcıları ayarla
    node = Node("letter_drawer")
    publisher_C = node.create_publisher(Twist, '/turtlesim1/turtle1/cmd_vel', 10)
    publisher_D = node.create_publisher(Twist, '/turtlesim2/turtle1/cmd_vel', 10)
    publisher_3 = node.create_publisher(Twist, '/turtlesim3/turtle1/cmd_vel', 10)
    publisher_2 = node.create_publisher(Twist, '/turtlesim4/turtle1/cmd_vel', 10)

    # Harfleri çizmek için thread'leri başlat
    thread_c = threading.Thread(target=draw_C, args=(node, publisher_C,))
    thread_d = threading.Thread(target=draw_D, args=(node, publisher_D,))
    thread_3 = threading.Thread(target=draw_3, args=(node, publisher_3,))
    thread_2 = threading.Thread(target=draw_2, args=(node, publisher_2,))
    thread_c.start()
    thread_d.start()
    thread_3.start()
    thread_2.start()

    # Thread'lerin tamamlanmasını bekle
    thread_c.join()
    thread_d.join()
    thread_3.join()
    thread_2.join()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    rclpy.shutdown()

if __name__ == '__main__':
    main()

