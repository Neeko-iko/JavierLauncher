#!/usr/bin/python3
from Internals import jdb
from sys import platform
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