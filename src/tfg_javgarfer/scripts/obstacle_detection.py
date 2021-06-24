#!/usr/bin/python3

import rospy
import numpy as np
from stereo_msgs.msg import DisparityImage
from cv_bridge import CvBridge, CvBridgeError
import sys



class naive_obstacle_detector:

	

	def __init__(self):
		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("/stereo/disparity",DisparityImage,self.callback, queue_size=1)
		self.stop = False
		self.count = 0
		self.stopDistance = 50


	def callback(self,data):
		try:
			disparity_img = self.bridge.imgmsg_to_cv2(data.image, "passthrough")
		except CvBridgeError as e:
			print(e)

		max_disp = disparity_img.max()
		distance = 5*875/max_disp
		print(distance, " cm") #base_offset*focal_length/disparity


		if not self.stop and distance < self.stopDistance:
			self.count += 1
		elif self.stop and distance >= self.stopDistance :
			self.count += 1
		else:
			self.count = 0

		if self.count > 3:
			self.stop = not self.stop
			self.count = 0

		print("stop" if self.stop else "go")


def main(args):
	ic = naive_obstacle_detector()
	rospy.init_node('naive_obstacle_detector', anonymous=True)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
		cv2.destroyAllWindows()

if __name__ == '__main__':
	main(sys.argv)
