
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class Navigation(Node):
    def __init__(self):
        super().__init__('navigation')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.laser_callback,
            10)
        self.subscription  # prevent unused variable warning

    def laser_callback(self, msg):
        cmd = Twist()
        if min(msg.ranges) < 0.5:
            cmd.angular.z = 0.5
        else:
            cmd.linear.x = 0.5
        self.publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    navigation = Navigation()
    rclpy.spin(navigation)
    navigation.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
