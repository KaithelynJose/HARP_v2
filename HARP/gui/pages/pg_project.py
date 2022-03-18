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
        "obj": gui.label(arg,"labelTitle","left","Project:", name="labelTitle"),
        "pos": sn(**{
            "x": h.logo.pos.x + h.logo.pos.w + 15,
            "y": h.logo.pos.y + 5,
            "w": 400,
            "h": 30,
        })
    })

    h.records = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.listbox(arg,data=[], name="records"),
        "pos": sn(**{
            "x": 50,
            "y": 100,
            "w": 250,
            "h": 325,
        })
    })
    
    h.btnRecord = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.button(arg,"button","center","Record and Save", lambda: arg.fcn_project.newRecord(arg)),
        "pos": sn(**{
            "x": 350,
            "y": 100,
            "w": 200,
            "h": 50,
        })
    })

    h.btnView = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.button(arg,"button","center","View Tablature", lambda: arg.fcn_project.viewRecord(arg)),
        "pos": sn(**{
            "x": 350,
            "y": 165,
            "w": 200,
            "h": 50,
        })
    })

    h.btnMerge = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.button(arg,"button","center","Merge Records", lambda: arg.fcn_project.mergeRecords(arg)),
        "pos": sn(**{
            "x": 350,
            "y": 230,
            "w": 200,
            "h": 50,
        })
    })

    h.btnExport = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.button(arg,"button","center","Generate as PDF", lambda: arg.fcn_project.btnExport(arg)),
        "pos": sn(**{
            "x": 350,
            "y": 295,
            "w": 200,
            "h": 50,
        })
    })

    h.btnDelete = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.button(arg,"button","center","Delete Record", lambda: arg.fcn_project.deleteRecord(arg)),
        "pos": sn(**{
            "x": 350,
            "y": 360,
            "w": 200,
            "h": 50,
        })
    })

    h.btnBack = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.button(arg,"button","center","BACK", lambda: arg.fcn_project.back(arg)),
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
    
