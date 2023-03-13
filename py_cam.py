import tkinter as tk
import cv2
import numpy as np
from PIL import Image, ImageTk
import os
from datetime import datetime
import time  

time_stamp = time.time()
time_stamp = 1617295943.17321



root= tk.Tk()
win = tk.Tk()


# imgrgb = cv2.imread("game\Resources\Bloons TD6 03.jpg",1)
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()
# os.chdir("D:\\vishnu2\\python\\py_cam")
os.chdir(os.getcwd())
def hello ():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #0 for webcam, 1 for external camera and so on
    cap.set(3, 1280) #width
    cap.set(4, 720) #heights
    success, imgrgb = cap.read()
    
      
    cv2.imshow('Looking Good',imgrgb) 
    # 
    cap.release()

    date_time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    print(date_time)
    cv2.imwrite('Photo_'+date_time+'.jpg',imgrgb)

    label1 = tk.Label(root, text= 'Looking Good!',bg = 'purple', fg='green', font=('comicSans', 20, 'italic'))
    canvas1.create_window(150, 200, window=label1)
    win.mainloop()
    
    
    
button1 = tk.Button(text='Click Me to Capture!',height= 10,width= 30, command=hello, bg='purple',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()