#! /usr/bin/python3
# Author: Maximilian Muth <mail@maxi-muth.de>
# https://github.com/mammuth/bing-wallpaper
# Version: 1.0
# License: GPL-2.0
# Description: Downloads the Bing picture of the Day and sets it as wallpaper (Linux / Windows).

import datetime
from urllib.request import urlopen, urlretrieve
from xml.dom import minidom
import os
import sys


def join_path(*args):
    # Takes an list of values or multiple values and returns an valid path.
    if isinstance(args[0], list):
        path_list = args[0]
    else:
        path_list = args
    val = [str(v).strip(' ') for v in path_list]
    return os.path.normpath('/'.join(val))

dir_path = os.path.dirname(os.path.realpath(__file__))
save_dir = join_path(dir_path, 'images')
if not os.path.exists(save_dir):
    os.makedirs(save_dir)


def set_windows_wallpaper(pic_path):
    print("Remove TranscodedImageCache from registry")
    os.system('REG DELETE \"HKCU\Control Panel\Desktop\" /v TranscodedImageCache /f')

    print("\nSet image in registry")
    cmd = 'REG ADD \"HKCU\Control Panel\Desktop\" /v Wallpaper /t REG_SZ /d \"%s\" /f' % pic_path
    os.system(cmd)

    print("\nClean theme cached image folders")
    os.system("del /F /Q %AppData%\Microsoft\Windows\Themes\CachedFiles")
    os.system("del /F /Q %AppData%\Microsoft\Windows\Themes\TranscodedWallpaper")

    # refresh user params
    os.system('rundll32.exe user32.dll, UpdatePerUserSystemParameters')
    print('Wallpaper is set.')


def set_linux_wallpaper(pic_path):
    os.system(''.join(['gsettings set org.gnome.desktop.background picture-uri file://', pic_path]))
    print('Wallpaper is set.')


def set_wallpaper(pic_path):
    if sys.platform.startswith('win32'):
        set_windows_wallpaper(pic_path)
    elif sys.platform.startswith('linux'):
        set_linux_wallpaper(pic_path)
    else:
        print('OS not supported.')


def download_old_wallpapers(minus_days=False):
    """Uses download_wallpaper(set_wallpaper=False) to download the last 20 wallpapers.
    If minus_days is given an integer a specific day in the past will be downloaded.
    """
    if minus_days:
        download_wallpaper(idx=minus_days, use_wallpaper=False)
        return
    for i in range(0, 20):  # max 20
        download_wallpaper(idx=i, use_wallpaper=False)


def download_wallpaper(idx=0, use_wallpaper=True):
    # Getting the XML File
    try:
        usock = urlopen(''.join(['http://www.bing.com/HPImageArchive.aspx?format=xml&idx=',
                                 str(idx), '&n=1&mkt=ru-RU']))  # ru-RU, because they always have 1920x1200 resolution
    except Exception as e:
        print('Error while downloading #', idx, e)
        return
    try:
        xmldoc = minidom.parse(usock)
    # This is raised when there is trouble finding the image url.
    except Exception as e:
        print('Error while processing XML index #', idx, e)
        return
    # Parsing the XML File
    for element in xmldoc.getElementsByTagName('url'):
        url = 'http://www.bing.com' + element.firstChild.nodeValue
        # Get Current Date as fileName for the downloaded Picture
        now = datetime.datetime.now()
        date = now - datetime.timedelta(days=int(idx))
        pic_path = join_path(save_dir, ''.join([date.strftime('bing_wp_%d-%m-%Y'), '.jpg']))
        if os.path.isfile(pic_path):
            print('Image of', date.strftime('%d-%m-%Y'), 'already downloaded.')
            if use_wallpaper:
                set_wallpaper(pic_path)
            return
        print('Downloading: ', date.strftime('%d-%m-%Y'), 'index #', idx)

        # Download and Save the Picture
        # Get a higher resolution by replacing the file name
        urlretrieve(url.replace('_1366x768', '_1920x1200'), pic_path)
        # Set Wallpaper if wanted by user
        if use_wallpaper:
            set_wallpaper(pic_path)


if __name__ == "__main__":
    download_wallpaper()
    # download_old_wallpapers(minus_days=False)
