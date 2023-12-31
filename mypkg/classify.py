# SPDX-FileCopyrightText: 2023 Yuya Kyama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    judg = isprime(msg.data)
    node.get_logger().info("%d is a prime number? :%s " % (msg.data , judg))

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
