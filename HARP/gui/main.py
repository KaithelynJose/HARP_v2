######## Imports the Required Libaries ########
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


sys.path.append("plugins")
sys.path.append("system")

if sys.version_info.major == 3:
    print('Python3')
    from types import SimpleNamespace as sn
else:
    print('Python2')
    # import types_py2
    # sn = types.SimpleNamespace
    from types_py2 import SimpleNamespace as sn

import g  # Global Variables
import gui
import styles


arg = sn(**{}) ## Global Variable for All Dynamic Data

g.__dict__["arg"] = arg

## Holder for Images
arg.imgs = sn(**{})

## Setup Tkinter
gui.setupMaster(arg)
styles.setup()

# set application to fullscreen
if g.activate_fullscreen:
    arg.master.attributes('-fullscreen', True)


######## Global Variable Listeners for Tkinter Check Button Elements ########
arg.checkbox = sn(**{});

###### Trigger to Stop thread
arg.thread_trig = sn(**{});


gui.setupPages(arg)

#gui.setupKeyboard(arg)

# Page: keyboard

#import pg_keyboard
#arg.handles["pg_keyboard"] = pg_keyboard;



def showKeyboard(event, kbpage, kbelement, kbtype=None,clrentry=False, bypassPreshow=True,bypassPostshow=True):
    
    g.kbpage = kbpage
    g.kbelement = kbelement
    gui.showPage(arg, "pg_keyboard", kbtype, )
    g.kbcurstring = arg.handles.__dict__[kbpage].__dict__[kbelement].obj.get()
    if "password" in arg.handles.__dict__[kbpage].__dict__[kbelement].bind.__dict__:
        g.kbpassword = True
        msg= g.kbcurstring;
        arg.handles.pg_keyboard.label.obj.config(
            text=gui.passwordMask(arg,msg))
    else:
        g.kbpassword = False
        arg.handles.pg_keyboard.label.obj.config(
            text=g.kbcurstring)


######## Bind Keyboard #########
def bindKeyboard(master, handles):
    for page in handles.__dict__:
        for element in handles.__dict__[page].__dict__:
            if "bind" in handles.__dict__[page].__dict__[element].__dict__:

                if "keyboard" in handles.__dict__[page].__dict__[element].bind.__dict__:
                    
                    ## Note: Lambda does not use the variable. Need to reassign actual texts: "number","date", etc
                    if "number" in handles.__dict__[page].__dict__[element].bind.__dict__:
                        handles.__dict__[page].__dict__[element].obj.bind("<Button-1>",
                        lambda event, kbpage=page,
                        kbelement=element:showKeyboard(event, kbpage, kbelement, "number"))
                    elif "date" in handles.__dict__[page].__dict__[element].bind.__dict__:
                        handles.__dict__[page].__dict__[element].obj.bind("<Button-1>",
                        lambda event, kbpage=page,
                        kbelement=element:showKeyboard(event, kbpage, kbelement, "date"))
                    elif "time" in handles.__dict__[page].__dict__[element].bind.__dict__:
                        handles.__dict__[page].__dict__[element].obj.bind("<Button-1>",
                        lambda event, kbpage=page,
                        kbelement=element:showKeyboard(event, kbpage, kbelement, "time"))
                    else:
                        handles.__dict__[page].__dict__[element].obj.bind("<Button-1>",
                            lambda event, kbpage=page,
                            kbelement=element:showKeyboard(event, kbpage, kbelement, None))
                    
if g.useKeyboard:
    bindKeyboard(arg.master, arg.handles)

######## Show Only the Elements for this Page ########
gui.showPage(arg, g.defaultPage)

# Initiate Tkinter and Loop Forever
arg.master.mainloop()
