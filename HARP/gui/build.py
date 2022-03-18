import sys
sys.path.append("..")

import subprocess
import os
import shutil
import pyfiglet
from pyfiglet import Figlet

import g
import argparse
import glob
from types import SimpleNamespace as sn


# BUILDER FUNCTIONS
from system.builder.change_default_page import index as change_default_page
from system.builder.create_page import index as create_page
from system.builder.delete_page import index as delete_page
from system.builder.clean import *

# path = "system/gui/buttons/"
# pathdot = "system.gui.buttons."
# mymodules = glob.glob("system/gui/buttons/*.py")
# for ctr in range(0,len(mymodules)):
#     # print(mymodules[ctr][len(path):-3])
#     name = mymodules[ctr][len(path):-3]
#     importlib.import_module(pathdot + name)

# Importing BUILDER FUNCTIONS
# builder = sn(**{})
# mymodules = glob.glob("system/gui/buttons/*.py")
# for ctr in range(0,len(mymodules)):
#     modulename = mymodules[ctr][len(path):-3]
#     builder.__dict__[modulename] = importlib.import_module("system.gui.buttons." + modulename) 
#     print(builder)


G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'   # white
# def banner():
#     print("""%s %s%s
                
#     """ % (R, W, Y))


# from types import SimpleNamespace as sn

def main():


    if len(sys.argv) < 2:
        # print("""%sGreen%sWhite%sRed""" % (G, W, R))
        
        print("""%s""" % (Y))
        custom_fig = Figlet(font=g.builder_font)
        print(custom_fig.renderText(g.builder_title))

        print("""%s                             Visual Py Builder 1.0


            """ % (G))

        # ascii_banner = pyfiglet.figlet_format(g.builder_title_sub)
        # print(ascii_banner)
        print("""%sCOMMANDS:%s""" % (Y,G))
        helper()
        return

    cmd = sys.argv[1]
    # RUN PAGE
    if cmd == "run" or cmd == "r":

        if len(sys.argv)==2:
            try: 
                subprocess.call(["python3","main.py"])
            except: 
                subprocess.call(["python", "main.py"])

            return

        pagename = sys.argv[2]
        
        ## Validations Start
        if len(pagename) == 0:
            print("Error: Invalid filename")
        
        if not os.path.isfile("pages/pg_" + pagename + ".py"):
            print("Error: Page does not exist!")
            return
        
        ## Validations End
        
        os.chdir("pages");
        pagename = "pg_" + pagename + ".py"
        try: 
            
            subprocess.call(["python3", pagename])
        except:

            subprocess.call(["python", pagename])
        # os.system("python3 pg_" + pagename + ".py")

    elif cmd == "create_page" or cmd == "c" or cmd == "create":
        ## CREATE NEW PAGE
       
        
        ## Validations Start
        MyValidations()
        ## Validations End

        pagename = sys.argv[2]
        create_page(pagename)
        # create_page.index(pagename)
        # builder.create_page.index(pagename)
        
        
        return
    elif cmd == "delete_page" or cmd == "d" or cmd == "delete":
        ## CREATE NEW PAGE
       
        
        ## Validations Start
        pagename = sys.argv[2]
        if len(pagename) == 0:
            print("Error: Invalid filename")
            return
        ## Validations End

        pagename = sys.argv[2]
        delete_page(pagename)
        
        
        return
    
    elif cmd == "change_default_page" or cmd == "ch" or cmd == "change":
        if len(sys.argv) <= 2:
            helper()
            return
            
        pagename = sys.argv[2]
        change_default_page(pagename)
        return
    elif cmd == "clean":
        # Clean here
        builder_clean()

    else:
        print("command are not found!.")


def MyValidations():
    # print("get in")
    # print("argv2:",sys.argv[2])
    pagename = sys.argv[2]
    if len(pagename) == 0:
        print("Error: Invalid filename")
        return

    if os.path.isfile("pages/pg_" + pagename + ".py"):
        print("Error: Page file existing!")
        return

    if os.path.isfile("functions/fcn_" + pagename + ".py"):
        print("Error: Function file existing!")
        return

def helper():
    f=open("system/helper.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        print(contents)
    f.close() 

if __name__ == "__main__":
    main()