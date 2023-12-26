import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def __init__(self, node):
        self.year = node.create_publisher(Int16, "year", 10)
        self.month = node.create_publisher(Int16, "month", 10)
        self.day = node.create_publisher(Int16, "day", 10)
        self.n = 0
        self.o = 0
        self.p = 0
        node.create_timer(0.5, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.year.publish(msg)
        msg.data = self.o
        self.month.publish(msg)
        msg.data = self.p
        self.day.publish(msg)
        
        self.n += 1
        self.o += 1
        self.p += 1
        

def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
