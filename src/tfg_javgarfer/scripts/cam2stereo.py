#!/usr/bin/python3
from __future__ import print_function

import roslib
import sys
import rospy
import cv2
import yaml
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
from sensor_msgs.msg import CameraInfo



def yaml_to_CameraInfo(yaml_fname):
	with open(yaml_fname, "r") as file_handle:
		calib_data = yaml.load(file_handle)

 # Parse camera_info
	camera_info_msg = CameraInfo()
	camera_info_msg.width = calib_data["image_width"]
	camera_info_msg.height = calib_data["image_height"]
	camera_info_msg.K = calib_data["camera_matrix"]["data"]
	camera_info_msg.D = calib_data["distortion_coefficients"]["data"]
	camera_info_msg.R = calib_data["rectification_matrix"]["data"]
	camera_info_msg.P = calib_data["projection_matrix"]["data"]
	camera_info_msg.distortion_model = calib_data["distortion_model"]
	return camera_info_msg



class image_converter:
	def __init__(self, numero_maquinas=1):
		self.numero_maquinas = numero_maquinas
		# Inicializar talkers
		self.left_pubs = [rospy.Publisher("/stereo/"+str(i+1)+"/left/image_raw/compressed",CompressedImage, queue_size=5) for i in range(numero_maquinas)]
		self.right_pubs = [rospy.Publisher("/stereo/"+str(i+1)+"/right/image_raw/compressed",CompressedImage, queue_size=5) for i in range(numero_maquinas)]

		self.left_info_pubs = [rospy.Publisher("/stereo/"+str(i+1)+"/left/camera_info",CameraInfo, queue_size=5) for i in range(numero_maquinas)]
		self.right_info_pubs = [rospy.Publisher("/stereo/"+str(i+1)+"/right/camera_info",CameraInfo, queue_size=5) for i in range(numero_maquinas)]


		# self.left_pub = rospy.Publisher("/stereo/left/image_raw",Image, queue_size=1)
		# self.right_pub = rospy.Publisher("/stereo/right/image_raw",Image, queue_size=1)
		# self.left_info_pub = rospy.Publisher("/stereo/left/camera_info",CameraInfo, queue_size=1)
		# self.right_info_pub = rospy.Publisher("/stereo/right/camera_info",CameraInfo, queue_size=1)

		# Inicializar listener
		self.image_sub = rospy.Subscriber("/usb_cam/image_raw/compressed",CompressedImage,self.callback, queue_size=3)

		# Inicializar CvBridge
		self.bridge = CvBridge()



	def callback(self,data):
		try:
			cv_image = self.bridge.compressed_imgmsg_to_cv2(data, desired_encoding="bgr8")
		except CvBridgeError as e:
			print(e)


		# Separar imagenes
		(rows,cols,channels) = cv_image.shape
		cv_left = cv_image[:,cols//2:]
		cv_right = cv_image[:,:cols//2]

		# ===========DEBUG===============
		# cv2.imshow("Left", cv_left)
		# cv2.waitKey(3)
		# cv2.imshow("Right", cv_right)
		# cv2.waitKey(3)
		# ===============================

		try:
			i = data.header.seq%self.numero_maquinas
			# ===========DEBUG===============
			# print(i)
			# print(data.header.seq)
			# print(self.right_pubs)
			# print(self.right_pubs[i])
			# ===============================

			# Preparando mensaje imagen izquierda
			left_msg = self.bridge.cv2_to_compressed_imgmsg(cv_left, dst_format='jpeg')
			left_msg.header = data.header
			left_msg.header.frame_id = "/stereo/left"
			#left_msg.height = rows
			#left_msg.width = cols//2
			left_info = yaml_to_CameraInfo("/home/jgarruchof/.ros/camera_info/left.yaml")
			left_info.header = left_msg.header

			# Publicando mensajes imagen izquierda
			self.left_pubs[i].publish(left_msg)
			self.left_info_pubs[i].publish(left_info)


			# Preparando mensaje imagen derecha
			right_msg = self.bridge.cv2_to_compressed_imgmsg(cv_right, dst_format='jpeg')
			right_msg.header = data.header
			right_msg.header.frame_id = "/stereo/right"
			#right_msg.height = rows
			#right_msg.width = cols//2
			right_info = yaml_to_CameraInfo("/home/jgarruchof/.ros/camera_info/right.yaml")
			right_info.header = right_msg.header

			# Publicando mensajes imagen derecha

			self.right_pubs[i].publish(right_msg)
			self.right_info_pubs[i].publish(right_info)

		except CvBridgeError as e:
			print(e)


def main(args):
	ic = image_converter(numero_maquinas=int(args[1]))
	rospy.init_node('cam2stereo', anonymous=True)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()

if __name__ == '__main__':
	args = rospy.myargv(argv=sys.argv)

	main(args)

