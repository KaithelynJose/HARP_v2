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

    h.logo = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.image(arg,"logo","logo.png",(50,30)),
        "pos": sn(**{
            "x": 220,
            "y": 20,
            "w": 50,
            "h": 30,
        })
    })

    h.labelTitle = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.label(arg,"labelTitle","left","HARP Guitar Tab Generator", name="labelTitle"),
        "pos": sn(**{
            "x": h.logo.pos.x + h.logo.pos.w + 15,
            "y": h.logo.pos.y + 5,
            "w": 400,
            "h": 30,
        })
    })

    h.projects = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.listbox(arg,data=[], name="projects"),
        "pos": sn(**{
            "x": 50,
            "y": 100,
            "w": 250,
            "h": 325,
        })
    })
    
    h.btnNew = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.button(arg,"button","center","Create Project", lambda: arg.fcn_main.newProject(arg)),
        "pos": sn(**{
            "x": 400,
            "y": 100,
            "w": 200,
            "h": 50,
        })
    })

    h.btnView = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.button(arg,"button","center","Open Project", lambda: arg.fcn_main.viewProject(arg)),
        "pos": sn(**{
            "x": 400,
            "y": 175,
            "w": 200,
            "h": 50,
        })
    })

    h.btnDelete = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.button(arg,"button","center","Delete Project", lambda: arg.fcn_main.deleteProject(arg)),
        "pos": sn(**{
            "x": 400,
            "y": 250,
            "w": 200,
            "h": 50,
        })
    })

    h.btnShutdown = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.button(arg,"button","center","SHUTDOWN", lambda: arg.fcn_main.shutDown(arg)),
        "pos": sn(**{
            "x": 600,
            "y": 400,
            "w": 150,
            "h": 40,
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
    
