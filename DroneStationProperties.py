from jproperties import Properties

class DroneStationProperties:
	
	def __init__(self):
		self.configs = Properties()
		with open('DroneStation.properties', 'rb') as config_file:
			self.configs.load(config_file)
	
	def getLoggingFolder(self):
		return self.configs.get("dronestation.logging_folder").data
		
	def getVideoFolder(self):
		return self.configs.get("dronestation.video_folder").data
		
	def getVideoFileSize(self):
		return self.configs.get("dronestation.video_file_size").data
		
	def getVideoFilePrefix(self):
		return self.configs.get("dronestation.video_file_prefix").data
		

