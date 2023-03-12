import logging

import DroneStationProperties

properties = DroneStationProperties.DroneStationProperties()

class DroneStationHandler:
	
	def __init__(self):
		
		# Initialize logger
		logging.basicConfig(filename=str(properties.getLoggingFolder()) + "VideoStorageHandler.log", format='%(asctime)s %(module)s %(levelname)s - %(message)s', filemode='w')
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.DEBUG)
		
		self.logger.info("Initializing Video Station Handler...")
		
		self.initialized = False
		
	def initializeDroneStation(self):
		
		if (self.initialized == False):
			self.initialized = True
	
	def evaluateRotation(self):
		self.logger.info("Rotate")
	
	def startRotation(self):
		self.logger.info("Start Rotating Drone Station...")

	def stopRotation(self):
		self.logger.info("Stop Rotating Drone Station...")

	def shutdown(self):
		self.stopRotation()
