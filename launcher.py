from Internals import updater, jdb
from sys import platform
jdb.deploy()
currVersion = jdb.readSettingValue('LastVersion')
ucResult = updater.updateCheck(currVersion)
if ucResult != False:
  if platform == 'win32':
    updater.update(ucResult)
  else:
    print("An update is required.")
else:
  import Javier