
from platform import libc_ver
import scipy.fftpack as sf
from scipy.io import wavfile
import scipy.signal as signal
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import glob
import shutil
from pdf2image import convert_from_path
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

sys.path.append("..")
sys.path.append("../plugins")
sys.path.append("../pages")
sys.path.append("../system")

## IMPORT PLUGINS AND MODULES
import g, gui, styles
import time
import _thread
import cv2


class ScrollableImage(tk.Frame):
    def __init__(self, master=None, **kw):
        self.image = kw.pop('image', None)
        sw = kw.pop('scrollbarwidth', 10)
        super(ScrollableImage, self).__init__(master=master, **kw)
        self.cnvs = tk.Canvas(self, highlightthickness=0, **kw)
        self.cnvs.create_image(0, 0, anchor='nw', image=self.image)
        # Vertical and Horizontal scrollbars
        self.v_scroll = tk.Scrollbar(self, orient='vertical', width=sw)
        self.h_scroll = tk.Scrollbar(self, orient='horizontal', width=sw)
        # Grid and configure weight.
        self.cnvs.grid(row=0, column=0,  sticky='nsew')
        self.h_scroll.grid(row=1, column=0, sticky='ew')
        self.v_scroll.grid(row=0, column=1, sticky='ns')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # Set the scrollbars to the canvas
        self.cnvs.config(xscrollcommand=self.h_scroll.set, 
                           yscrollcommand=self.v_scroll.set)
        # Set canvas view to the scrollbars
        self.v_scroll.config(command=self.cnvs.yview)
        self.h_scroll.config(command=self.cnvs.xview)
        # Assign the region to be scrolled 
        self.cnvs.config(scrollregion=self.cnvs.bbox('all'))
        self.cnvs.bind_class(self.cnvs, "<MouseWheel>", self.mouse_scroll)

    def mouse_scroll(self, evt):
        if evt.state == 0 :
            self.cnvs.yview_scroll(-1*(evt.delta), 'units') # For MacOS
            self.cnvs.yview_scroll(int(-1*(evt.delta/120)), 'units') # For windows
        if evt.state == 1:
            self.cnvs.xview_scroll(-1*(evt.delta), 'units') # For MacOS
            self.cnvs.xview_scroll(int(-1*(evt.delta/120)), 'units') # For windows


def preshow(arg):
    if "quickpreview" in arg.__dict__:
        ## Quick View Functions Here
    
        return True
    
    toDelete = glob.glob('page*.jpg')
    toDelete.extend(glob.glob('pdf2show.jpg'))

    for item in toDelete:
        os.remove(item)
    
    while True:
        for item in toDelete:
            if os.path.exists(item):
                continue
        break

    # Store Pdf with convert_from_path function
    if g.os == "win":
        images = convert_from_path('./exports/' + arg.currentRecord, poppler_path="../poppler-0.68.0/bin")
    else:
        images = convert_from_path('./exports/' + arg.currentRecord)
    
    for idx, img in enumerate(images):
        img.save('page'+ str(idx) +'.jpg', 'JPEG')
        if idx==0:
            newImg = cv2.imread('page'+ str(idx) +'.jpg')
        else:
            newImg = cv2.vconcat([newImg, np.ones((50,newImg.shape[1],3), dtype=np.uint8) * 200])
            newImg = cv2.vconcat([newImg, cv2.imread('page'+ str(idx) +'.jpg')])
    
    cv2.imwrite('pdf2show.jpg', newImg)

    width = 650
    height = 410
    img = Image.open('pdf2show.jpg')
    imgW, imgH = img.size
    img = img.resize((width, int(round(imgH * width / imgW))))

    img = ImageTk.PhotoImage(img)

    arg.pdfWindow = ScrollableImage(arg.master, image=img, scrollbarwidth=g.scrollWidth, 
                                width=width, height=height)
    arg.pdfWindow.place(x=20, y=50, w=width, h=height)

    ## Main Functions Here
    arg.handles.pg_pdf.labelTitle.obj.config(text='PDF File: ' + arg.currentRecord)

    

    return True

def postshow(arg):
    return True


def btnBack(arg):
    arg.pdfWindow.place_forget()
    gui.showPage(arg, 'pg_project')