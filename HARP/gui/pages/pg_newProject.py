import sys
sys.path.append("..")
sys.path.append("../plugins")
sys.path.append("../functions")
sys.path.append("../system")

## IMPORT PLUGINS AND MODULES
import g, gui, styles
import os, importlib

if sys.version_info.major == 3:
    print('Python3')
    from types import SimpleNamespace as sn
    from tkinter import IntVar

else:
    print('Python2')
    # import types_py2
    # sn = types.SimpleNamespace
    from types_py2 import SimpleNamespace as sn
    from Tkinter import IntVar



def page(arg):

    ## SAVE PROPERTIES
    arg.hprops = sn(**{}); arg.hobjs = sn(**{}); arg.hvars = sn(**{})
    arg.hprops.__dict__[arg.curpage] = sn(**{});
    arg.hobjs.__dict__[arg.curpage] = sn(**{});
    arg.hvars.__dict__[arg.curpage] = sn(**{});
    
    h = sn(**{})
    ####################### GUI ELEMENTS START #########################

    h.entryName = sn(**{ ## 
        "obj": gui.entry(arg,"entry","center","", name="entryName", keyboard=True),
        "pos": sn(**{
            "x": 150,
            "y": 130,
            "w": 500,
            "h": 50,
        })
    })

    h.btnAdd = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.button(arg,"button","center","ADD", lambda: arg.fcn_newProject.addProject(arg)),
        "pos": sn(**{
            "x": 300,
            "y": 250,
            "w": 200,
            "h": 50,
        })
    })

    h.btnCancel = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.button(arg,"button","center","CANCEL", lambda: arg.fcn_newProject.cancelAddProject(arg)),
        "pos": sn(**{
            "x": 20,
            "y": 480 - 50 - 20,
            "w": 200,
            "h": 50,
        })
    })


    ####################### GUI ELEMENTS END #########################
    gui.hpropsobjs(arg,h)
    return h


### RUN THIS FILE FOR QUICK VIEWING ###    
if __name__ == "__main__":
    arg = sn(**{})
    arg.quickpreview = True
    
    arg.curpage = os.path.basename(__file__)[0:-3]
    fcnFilename = "fcn_" + arg.curpage[3:]
    
    gui.setupMaster(arg)
    styles.setup()
    
    arg.handles = sn(**{ arg.curpage : page(arg)})
    arg.__dict__[fcnFilename] = importlib.import_module("functions." + fcnFilename)
#    fcn = arg.__dict__[fcnFilename].preshow(arg)
#    gui.dbgview(arg, fcn, preshow=True )
    gui.showPage(arg,arg.curpage)
    arg.master.mainloop()
    
