
from platform import libc_ver
import scipy.fftpack as sf
from scipy.io import wavfile
import scipy.signal as signal
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import glob

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

    return True

def postshow(arg):
    return True


def cancelAddProject(arg):
    gui.showPage(arg, 'pg_main')


def addProject(arg):
    projectName = arg.handles.pg_newProject.entryName.obj.get().strip()
    
    # Must be at least 3 characters long
    if len(projectName) < g.projectNameLength:
        gui.msgbox(arg, "Project name must be at least " + str(g.projectNameLength) + " characters long.",
            MessageBoxButtons = "ok",
            MessageBoxIcon = "error",
        )
        return

    # Must not exist
    if projectName.lower() in [project.lower() for project in arg.projects]:
        gui.msgbox(arg, "Project name already exists.",
            MessageBoxButtons = "ok",
            MessageBoxIcon = "error",
        )
        return
    
    # Create Directory
    os.mkdir('database/' + projectName)

    gui.msgbox(arg, "Successfully created project.",
        MessageBoxButtons = "ok",
        MessageBoxIcon = "info",
    )

    gui.showPage(arg, 'pg_main')

