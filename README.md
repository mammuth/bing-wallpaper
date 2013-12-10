Bing-Wallpaper
==============

A Python3 Script to set the daily background image of www.bing.com as Desktop Wallpaper of Linux or Windows.

Works fine with Ubuntu 13.10 (Unity and Gnome3).
KDE is not supported yet.
By testing it in Win7 I experienced a reset of the wallpaper after rebooting.


#### HowTo Use:

Just take a look at the 2-3 variables at the beginning of the script and change them to your needs. 
The Script will download the daily pictures, so a extra directory for it is recommended.


#### Note:
This isn't really finished, (especially regarding compatibility) but maybe this already is useful for someone.
If you have any questions or ideas how to improve this, tell me! ;-)


#### Additional tip:
###### Automate it! (Linux) 
Make something like the following starting at boot time, to automate the process (change the paths to your needs):

```bash
#! /bin/bash
DATE=`date +%d-%m-%Y`
#only start the script if the todays picture doesn't exists
if [ ! -a /pathTo/saveDir/bing_wp_$DATE".jpg" ]; then
	python3 /pathTo/pythonScript/bing-wallpaper.py
fi
```
