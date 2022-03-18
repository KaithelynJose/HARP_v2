
from platform import libc_ver
import scipy.fftpack as sf
from scipy.io import wavfile
from scipy.signal import find_peaks
import numpy as np
import sys
from matplotlib import pyplot as plt
import os
import pyaudio
import math
import wave
from tkinter import font

asciiFont = font.Font(family="Courier New", size="24")

sys.path.append("..")
sys.path.append("../plugins")
sys.path.append("../pages")
sys.path.append("../system")

## IMPORT PLUGINS AND MODULES
import g, gui, styles
import time
import _thread


def preshow(arg):
    if "quickpreview" in arg.__dict__:
        ## Quick View Functions Here
    
        return True
    

    arg.handles.pg_record.labelTitle.obj.config(text="Record: " + arg.currentRecord)

    with open('database/' + arg.currentProject + '/' + arg.currentRecord, 'r') as fid:
        asciiLines = fid.readlines()
    
    gui.listbox_data(arg, arg.handles.pg_record.ascii, asciiLines)
    arg.handles.pg_record.ascii.obj.config(font=asciiFont)

    return True

def postshow(arg):
    return True

def back(arg):
    gui.showPage(arg, 'pg_project')

