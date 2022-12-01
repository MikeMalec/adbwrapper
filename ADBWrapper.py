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
            os.system(f"adb pull {filePath} {path}")
        else:        
            os.system(f"adb pull {self.androidCameraPath} {path}")

    def copyScreenShots(self, path, latestFile):
        if latestFile:
            fileName = self.getLatestFileName(self.androidScreenShotsPath)
            filePath = self.androidScreenShotsPath + "/" + fileName
            os.system(f"adb pull {filePath} {path}")
        else:
            os.system(f"adb pull {self.androidScreenShotsPath} {path}")        

    def getLatestFileName(self, path):
        commands = f"""
            adb shell
            cd { path }
            ls -latr | tail -1 | awk '{{ print  $8 }}' 
            exit
        """

        process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = process.communicate(commands.encode('utf-8'))
        return out.decode('utf-8').strip()

        
