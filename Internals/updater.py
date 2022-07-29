import jdb
import requests
cv = jdb.readSettingValue('LastVersion')
def updateCheck(clientVersion):
  """
  Returns a release tag if an update is needed and False if not.
  """
  r = requests.get('https://api.github.com/repos/Neeko-iko/JavierLauncher/releases')
  rj = r.json()
  for i in range(0, 10):
    commitData = requests.get(rj[i]['url'])
    commitTag = commitData.json()['tag_name']
    if commitTag == clientVersion:
      return False
    elif 'lite' in commitTag:
      continue
    #semantic versioning processing time
    splCommitTag = commitTag.split('.')
    splClientVersion = clientVersion.split('.')
    if int(splCommitTag[0]) > int(splClientVersion[0]):
      return commitTag
    elif int(splCommitTag[1]) > int(splClientVersion[1]):
      return commitTag
    elif int(splCommitTag[2]) > int(splClientVersion[2]):
      return commitTag
    else:
      return False
def update(targetVers):
  print("This function is currently a stub (update() function)")
ucResult = updateCheck(cv)
if ucResult != False:
  update(ucResult)
