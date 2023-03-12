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
		
	def getCommandString(self):
		return self.configs.get("dronestation.command_string").data
		
	def getFramerate(self):
		return self.configs.get("dronestation.framerate").data
		
	def getResolution(self):
		return self.configs.get("dronestation.resolution").data
		
	def getSource(self):
		return self.configs.get("dronestation.source").data
		
	def getTotalCommandString(self):
		return self.getCommandString() + " " + self.getFramerate() + " -s " + self.getResolution() + " -i " + self.getSource()

	def getStepPin(self):
		return self.configs.get("dronestation.step_pin").data
		
	def getDirectionPin(self):
		return self.configs.get("dronestation.direction_pin").data
