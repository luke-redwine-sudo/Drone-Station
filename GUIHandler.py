from random import randint
import logging
import sys

import VideoStorageHandler
import DroneStationHandler
import DroneStationProperties

properties = DroneStationProperties.DroneStationProperties()

class GUIHandler:
	
	def __init__(self, root, dronePhoneRotationButton):
		
		# Initialize self variables
		self.root = root
		self.dronePhoneRotationButton = dronePhoneRotationButton
		self.collectData = False
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
		# Initialize Sensors
		self.logger.info("Starting Video Collection...")
		self.setCollectVideo(True)
		self.DroneStationHandler.initializeDroneStation()
		
	def endVideoCollection(self):
		# Shutdown sensors
		self.logger.info("Ending Data Collection...")
		self.setCollectVideo(False)

	def update(self):
		# Poll the sensors and update the read outs
		self.logger.debug("Updating Read outs...")
		
		# Only poll the sensors if data collection has started
		if (self.collectVideo == True):
			temperature, humidity, pressure = self.updateBMESensor()
			UV = self.updateUVSensor()
			windDirection, windSpeed = self.updateWindSensor()
			self.VideoStorageHandler.write()
			
		self.root.after(properties.getCollectionFrequency(), self.update)
		
	def setCollectVideo(self, collect):
		# Set collect video
		self.collectVideo = collect
		self.VideoStorageHandler.initializeVideoStorage()
		
	def getCollectVideo(self):
		# Return the current collection status
		return self.CollectVideo
		
	def toggleDronePhoneRotation(self):
		if (self.isRotation):
			self.stopDronePhoneRotation()
			self.dronePhoneRotationButton.configure(text="Start Rotation", fg_color='orange')
		else:
			self.startDronePhoneRotation()
			self.dronePhoneRotationButton.configure(text="Stop Rotation", fg_color='red')
			
		self.isRotation = not self.isRotation
	
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
