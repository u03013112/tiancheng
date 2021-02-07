from cv2 import cv2
import sys
import time
import math
import threading
import numpy as np

class Camera(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url
        self.ready = 0
        self.isQuit = False
    def close(self):
        self.isQuit = True
    def run(self):
        try:
            while self.isQuit == False:
                try:
                    camera=cv2.VideoCapture(self.url)
                    self.camera = camera
                except Exception as e:
                    print('Error:',e)
                    self.camera = None
                    time.sleep(1)
                    continue
                print('connected successed!')

                while self.isQuit == False:
                    if camera.isOpened():
                        success,frame = camera.read()
                        if success==False:
                            print('camera read err!')
                            time.sleep(1)
                            break
                        self.frame = frame
                        self.ready = 1
                    else:
                        print('camera not open!')
                        time.sleep(1)
                        break

                camera.release()
        except KeyboardInterrupt:
                self.isQuit = True
                print('received an ^C and exit.')

if __name__ == '__main__':
    camera=Camera()
    camera.start()
   