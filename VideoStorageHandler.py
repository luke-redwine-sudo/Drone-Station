import os
import logging
import time
import subprocess
import shlex
import signal
import multiprocessing

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
		
		self.recordingProcess = None
		
		self.camerapid = None
		
		
		
		
	def initializeVideoStorage(self):
		
		if (self.initialized == False):
			self.updateFolderNumber()
			self.initialized = True
	
	def updateFolderNumber(self):
		self.folder = str(properties.getVideoFolder())
		self.max_video_number = 1
			
		if (os.path.isdir(self.folder)):
			dir_list = os.listdir(self.folder)
			
			for f in dir_list:
				self.logger.info(f)
				if (str(properties.getVideoFilePrefix()) in f and int(f.split("_")[1].split(".")[0]) >= self.max_video_number):
					self.logger.info("Increasing Video Level...")
					self.max_video_number = int(f.split("_")[1].split(".")[0]) + 1
				elif(os.path.exists(self.folder) == False):
					os.makedirs(self.folder)
		
		self.filename = self.folder + str(properties.getVideoFilePrefix()) + "_{0:0=2d}".format(self.max_video_number) + ".avi"	
		
		self.commandString = "ffmpeg -f video4linux2 -framerate 22.5 -s 640x480 -i /dev/video0 " + self.filename
	
	def startVideoCollection(self):
		
		if (self.initialized == True):
			self.updateFolderNumber()
		
		self.camera = subprocess.Popen(shlex.split(self.commandString), stdout=subprocess.DEVNULL, shell=False)
		self.camerapid = self.camera.pid
		self.recordingProcess = multiprocessing.Process(target=self.startVideo)
		self.recordingProcess.start()
	
	def stopVideoCollection(self):
		self.stopVideo()
	
	def startVideo(self):
		self.camera.wait()
		
	def stopVideo(self):
		if (self.initialized == True):
			self.camera.terminate()
			

	def shutdown(self):
		
		self.logger.info("Shutdown Video Storage Handler...")
		
		if (self.initialized == True):
			self.stopVideo()
			
