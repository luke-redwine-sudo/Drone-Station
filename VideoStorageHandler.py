import os
import logging
#import pirecorder
import time

import DroneStationProperties

properties = DroneStationProperties.DroneStationProperties()

class VideoStorageHandler:
	
	def __init__(self):
		
		# Initialize logger
		logging.basicConfig(filename=str(properties.getLoggingFolder()) + "VideoStorageHandler.log", disable_existing_loggers=False, format='%(asctime)s %(module)s %(levelname)s - %(message)s', filemode='w')
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.DEBUG)
		
		self.logger.info("Initializing Video Storage Handler...")
		
		self.initialized = False
		
		self.camera = None
		
		
	def initializeVideoStorage(self):
		
		if (self.initialized == False):
			self.folder = str(properties.getVideoFolder())
			self.max_video_number = 1
			
			if (os.path.isdir(self.folder)):
				dir_list = os.listdir(self.folder)
				
				for f in dir_list:
					self.logger.info(f)
					if (str(properties.getVideoFilePrefix()) in f and int(f.split("_")[1].split(".")[0]) >= self.max_video_number):
						self.logger.info("Increasing Log Level...")
						self.max_video_number = int(f.split("_")[1].split(".")[0]) + 1
				
			else:
				os.makedirs(self.folder)
			
			self.filename = self.folder + str(properties.getVideoFilePrefix()) + "_{0:0=2d}".format(self.max_video_number) + ".mp4"

			#self.startVideo()

			self.initialized = True
	
	def startVideo(self):
		self.camera = rec.set_config(rectype = "vid", viddelay = 20, vidquality = 30, viddims = (1640, 1232), vidfps = 24)
		self.camera.record()
		
	def stopVideo(self):
		self.max_video_number = self.max_video_number + 1
		self.filename = self.folder + str(properties.getVideoFilePrefix()) + "_{0:0=2d}".format(self.max_video_number) + ".mp4"
		
		if (self.initialized == True):
			self.camera.stop_recording()

	def shutdown(self):
		
		self.logger.info("Shutdown Video Storage Handler...")
		
		if (self.initialized == True):
			self.stopVideo()
			
