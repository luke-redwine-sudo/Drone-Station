from tkinter import *
import customtkinter
from threading import Thread
from PIL import ImageTk, Image
import GUIHandler
import logging
import sys
import time
import math
import os
import DroneStationProperties

properties = DroneStationProperties.DroneStationProperties()

customtkinter.set_appearance_mode("dark")

if (os.path.isdir(str(properties.getLoggingFolder())) != True):
	os.mkdir(str(properties.getLoggingFolder()))

logging.basicConfig(filename=str(properties.getLoggingFolder()) + "DroneStation.log",
                    format='%(asctime)s %(module)s %(levelname)s - %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)  
handler.setFormatter(logging.Formatter('%(asctime)s %(module)s %(levelname)s - %(message)s'))                                  
logger.addHandler(handler)   

# Create Tkinter Object
root = customtkinter.CTk()
root.attributes('-fullscreen',True)

logger.info("Creating Tkinter Object...")
 
# Specify Grid
Grid.columnconfigure(root,0,weight=2)
Grid.columnconfigure(root,1,weight=1)
Grid.columnconfigure(root,3,weight=2)
Grid.rowconfigure(root,0,weight=10)
Grid.rowconfigure(root,1,weight=1)
Grid.rowconfigure(root,2,weight=5)
Grid.rowconfigure(root,3,weight=1)
Grid.rowconfigure(root,4,weight=1)
Grid.rowconfigure(root,5,weight=1)

logger.info("Specifying Grid...")

# Create Buttons
startButton = customtkinter.CTkButton(root,text="Start Video Collection", fg_color='green',
	command = lambda: guiHandler.startVideoCollection(), text_color="black",
	font=("Inter", 15))
endButton = customtkinter.CTkButton(root,text="End Video Collection", fg_color='yellow',
	command = lambda: guiHandler.endVideoCollection(), text_color="black",
	font=("Inter", 15))
exitButton = customtkinter.CTkButton(root,text="Exit", fg_color='red',
	command = lambda: guiHandler.shutdown(), text_color="black",
	font=("Inter", 15))
dronePhoneRotationButton = customtkinter.CTkButton(root,text="Start Rotation",
	fg_color='orange', command = lambda: guiHandler.toggleDronePhoneRotation(),
	text_color="black", font=("Inter", 15))

logger.info("Creating Buttons...")

# Create Image
logo = customtkinter.CTkImage(dark_image=Image.open("assets/logo.png"), size=(400, 300))
logoLabel = customtkinter.CTkLabel(root, text="", image=logo)
logoLabel.image = logo
droneStationLabel = customtkinter.CTkLabel(root, text="Drone Station GUI", font=("Inter", 25))

logging.info("Creating Image...")

# Set Image grid
logoLabel.grid(row=0,column=1,sticky="NSEW", padx=(20, 20), pady=(20, 1))
droneStationLabel.grid(row=1,column=1,sticky="NSEW", padx=(20, 20), pady=(1, 20))

# Set Button grid
startButton.grid(row=2,column=0,sticky="NSEW", padx=(20, 20), pady=(20, 20))
endButton.grid(row=2,column=1,sticky="NSEW", padx=(20, 20), pady=(20, 20))
exitButton.grid(row=5,column=2,sticky="NSEW", padx=(20, 20), pady=(20, 20))
dronePhoneRotationButton.grid(row=2,column=2,sticky="NSEW", padx=(20, 20), pady=(20, 20))

# Start GUI Handler
guiHandler = GUIHandler.GUIHandler(root, dronePhoneRotationButton)

logger.info("Enabling GUIHandler...")

#guiHandler.update()

# Execute tkinter
root.mainloop()

logger.info("Ending TKinter Mainloop...")

