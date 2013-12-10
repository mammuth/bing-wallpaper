#! /usr/bin/python3
﻿# Author: Maximilian Muth <mail@maxi-muth.de>
﻿# Version: 1.0 
﻿# License: GPL-3.0 
﻿# Description: Download the Bing Picture of the Day and set it as (Linux / Windows) wallpaper.
﻿
import datetime
from urllib.request import urlopen, urlretrieve
from xml.dom import minidom
import os


#Variables:
idx = '0' #defines the day of the picture: 0 = today, 1 = yesterday, ... 20.
saveDir = '/media/HDD/ProgrammingStuff/Python/BingWallpaper/' #in Windows put 2 \\ at the end
operatingSystem = 'linux' # windows and linux (gnome)



#Methods for setting a picture as Wallpaper
def setWindowsWallpaper(picPath):
	cmd = 'REG ADD \"HKCU\Control Panel\Desktop\" /v Wallpaper /t REG_SZ /d \"%s\" /f' % (picPath)
	os.system(cmd)
	os.system('rundll32.exe user32.dll, UpdatePerUserSystemParameters')
	return
	
def setGnomeWallpaper(picPath):
	os.system('gsettings set org.gnome.desktop.background picture-uri file://'+picPath)
	return


#Getting and Parsing the XML File
usock = urlopen('http://www.bing.com/HPImageArchive.aspx?format=xml&idx='+idx+'&n=1&mkt=ru-RU') #ru-RU, because they always have 1920x1200 resolution pictures
xmldoc = minidom.parse(usock)

for element in xmldoc.getElementsByTagName('url'):
	url = bing+element.firstChild.nodeValue
  
	#Get Current Date as fileName for the downloaded Picture
	now = datetime.datetime.now()
	picPath = saveDir+now.strftime('bing_wp_%d-%m-%Y')+'.jpg'
	
	#Download and Save the Picture
	#Get a higher resolution by replacing the image name
	urlretrieve (url.replace('_1366x768', '_1920x1200'), picPath)
	
	#Set Wallpaper:
	if operatingSystem == 'windows':
		setWindowsWallpaper(picPath)
	elif operatingSystem == 'linux' or operatingSystem == 'gnome':
		setGnomeWallpaper(picPath)  
