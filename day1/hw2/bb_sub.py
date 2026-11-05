import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy
from std_msgs.msg import String


class BBSub(Node):
    def __init__(self):
        super().__init__('bb_sub')
        # config: 나중에 접속해도 받아야 함 → transient local
        config_qos = QoSProfile(depth=1,
                                reliability=ReliabilityPolicy.RELIABLE,
                                durability=DurabilityPolicy.TRANSIENT_LOCAL)
        # stream: 발행자가 best effort → 구독도 best effort
        stream_qos = QoSProfile(depth=10,
                                reliability=ReliabilityPolicy.BEST_EFFORT,
                                durability=DurabilityPolicy.VOLATILE)
        self.create_subscription(String, '/bb_c171/config', self.on_config, config_qos)
        self.create_subscription(String, '/bb_c171/stream', self.on_stream, stream_qos)

    def on_config(self, msg):
        self.get_logger().info(f'[config] {msg.data}')

    def on_stream(self, msg):
        self.get_logger().info(f'[stream] {msg.data}')


rclpy.init()
rclpy.spin(BBSub())
