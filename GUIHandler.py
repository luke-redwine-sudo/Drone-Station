from random import randint
import logging
import sys

import VideoStorageHandler
import DroneStationHandler
import DroneStationProperties

properties = DroneStationProperties.DroneStationProperties()

class GUIHandler:
	
	def __init__(self, root, dronePhoneRotationButton, videoButton):
		
		# Initialize self variables
		self.root = root
		self.dronePhoneRotationButton = dronePhoneRotationButton
		self.videoButton = videoButton
		self.isRecording = False
		self.isRotation = False
		
		# Initialize logger
		logging.basicConfig(filename=str(properties.getLoggingFolder()) + "GUIHandler.log", disable_existing_loggers=False, format='%(asctime)s %(module)s %(levelname)s - %(message)s', filemode='w')
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.DEBUG)
		
		self.logger.info("Initializing GUI Handler...")
		
		# Initialize Handlers
		self.VideoStorageHandler = VideoStorageHandler.VideoStorageHandler()
		self.DroneStationHandler = DroneStationHandler.DroneStationHandler()
		
		
	def startVideoCollection(self):
		# Initialize Camera
		self.logger.info("Starting Video Collection...")
		
		if (self.VideoStorageHandler.initialized is not True):
			self.VideoStorageHandler.initializeVideoStorage()
		
		self.VideoStorageHandler.startVideo()
		
	def endVideoCollection(self):
		# Shutdown Camera
		self.logger.info("Ending Data Collection...")
		self.VideoStorageHandler.stopVideo()
		
	def toggleDronePhoneRotation(self):
		if (self.isRotation):
			self.stopDronePhoneRotation()
			self.dronePhoneRotationButton.configure(text="Start Rotation", fg_color='green')
		else:
			self.startDronePhoneRotation()
			self.dronePhoneRotationButton.configure(text="Stop Rotation", fg_color='orange')
			
		self.isRotation = not self.isRotation
	
	def toggleVideoCollection(self):
		if (self.isRecording):
			self.stopVideoCollection()
			self.videoButton.configure(text="Start Recording", fg_color='green')
		else:
			self.startVideoCollection()
			self.videoButton.configure(text="Stop Recording", fg_color='orange')
			
		self.isRecording = not self.isRecording
		
	def startDronePhoneRotation(self):
		self.DroneStationHandler.startRotation()
		
	def stopDronePhoneRotation(self):
		self.DroneStationHandler.stopRotation()
		
	def shutdown(self):
		self.logger.info("Commense Shutdown...")
		
		# Shutdown sensors and close window
		self.DroneStationHandler.shutdown()
		
		if (self.VideoStorageHandler != None):
			self.VideoStorageHandler.shutdown()	
		
		
		self.root.quit()
