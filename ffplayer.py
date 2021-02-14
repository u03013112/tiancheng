import time
import threading
from ffpyplayer.player import MediaPlayer
from PIL import Image,ImageTk
import numpy as np

class Camera(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        url = url + ' live=1'
        self.ready = 0
        self.isQuit = False
        self.player = MediaPlayer(url)
        self.player.set_size(360,640)
    def close(self):
        self.isQuit = True
    def run(self):
        try:
            while self.isQuit == False:
                frame, val = self.player.get_frame()
                if val == 'eof':
                    print('player get_frame eof')
                    break
                elif frame is None:
                    time.sleep(0.01)
                    # print('player get_frame None')
                else:
                    img, t = frame
                    w, h = img.get_size()
                    data = img.to_bytearray()[0]
                    img = np.asarray(img.to_bytearray()[0]).reshape(h,w,3)
                    im = Image.fromarray(img)
                    imgtk = ImageTk.PhotoImage(image=im)
                    self.frame = imgtk
                    time.sleep(val)
                    self.ready = 1
        except KeyboardInterrupt:
                self.isQuit = True
                print('received an ^C and exit.')
        self.player.close_player()

if __name__ == '__main__':
    camera=Camera()
    camera.start()
   