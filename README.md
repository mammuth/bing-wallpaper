Bing-Wallpaper
==============

A Python3 script to set the daily background image of www.bing.com as desktop allpaper on Linux or Windows.

Works fine with Ubuntu 13.10 (Unity and Gnome3).
KDE is not supported yet.
By testing it in Win7 I experienced a reset of the wallpaper after rebooting.


### HowTo Use:

Just run ```python3 bing_wallpaper.py```
 
The images will be stored in an _image/_ folder.


### Automate it! (Linux) 
Make something like the following starting at boot time, to automate the process (change the paths to your needs):

```bash
#! /bin/bash
DATE=`date +%d-%m-%Y`
#only start the script if the todays picture doesn't exists
if [ ! -a /pathTo/saveDir/bing_wp_$DATE".jpg" ]; then
	python3 /pathTo/pythonScript/bing_wallpaper.py
fi
```


### Note:
This isn't really finished, (especially regarding compatibility) but maybe this already is useful for someone.
If you have any questions or ideas how to improve this, tell me! ;-)
