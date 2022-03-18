import sys
sys.path.append("..")
sys.path.append("../plugins")
sys.path.append("../functions")

## IMPORT PLUGINS AND MODULES
import g, gui, styles
import os, importlib
import tkinter as tk
from tkinter import ttk
from types import SimpleNamespace as sn
import _thread as thread
import time



def page(arg):
    ## Name of this Page
#    print(arg.curpage)
    
    ## SAVE PROPERTIES
    arg.hprops = sn(**{}); arg.hobjs = sn(**{}); arg.hvars = sn(**{})
    arg.hprops.__dict__[arg.curpage] = sn(**{});
    arg.hobjs.__dict__[arg.curpage] = sn(**{});
    arg.hvars.__dict__[arg.curpage] = sn(**{});
    

    ####################### GUI ELEMENTS #########################
    h = sn(**{})

    ## Optional Variables for Guided Positioning
    margin = 30
    spacing = 10
    small = 150
    medium = 225
    large = 300
    height = 40

    h.bg =  sn(**{  ## gui.image(arg,"imagename", "image.jpg", (w,h)))
        "obj": gui.image(arg,"pg_1-bg","bg.jpg",(g.frameWidth,g.frameHeight)),
        "pos": sn(**{
            "x": 0,
            "y": 0,
            "w": g.frameWidth,
            "h": g.frameHeight,
        })
    })


    ### LABEL 
    h.label1 = sn(**{ ## gui.label(arg,"style","align","text")
       "obj": gui.label(arg,"labelSmall","center","Hello There!"),                
       "pos": sn(**{
           "x": margin,
           "y": 300,
           "w": medium,
           "h": height,
       })
    })
   
   
    ### ENTRY
    h.myEntry = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.entry(arg,"entryMedium","center","Edit me!", name="myEntry", password=True, keyboard=True),
        "pos": sn(**{
            "x": 10,
            "y": 10,
            "w": 150,
            "h": 30,
        })
    })
    
    

    
    h.btnTest1 = sn(**{ ## gui.button(arg,"style","unused","text",lambda: fcn(arg)),
            ## Function Wont Work on Quick View
        "obj": gui.button(arg,"btnBig","center","Push Me!",lambda: arg.fcn_main.testFcn(arg)),
        "pos": sn(**{
            "x": margin,
            "y": 200,
            "w": medium,
            "h": height,
        })
    })
    
    h.btnTest2 = sn(**{ ## gui.button(arg,"style","unused","text",lambda: fcn(arg)),
        "obj": gui.button(arg,"btnBig","center","NEXT PAGE",lambda: gui.showPage(arg,"pg_testing")),
        "pos": sn(**{
            "x": margin,
            "y": h.btnTest1.pos.y + h.btnTest1.pos.h + spacing,
            "w": medium,
            "h": height,
        })
    })
#
    data = ["Entry1","fsfs"] ## ["Entry 1" , "Entry 2"]
    h.listbox1 = sn(**{
        "obj" : gui.listbox(arg,data,"listbox1"),
        "pos": sn(**{
            "x": margin + medium + spacing,
            "y": margin,
            "w": large,
            "h": 300,
        })                   
    })
    
    data = ["Entry 1" , "Entry 2"]
    h.dropdown1 = sn(**{
        "obj" : gui.dropdown(arg,"ddstyle","center",data,"dropdown1"),
        "pos": sn(**{
            "x": 600,
            "y": 20,
            "w": 180,
            "h": 35,
        })          
    })


    rsp = db(arg,"getPathologist")
    data = []
    for dt in rsp:
        data.append([dt["name"],dt["status"]])

    h.table1 = sn(**{
        "obj" : gui.ttk.Treeview(arg.master),
        "pos" : sn(**{
            "x" : 70,
            "y" : 180,
            "w" : 650,
            "h" : 200,
        }),
        "table" : sn(**{
            "columns" : [
                sn(**{"title" : "Name", "width" : 500}),
                sn(**{"title" : "Status", "width" : 150}),
                # sn(**{"title" : "Brand", "width" : 150}),
                # sn(**{"title" : "Equipment", "width" : 200}),
                # sn(**{"title" : "Tag", "width" : 100}),
            
            ],
            "data" : [
                []
            ],
        }),
    })

     # For Scrollbar
    h.table1Scroll = sn(**{
        "obj" : gui.ttk.Scrollbar(arg.master, orient="vertical",
            command=h.table1.obj.yview),
        "pos" : sn(**{
            "x" : 725,
            "y" : 180,
            "w" : 25,
            "h" : 200,
        })
    })
    
    h.table1.obj.configure(yscrollcommand=h.table1Scroll.obj.set)

    # self.canvas.bind('<Button-1>', self.clicked)  
    # self.canvas.bind('<Double-1>', self.double_click)  
    # self.canvas.bind('<ButtonRelease-1>', self.button_released)  
    # self.canvas.bind('<B1-Motion>', self.moved)  

    # Bind double click even on table1 data/row.
    h.table1.obj.bind('<Double-1>', lambda event,t=h.table1.obj: arg.fcn_gui3.table1Double_ClickEven(arg))  

    # "data" : [
    #             ["Felipe Templo Jr, MD","ON-DUTY"],
    #             ["Jeffrey S. So, MD, DPSP","OFF-DUTY"],
    #             ["Francis G. Moria, MD, MSc FPSP","OFF-DUTY"],
    #             ["Jose Maria C. Avila, MD","ON-DUTY"],
    #             ["Michelle Anne M. Latoy, MD","ON-DUTY"],
    #             ["Aida Isabel Mendoza, MD","OFF-DUTY"],
    #             ["Charles Harris, MD","OFF-DUTY"],
    #             ["Felipe Templo Jr, MD","ON-DUTY"],
    #             ["Jeffrey S. So, MD, DPSP","OFF-DUTY"],
    #             ["Francis G. Moria, MD, MSc FPSP","OFF-DUTY"],
    #             ["Jose Maria C. Avila, MD","ON-DUTY"],
    #             ["Michelle Anne M. Latoy, MD","ON-DUTY"],
    #             ["Aida Isabel Mendoza, MD","OFF-DUTY"],
    #             ["Charles Harris, MD","OFF-DUTY"],
    #         ],


#    h.scrollAlone = sn(**{
#        "obj": gui.scroll(arg,"scrollstyle","center"),
#        "pos": sn(**{
#            "x": h.listbox1.pos.x + h.listbox1.pos.w + spacing,
#            "y": margin,
#            "w": 50,
#            "h": 300,
#        })
#    })



# data = ["Entry1  -  ON-DUTY","fsfs  -  OFF-DUTY"] ## ["Entry 1" , "Entry 2"]

    # h.listbox1 = sn(**{
    #     "obj" : gui.listbox(arg,data,"listbox1"),
    #     "pos": sn(**{
    #         "x": 70,
    #         "y": 180,
    #         "w": 645,
    #         "h": 200,
    #     })                   
    # })

    # For Scrollbar
    # h.listScroll = sn(**{
    #     "obj" : ttk.Scrollbar(master, orient="vertical",
    #         # command=handle["listbox1"]["element"].yview),
    #         command=h.listbox1.obj.yview),
    #     "pos" : sn(**{
    #         "x": 200,
    #         "y": 50,
    #         "w": 40,
    #         "h": 720,
    #     })
    # })  
    
    # ##### SUB PROPERTIES OF THE ABOVE HANDLES
    # h.listbox1.obj.configure(yscrollcommand=h.listScroll.obj.set);

    h.checkbox = sn(**{ ## gui.checkbox(arg,"yourText", lambda: test(arg)),
        "obj": gui.checkbox(arg,"yourText", lambda: test(arg)),
        "pos": sn(**{
            "x": 10,
            "y": 10,
            "w": 150,
            "h": 30,
        })
    })


    # array 0 is the default value.
    optionList1 = ('a','a' ,'b', 'c')
    h.combobox = sn(**{ ## ttk.OptionMenu(arg.master,v1,*optionList1, command=lambda selected:test123123(selected))
        "obj": gui.combobox(arg,optionList1,lambda selected_val:test(selected_val)),
        "pos": sn(**{
            "x": 50,
            "y": 10,
            "w": 150,
            "h": 30,
        })
    })

    h.progressbar = sn(**{ ## tttk.Progressbar(arg.master, orient = orient, length = length, mode = mode)
        "obj": gui.progressbar(arg),
        "pos": sn(**{
            "x": 100,
            "y": 10,
            "w": 150,
            "h": 30,
        })
    })

    gui.hpropsobjs(arg,h)
    return h


def updateTimeAndDate(arg):
    
    # Updating Time Display in Label Widget.
    # https://www.w3schools.com/python/python_datetime.asp
    h = arg.handles.pg_history
    while arg.thread_trig.historytime:
        x = datetime.datetime.now()
        curtime = x.strftime("%I:%M:%S %p")
        curdate = x.strftime("%m / %d / %y")
        print(curdate,curtime)
        gui.set_val(arg,h.lblTime.obj,"Time: " + curtime)
        gui.set_val(arg,h.lblDate.obj,"Date: " + curdate)

        arg.master.update()
        time.sleep(1)


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
    print(arg.__dict__)
    fcn = arg.__dict__[fcnFilename].preshow(arg)
    gui.dbgview(arg, fcn, preshow=True )
    

    