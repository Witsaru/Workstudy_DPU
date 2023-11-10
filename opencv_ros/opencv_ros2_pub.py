import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2

class ImageProcessor(Node):
    def __init__(self):
        super().__init__('image_processor')
        self.cv_bridge = CvBridge()

        self.publishers_ = self.create_publisher(Image, 'video_frames', 10)

        timer_period = 0.1

        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.cap = cv2.VideoCapture(0)
        self.br = CvBridge()

        
    def timer_callback(self):
       
        ret, frame = self.cap.read()

        if ret == True:
           self.publishers_.publish(self.br.cv2_to_imgmsg(frame))

        self.get_logger().info('Publishing video frame')


def main(args=None):
    rclpy.init(args=args)
    image_processor = ImageProcessor()
    rclpy.spin(image_processor)
    rclpy.shutdown()

if __name__ == '__main__':
    main()