import logging
import time
import RPi.GPIO as gpio
import spidev

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
		
		self.stepPin = int(properties.getStepPin())
		self.dirPin = int(properties.getDirectionPin())
		self.enablePin = int(properties.getEnablePin())
		
	def initializeDroneStation(self):
		if (self.initialized == False):
			self.initialized = True
			self.oldMircoseconds = time.time() * 1000
			gpio.setmode(gpio.BOARD)
			gpio.setup(self.stepPin, gpio.OUT)
			gpio.setup(self.dirPin, gpio.OUT)
			gpio.setup(self.enablePin, gpio.OUT)
			gpio.output(self.dirPin, True)
			gpio.output(self.enablePin, False)
	
	def evaluateRotation(self):
		if (self.initialized and self.rotate):
			#self.newMicroseconds = time.time() * 1000
			#if ((self.newMicroseconds - self.oldMircoseconds) >= 10):
				#self.oldMircoseconds = self.newMicroseconds
				#gpio.output(self.stepPin, not gpio.input(self.stepPin))
				#time.sleep(0.01)
			gpio.output(self.stepPin, True)
			time.sleep(0.001)
			gpio.output(self.stepPin, False)

	def startRotation(self):
		if (self.initialized):
			self.logger.info("Start Rotating Drone Station...")
			self.rotate = True

	def stopRotation(self):
		if (self.initialized):
			self.logger.info("Stop Rotating Drone Station...")
			self.rotate = False
			gpio.output(self.stepPin, False)

	def shutdown(self):
		if (self.initialized):
			self.stopRotation()
