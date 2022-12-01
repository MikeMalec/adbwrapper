import os
import subprocess

class ADBWrapper:

    def __init__(self):
        self.androidCameraPath = "/storage/self/primary/DCIM/Camera"
        self.androidScreenShotsPath = "/storage/self/primary/DCIM/Screenshots"
        os.system("adb devices")
    
    def copyCameraPhotos(self, path, latestFile):
        if latestFile:
            fileName = self.getLatestFileName(self.androidCameraPath)
            filePath = self.androidCameraPath + "/" + fileName
            os.system('adb pull {filePath} {path}'.format(filePath = filePath, path = path))
        else:        
            os.system("adb pull {androidCameraPath} {path}".format(androidCameraPath = self.androidCameraPath, path = path))

    def copyScreenShots(self, path, latestFile):
        if latestFile:
            fileName = self.getLatestFileName(self.androidScreenShotsPath)
            filePath = self.androidScreenShotsPath + "/" + fileName
            os.system("adb pull {filePath} {path}".format(filePath = filePath, path = path))
        else:
            os.system("adb pull {androidScreenShotsPath} {path}".format(androidScreenShotsPath = self.androidScreenShotsPath, path = path))        

    def getLatestFileName(self, path):
        commands = """
            adb shell
            cd {path}
            ls -latr | tail -1 | awk '{{ print  $8 }}' 
            exit
        """.format(path = path)

        process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = process.communicate(commands.encode('utf-8'))
        return out.decode('utf-8').strip()

        
