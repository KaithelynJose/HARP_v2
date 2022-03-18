
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
    
    ## Main Functions Here
    arg.pageShowInc = 0;

    # Make Listbox Multiselect
    arg.handles.pg_main.projects.obj.config(selectmode='multiple')

    arg.projects = [path for path in sorted(os.listdir('database')) if os.path.isdir('database/' + path)]
    
    # Populate Data
    gui.listbox_data(arg, arg.handles.pg_main.projects, arg.projects)

    return True

def postshow(arg):
    return True


def newProject(arg):
    gui.showPage(arg,'pg_newProject')


def viewProject(arg):
    selection = arg.handles.pg_main.projects.obj.curselection()

    if len(selection) == 0:
        gui.msgbox(arg, "No project selected.",
            MessageBoxButtons = "ok",
            MessageBoxIcon = "error",
        )
        return
    
    if len(selection) > 1:
        gui.msgbox(arg, "Choose only one project.",
            MessageBoxButtons = "ok",
            MessageBoxIcon = "error",
        )
        return
    
    idx = selection[0]

    arg.currentProject = arg.projects[idx]

    gui.showPage(arg, 'pg_project')

def deleteProject(arg):
    selection = arg.handles.pg_main.projects.obj.curselection()

    if len(selection) == 0:
        gui.msgbox(arg, "No project selected.",
            MessageBoxButtons = "ok",
            MessageBoxIcon = "error",
        )
        return
    
    if len(selection) == 1:

        idx = selection[0]
        userRsp = gui.msgbox(arg, 'Are you sure to delete project: "' + arg.projects[idx] + '"?',
                MessageBoxButtons = "yesno",
                MessageBoxIcon = "question",
            )
        if not userRsp == 'yes':
            return

        shutil.rmtree('database/' + arg.projects[idx])
    
    else:

        userRsp = gui.msgbox(arg, 'Are you sure to delete ' + str(len(selection)) + ' projects?',
                MessageBoxButtons = "yesno",
                MessageBoxIcon = "question",
            )
        if not userRsp == 'yes':
            return
        
        for idx in selection:
            shutil.rmtree('database/' + arg.projects[idx])
    
    

    gui.showPage(arg, 'pg_main')


    
def shutDown(arg):

    userRsp = gui.msgbox(arg, "Shut down HARP?",
        MessageBoxButtons = "yesno",
        MessageBoxIcon = "question",
    )

    if not userRsp == "yes":
        return
    os.system('sudo shutdown -h now')