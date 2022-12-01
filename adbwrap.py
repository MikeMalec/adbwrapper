import sys
from ADBWrapper import ADBWrapper

type = 'ss'
path = '~/Desktop' 
latestFile = False

for arg in sys.argv:
    if "type" in arg:
        type = arg.split("=")[1]        
    elif "path" in arg:
        path = arg.split("=")[1]
    elif "latest" in arg:
        latestFile = True

adbWrapper = ADBWrapper()
 
if type == 'camera':
    adbWrapper.copyCameraPhotos(path, latestFile)
elif type == 'ss':
    adbWrapper.copyScreenShots(path, latestFile)

