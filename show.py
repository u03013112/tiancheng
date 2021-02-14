#!/usr/bin/python3 
import tkinter as tk
from cv2 import cv2
# from camera import Camera
from ffplayer import Camera
from PIL import Image, ImageDraw, ImageFont,ImageTk
import pyperclip

class Show():
    def __init__(self,root,title,url):
        self.windowW=360
        self.windowH=640

        self.isMute = False

        self.url=url
        # window = tk.Tk()
        if root != None:
            window = tk.Toplevel(root)
        window.title(title)
        window.geometry(str(self.windowW)+'x'+str(self.windowH))
        window["bg"] = "pink"
        
        self.window = window

        preview = tk.Label(self.window)
        preview.place(x=0,y=0,width=self.windowW,height=self.windowH)
        self.preview = preview
        
        # dt = 15
        dt = 33
        def winUpdate():
            # print(title,"update")
            self.window.after(dt,winUpdate)
            self.update()
        self.window.after(dt,winUpdate)

        self.camera = Camera(url)
        self.camera.start()

        def on_closing():
            self.camera.close()
            self.window.destroy()

        window.protocol("WM_DELETE_WINDOW", on_closing)
        def didCopyBtnClicked():  
            pyperclip.copy(self.url)
        copyBtn = tk.Button(window,text='复制直播地址至粘贴板',command=didCopyBtnClicked)
        copyBtn.place(x=5,y=2,width=200, height=23)

        def didMuteBtnClicked():
            if self.isMute == True:
                self.isMute = False
                self.camera.player.set_volume(1.0)
                self.muteBtn.configure(text='静音')
            else:
                self.isMute = True
                self.camera.player.set_volume(0.0)
                self.muteBtn.configure(text='开音')
        muteBtn = tk.Button(window,text='静音',command=didMuteBtnClicked)
        muteBtn.place(x=300,y=2,width=50, height=23)
        self.muteBtn = muteBtn


    def frame2Mtk(self,frame):
        w,h,_ = frame.shape
        # 直接拉伸
        if w != self.windowW or h != self.windowH:
            frame = cv2.resize(frame,(self.windowW, self.windowH))

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(image)
        imgtk = ImageTk.PhotoImage(image=im)
        return imgtk
    def setPreview(self,frame):
        self.preview.configure(image=frame)
        self.preview.image = frame
    def update(self):
        if self.camera.ready != 0:
            self.setPreview(self.camera.frame)
    def show(self):
        self.window.mainloop()

if __name__ == '__main__':
    show=Show('啤酒瓶插逼','rtmp://pull.liangholding.com/live/5939243_1612712447?txSecret=01eeb8c82592855127ea552b08e03ce1&txTime=60202C43')
    show.show()