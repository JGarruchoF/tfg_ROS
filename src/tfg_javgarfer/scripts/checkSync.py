#!/usr/bin/python3
from __future__ import print_function

import roslib
import sys
import rospy
import cv2
import yaml
from sensor_msgs.msg import Image
from stereo_msgs.msg import DisparityImage

class check:
	def __init__(self):
		# Inicializar listener

		# self.d0_sub = rospy.Subscriber("/stereo/1/disparity",DisparityImage, lambda data: print("d1: ",data.header.seq), queue_size=4)
		# self.d1_sub = rospy.Subscriber("/stereo/2/disparity",DisparityImage, lambda data: print("d2: ",data.header.seq), queue_size=4)
		# self.d2_sub = rospy.Subscriber("/stereo/3/disparity",DisparityImage, lambda data: print("d3: ",data.header.seq), queue_size=4)

		self.d_sub = rospy.Subscriber("/stereo/disparity",DisparityImage, self.callback, queue_size=3)


		# self.r0_sub = rospy.Subscriber("/stereo/0/right/image_raw",Image, lambda data: print("r0: ",data.header.seq), queue_size=4)
		# self.l0_sub = rospy.Subscriber("/stereo/0/left/image_raw",Image, lambda data: print("l0: ",data.header.seq), queue_size=4)
		# self.r1_sub = rospy.Subscriber("/stereo/1/right/image_raw",Image, lambda data: print("r1: ",data.header.seq), queue_size=4)
		# self.l1_sub = rospy.Subscriber("/stereo/1/left/image_raw",Image, lambda data: print("l1: ",data.header.seq), queue_size=4)
	


	def callback(self, data):
		print("d: ",data.header.stamp)
		with open("/home/jgarruchof/tiempos.txt", 'a+') as f:
			f.write(str(data.header.stamp)+";")

def main(args):
	c = check()
	rospy.init_node('checkSync', anonymous=True)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")

if __name__ == '__main__':
	args = rospy.myargv(argv=sys.argv)

	main(args)

