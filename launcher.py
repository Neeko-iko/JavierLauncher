from Internals import updater, jdb
jdb.deploy()
currVersion = jdb.readSettingValue('LastVersion')
currVersion = '1.9.0' #delete this line before shipping
ucResult = updater.updateCheck(currVersion)
if ucResult != False:
  updater.update(ucResult)