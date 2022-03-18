import sys
sys.path.append("..")
sys.path.append("../plugins")
sys.path.append("../functions")
sys.path.append("../system")

## IMPORT PLUGINS AND MODULES
import g, gui, styles
from types import SimpleNamespace as sn
import os, importlib
import _thread as thread
import time

def page(arg):

    ## SAVE PROPERTIES
    arg.hprops = sn(**{}); arg.hobjs = sn(**{}); arg.hvars = sn(**{})
    arg.hprops.__dict__[arg.curpage] = sn(**{});
    arg.hobjs.__dict__[arg.curpage] = sn(**{});
    arg.hvars.__dict__[arg.curpage] = sn(**{});
    
    h = sn(**{})
    ####################### GUI ELEMENTS START #########################
    h.bg =  sn(**{  ## gui.image(arg,"imagename", "image.jpg", (w,h)))
        "obj": gui.image(arg,"homepage-bg","homepage.png",(g.frameWidth,g.frameHeight)),
        "pos": sn(**{
            "x": 0,
            "y": 0,
            "w": g.frameWidth,
            "h": g.frameHeight,
        })
    })
    


    ####################### GUI ELEMENTS END #########################
    gui.hpropsobjs(arg,h)
    return h





## RUN THIS FILE FOR QUICK VIEWING ###    
if __name__ == "__main__":
    # For auto gui adjustment
    def realtimeadjustment(arg):
        while True:
            with open("adjust.txt","r") as fid:
                lines = fid.readlines()

            # print(lines)
            # posdata = content.split(",")

            pos = []
            for line in lines:
                line = line.split(",")[0]
                line = int(line.split(":")[1])
                pos.append(line)

            obj = arg.handles.pg_login.btnLoginGo
            obj.pos.x = pos[0]
            obj.pos.y = pos[1]
            obj.pos.w = pos[2]
            obj.pos.h = pos[3]
            obj.obj.place(
                x=pos[0],
                y=pos[1],
                width=pos[2],
                height=pos[3]
            )
            arg.master.update()
            time.sleep(0.4)


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

    # For auto gui adjustment
    thread.start_new_thread(realtimeadjustment, (arg,))

    gui.showPage(arg,arg.curpage)
    arg.master.mainloop()
    
