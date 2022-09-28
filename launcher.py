#!/usr/bin/python3
from sys import platform
from os import system
if platform == "linux":
  system("git pull")
from Internals import jdb
jdb.deploy()
currVersion = jdb.readSettingValue('LastVersion')
from Internals import updater
ucResult = updater.updateCheck(currVersion)
if ucResult != False:
  if platform == 'win32':
    updater.update(ucResult)
  else:
    print("An update is required.")
else:
  import Javier