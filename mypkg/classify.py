import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    print("Is a prime number?:",isprime(msg.data)) 

def isprime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True
    

rclpy.init()
node = Node("classify")
pub = node.create_subscription(Int16, "countup", cb, 10)
rclpy.spin(node)
