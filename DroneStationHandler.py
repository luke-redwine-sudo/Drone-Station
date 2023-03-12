import logging
import time
import RPi.GPIO as gpio

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
		
		self.rotate = False
		
		self.stepPin = properties.getStepPin()
		self.dirPin = properties.getDirectionPin()
		
	def initializeDroneStation(self):
		if (self.initialized == False):
			self.initialized = True
			self.oldMircoseconds = time.time() * 1000
			GPIO.setmode(gpio.BOARD)
			gpio.setup(self.stepPin, gpio.out)
			gpio.setup(self.dirPin, gpio.out)
			gpio.output(self.dirPin, True)
	
	def evaluateRotation(self):
		
		if (self.initialized and self.rotate):
			self.newMicroseconds = time.time() * 1000
			if ((self.newMicroseconds - self.oldMicroseconds) >= 300):
				self.oldMicroseconds = self.newMicroseconds
				gpio.output(self.stepPin, not GPIO.input(self.stepPin))
				print("Rotate")

	def startRotation(self):
		if (self.initialized):
			self.logger.info("Start Rotating Drone Station...")
			self.rotate = True

	def stopRotation(self):
		if (self.initialized):
			self.logger.info("Stop Rotating Drone Station...")
			self.rotate = False

	def shutdown(self):
		if (self.initialized):
			self.stopRotation()
