import sys
sys.path.append("..")


if sys.version_info.major == 3:
    print('Python3')
    from types import SimpleNamespace as sn
    import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox
    from tkinter import PhotoImage
    from tkinter import HORIZONTAL
else:
    print('Python2')
    # import types_py2
    # sn = types.SimpleNamespace
    from types_py2 import SimpleNamespace as sn
    import Tkinter as tk
    import ttk
    import tkMessageBox as messagebox
    from Tkinter import PhotoImage
    from Tkinter import HORIZONTAL
    
import styles
import importlib
import glob
import g
from PIL import Image, ImageTk
import numpy as np
import cv2 as cv
import os


# Page Navigation Functions
def hideAllPages(arg):
    handles = arg.handles;
    # Hide All Pages
    for page in handles.__dict__:
        for element in handles.__dict__[page].__dict__:
            
            handles.__dict__[page].__dict__[element].obj.place_forget()

'''#
|--------------------------------------------------------------------------
| showPage
|--------------------------------------------------------------------------
| context
|
'''
def showPage(arg,page,kbtype=None,clrentry=True,bypassPreshow=False,bypassPostshow=False):    
    


    handles = arg.handles;
    
    # if not bypassPostshow:
    #     # print("---- Page " + arg.curpage[3:] + " postshow has been called.")
    #     print("---- The fcn_" + arg.curpage[3:] + " postshow has been called.")
    #     if not(arg.__dict__["fcn_" + arg.curpage[3:]].postshow(arg):
    #         return;

    if not bypassPostshow:
        print("---- The fcn_" + arg.curpage[3:] + " postshow has been called.")
        
        if not(arg.__dict__["fcn_" + arg.curpage[3:]].postshow(arg)):
            return;


    # Perform preShow function
    if not bypassPreshow:
        # print("---- Page " + arg.curpage[3:] + " preshow has been called.")
        print("---- The fcn_" + page[3:] + " preshow has been called.")
        
        if not(arg.__dict__["fcn_" + page[3:]].preshow(arg)):
            return;
        # if not(arg.__dict__["fcn_" + arg.curpage[3:]].preshow(arg)):
        #     return;
        # arg.curpage = os.path.basename(__file__)[0:-3]
        # print("new:", arg.curpage)
        # fcnFilename = "fcn_" + arg.curpage[3:]
        # if not(arg.__dict__[fcnFilename].preshow(arg)):
        #     return
        # fcn = arg.__dict__[fcnFilename].preshow(arg)
    arg.curpage = page

    
#    g.curpage = page;
    
    # Hide All Except Page
    hideAllPages(arg)
    print("Showing Page: " , arg.curpage )

    for element in handles.__dict__[page].__dict__:

        if page == "pg_keyboard":
            showKBel = False;
            if kbtype is None:
                showKBel = True;
            elif kbtype == "number":
                if "number" in handles.__dict__[page].__dict__[element].__dict__:
                    showKBel = True;
            elif kbtype == "date":
                if ("date" in handles.__dict__[page].__dict__[element].__dict__) or ("number" in handles.__dict__[page].__dict__[element].__dict__):
                    showKBel = True;
            elif kbtype == "time":
                if ("time" in handles.__dict__[page].__dict__[element].__dict__) or ("number" in handles.__dict__[page].__dict__[element].__dict__):
                    showKBel = True;
                    
            if showKBel:
                handles.__dict__[page].__dict__[element].obj.place(
                    x=int((handles.__dict__[page].__dict__[element].pos
                           .x/15)*g.frameWidth)+g.kbwadj,
                    y=int((handles.__dict__[page].__dict__[element].pos
                           .y/6)*g.frameHeight)+g.kbhadj,
                    width=int((handles.__dict__[page].__dict__[element].pos
                               .w/15)*g.frameWidth)-(g.kbwadj*2),
                    height=int((handles.__dict__[page].__dict__[element].pos
                                .h/6)*g.frameHeight)-(g.kbhadj*2),
                )
                
                
        else:

            handles.__dict__[page].__dict__[element].obj.place(
                x=handles.__dict__[page].__dict__[element].pos.x,
                y=handles.__dict__[page].__dict__[element].pos.y,
                width=handles.__dict__[page].__dict__[element].pos.w,
                height=handles.__dict__[page].__dict__[element].pos.h,
            )
            
            ## Clear entries on page load
            if clrentry:
                if element.startswith("entry"):
                    if handles.__dict__[page].__dict__[element].obj.winfo_class()=="TEntry":
                        # handles.__dict__[page].__dict__[element].obj.delete(0,tk.END);
                        pass
                    elif handles.__dict__[page].__dict__[element].obj.winfo_class()=="TLabel":
                        handles.__dict__[page].__dict__[element].obj.config(text="");



            if "table" in handles.__dict__[page].__dict__[element].__dict__:
                tmplist = []
                for tmp in handles.__dict__[page].__dict__[element].table.columns:
                    tmplist.append(tmp.title)
                
                
                handles.__dict__[page].__dict__[element].obj.config(columns = tuple(
                    tmplist.copy()))
                
                
                handles.__dict__[page].__dict__[element].obj.column(
                    "#0",
                    width=0, stretch=tk.NO,
                )
                
                for tablectr,col in enumerate(handles.__dict__[page].__dict__[element].table.columns):
                    
                    
                    handles.__dict__[page].__dict__[element].obj.heading(
                        col.title, text=col.title)
                    
                    
                    handles.__dict__[page].__dict__[element].obj.column(
                        col.title,
                        width=col.width,
                        anchor=tk.CENTER
                    )


                handles.__dict__[page].__dict__[element].obj.delete(
                    *handles.__dict__[page].__dict__[element].obj.get_children())

                datactr = 0

                for data in handles.__dict__[page].__dict__[element].table.data:
                    datactr = datactr + 1

                    handles.__dict__[page].__dict__[element].obj.insert(
                        "", datactr, None,
                        text=str(datactr),
                        values=tuple(data),
                    )
    arg.master.update()


def passwordMask(arg,msg):
    
    toShow = ""
    for ctr in range(0, len(msg)):
        toShow = toShow + "*"

    return toShow


def keyboardInput(arg,keyin):
    master = arg.master;
    handles = arg.handles
        

    if keyin == "backspace":
        if len(g.kbcurstring) > 0:
            g.kbcurstring = g.kbcurstring[0:-1]
    elif keyin == "space":

        g.kbcurstring = g.kbcurstring + " "
    elif keyin == "ok":
        handles.__dict__[g.kbpage].__dict__[g.kbelement].obj.delete(0, tk.END)
        handles.__dict__[g.kbpage].__dict__[g.kbelement].obj.insert(0, g.kbcurstring)
        showPage(arg, g.kbpage,clrentry=False,bypassPreshow=True,bypassPostshow=True)


    elif keyin == "shift":

        g.kbshift = not(g.kbshift)

        if g.kbshift:
            for element in handles.pg_keyboard.__dict__:
                if "shift" in handles.pg_keyboard.__dict__[element].__dict__:

                    shiftVal = handles.pg_keyboard.__dict__[element].shift

                    handles.pg_keyboard.__dict__[element].obj.config(
                        text=shiftVal)
                    master.update()
        else:
            for element in handles.pg_keyboard.__dict__:
                if "shift" in handles.pg_keyboard.__dict__[element].__dict__:

                    handles.pg_keyboard.__dict__[element].obj.config(
                        text=element)

    else:
        if g.kbshift:
            keyin = handles.pg_keyboard.__dict__[keyin].shift

        g.kbcurstring = g.kbcurstring + keyin

    if g.kbpassword:
        handles.pg_keyboard.label.obj.config(
            text=passwordMask(arg,g.kbcurstring))
    else:
        handles.pg_keyboard.label.obj.config(
            text=g.kbcurstring)

    master.update()





######## GUI ELEMENTS ###########




def label(arg,style,align,text,name="",enabled=True):
    if align == "left":
        anchor = tk.W
        # anchor = 
    elif align == "right":
        anchor = tk.E
    elif align == "center":
        anchor = tk.CENTER
    else:
        # must be n, ne, e, se, s, sw, w, nw, or center
        anchor = align

    state=tk.NORMAL
    if enabled:
        state=tk.NORMAL
    else:
        state=tk.DISABLED

    obj = ttk.Label(arg.master,
    style= style + ".TLabel",
    anchor=anchor,
    text=text,
    state=state)


    
    return obj
    
def label_change_text(arg, obj, new_value=""):
    obj = obj.config(text=str(new_value));
    return obj

def label_get_text(arg, obj):
    text = obj.cget("text")
    return text

def set_label_val(arg, obj, new_value=""):
    obj = obj.config(text=str(new_value));
    return obj
    
def get_label_val(arg, obj):
    text = obj.cget("text")
    return text


def image(arg,imgname,imgPath,imgsz): #,imgtk):
    
    if "quickpreview" in arg.__dict__:
        imgPath = "../img/" + imgPath
    else:
        imgPath = "img/" + imgPath
    
    img = image_tk(imgPath)
    img = img.resize(imgsz,Image.ANTIALIAS)
    frame = ImageTk.PhotoImage(img)
        
    obj = tk.Label(arg.master,
      image=frame,
      relief="flat",
      highlightthickness=0,
      borderwidth=0)
    obj.image = frame

    return obj

def image_tk(imgPath): ## imgType= "cv" | "pil"
    if isinstance(imgPath,str):
        return Image.open(imgPath)
    elif isinstance(imgPath,np.ndarray):
        img = cv.cvtColor(imgPath,cv.COLOR_BGR2RGB);
        return Image.fromarray(img)


def image_show(arg,h,imgname,imgPath):
    if "quickpreview" in arg.__dict__:
        imgPath = "../img/" + imgPath
    else:
        imgPath = "img/" + imgPath

    imgsz = (h.pos.w,h.pos.h)
    img = image_tk(imgPath)
    img = img.resize(imgsz,Image.ANTIALIAS)
#    arg.hvars.__dict__[arg.curpage].__dict__[imgname] = ImageTk.PhotoImage(img)
    frame = ImageTk.PhotoImage(img)
    
#    h.obj.configure(image=arg.hvars.__dict__[arg.curpage].__dict__[imgname])
#    h.obj.image = arg.hvars.__dict__[arg.curpage].__dict__[imgname]
    
    h.obj.configure(image=frame)
    h.obj.image = frame
    
    arg.master.update()

def change_image(arg,h,imgname,imgPath):
    if "quickpreview" in arg.__dict__:
        imgPath = "../img/" + imgPath
    else:
        imgPath = "img/" + imgPath
    
    imgsz = (h.pos.w,h.pos.h)
    img = image_tk(imgPath)
    img = img.resize(imgsz,Image.ANTIALIAS)
#    arg.hvars.__dict__[arg.curpage].__dict__[imgname] = ImageTk.PhotoImage(img)
    frame = ImageTk.PhotoImage(img)
    
#    h.obj.configure(image=arg.hvars.__dict__[arg.curpage].__dict__[imgname])
#    h.obj.image = arg.hvars.__dict__[arg.curpage].__dict__[imgname]
    
    h.obj.configure(image=frame)
    h.obj.image = frame
    
    arg.master.update()


"""
# TEXTBOX OR ENTRY

# USAGE:
from types import SimpleNamespace as sn
import gui

h = sn(**{})

### YOUR ENTRY
h.YOUR_ENTRY_NAME_HERE = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
    "obj": gui.entry(arg,"entryMedium","center","Edit me!", name="YOUR_ENTRY_NAME_HERE", password=True, keyboard=True),
    "pos": sn(**{
        "x": 10,
        "y": 10,
        "w": 150,
        "h": 30,
    })
})

gui.hpropsobjs(arg,h)
return h

"""
def entry(arg,style,align,text,name="",password=False, keyboard=False,enabled=True):
    
    stylevar = styles.setup()

    arg.hprops.__dict__[arg.curpage].__dict__[name] = sn(**{ "bind" : sn(**{})})
    
    if align == "left":
        anchor = tk.LEFT
    elif align == "right":
        anchor = tk.RIGHT
    elif align == "center":
        anchor = tk.CENTER
    
    if password:
        toShow = "*"
        arg.hprops.__dict__[arg.curpage].__dict__[name].bind.password = True
    else:
        toShow = ""

    state=tk.NORMAL
    if enabled:
        state=tk.NORMAL
    else:
        state=tk.DISABLED
        
    obj = ttk.Entry(arg.master,
        font = (stylevar.lookup(style + ".TEntry","font")),
        # style = style + ".TEntry",
        justify = anchor,
        show = toShow,
        state = state)
    
    obj.delete(0,tk.END)
    obj.insert(0,text)
    

    if keyboard:
        arg.hprops.__dict__[arg.curpage].__dict__[name].bind.keyboard = True

    
    return obj
'''
@USAGE
gui.entry_change_text(arg, arg.handles.PG_NAME.ENTRY_NAME.obj,"NEW TEXT VALUE")
'''
def entry_change_text(arg, obj, new_value=""):
    obj.delete(0,arg.tk.END)
    obj.insert(0,str(new_value))
    return obj

'''
@USAGE
gui.entry_get_text(arg, arg.handles.PG_NAME.ENTRY_NAME.obj)
'''
def entry_get_text(arg, obj):
    text = obj.get()
    return text


def get_entry_val(arg,obj):
    val = obj.get()
    return val

def set_entry_val(arg,obj, new_value=""):
    obj.delete(0,tk.END)
    obj.insert(0,str(new_value))
    return obj

def set_val(arg, obj, new_value=""):
    # Lets check if the object is LABEL type
    if type(obj) == ttk.Label:
        # the object is LABEL
        new_obj = obj.config(text=str(new_value));
        return new_obj

    # Lets check if the object is ENTRY type
    if type(obj) == ttk.Entry:
        # the object is Entry
        obj.delete(0,tk.END)
        obj.insert(0,str(new_value))
        return obj

    if type(obj) == ttk.Button:
        # the object is Entry
        obj.config(text=str(new_value))
        return obj



def get_val(arg,obj,value=""):
    # Lets check if the object is LABEL type
    if type(obj) == ttk.Label:
        # the object is LABEL
        text = obj.cget("text")
        return text

    # Lets check if the object is ENTRY type
    if type(obj) == ttk.Entry:
        # the object is ENTRY
        val = obj.get()
        return val

    # Lets check if the object is ENTRY type
    if type(obj) == ttk.Button:
        # the object is ENTRY
        val = obj.cget("text")
        return val
        

def button(arg,style,align,text,command):
    
    ## Note: No Align Property. Not used    
    obj = ttk.Button(arg.master,
    style= style + ".TButton",
    text=text,
    command= command)
    
    return obj


def listbox(arg,data,name,orient="vertical"):
    obj = tk.Listbox(arg.master)
    
    obj.delete(0,tk.END)
    ## If data is List
    if isinstance(data,list):
        for d in data:
            obj.insert(tk.END, d)
    else:
        ## If data is scalar
        obj.insert(tk.END, data)
    
    if orient=="vertical":
        arg.hobjs.__dict__[arg.curpage].__dict__[name] = sn(**{
            "obj" : ttk.Scrollbar(arg.master, orient="vertical",
                command= obj.yview),
            "orient" : "vertical"
        })
        obj.config(yscrollcommand=arg.hobjs.__dict__[arg.curpage].__dict__[name].obj.set)
    else:
        arg.hobjs.__dict__[arg.curpage].__dict__[name] = sn(**{
            "obj" : ttk.Scrollbar(arg.master, orient="horizontal",
                command= obj.xview),
            "orient" : "horizontal"
        })
        obj.config(xscrollcommand=arg.hobjs.__dict__[arg.curpage].__dict__[name].obj.set)
    
    
    
    return obj

def listbox_data(arg,h,data):
    ## Replace data in listbox
    
    h.obj.delete(0,tk.END)
    ## If data is List
    if isinstance(data,list):
        for d in data:
            h.obj.insert(tk.END, d)
    else:
        ## If data is scalar
        h.obj.insert(tk.END, data)



def listbox_add(arg,h,data):
    ## Adds data to last row
    
    ## If data is List
    if isinstance(data,list):
        for d in data:
            h.obj.insert(tk.END, d)
    else:
        ## If data is scalar
        h.obj.insert(tk.END, data)
    

def dropdown(arg,style,align,data,name):
    
    arg.hvars.__dict__[arg.curpage].__dict__[name] = tk.StringVar()
    
    if isinstance(data,list):
        arg.hvars.__dict__[arg.curpage].__dict__[name].set(data[0])
        obj = ttk.OptionMenu(arg.master, \
          arg.hvars.__dict__[arg.curpage].__dict__[name],
          arg.hvars.__dict__[arg.curpage].__dict__[name].get(),
          *data)
    else:
        arg.hvars.__dict__[arg.curpage].__dict__[name].set(data)
        obj = ttk.OptionMenu(arg.master, \
          arg.hvars.__dict__[arg.curpage].__dict__[name],
          arg.hvars.__dict__[arg.curpage].__dict__[name].get(),
          *[data])
    
    
    
    
    return obj

def table(arg,style="",align="",header=[],data=[],name=""):
    ## Style Pending
    
    h = ttk.Treeview(arg.master)
    
    arg.hvars.__dict__[arg.curpage].__dict__[name] = sn(**{
        "header" : header,
        "data" : data,
    })
    
    return h

def table_initialize_data(arg,obj,data=[]):

    # remove all data on table first
    x = obj.get_children()
    # tree.delete(selected_item)
    for item in x: ## Changing all children from root item
            table1.delete(item)
    

    # rsp = db(arg,"getPathologist")
    # data = []
    data
    index = 1
    for dt in rsp:
        # data.append([dt["name"],dt["status"]])
        # for item in x: ## Changing all children from root item
        #     table1.item(item, text="blub", values=(dt["name"], dt["status"]))
        table1.insert("" , index,    text="Line " + str(index), values=(dt["name"], dt["status"]))
        index += 1

def table_get_selected_data(arg,obj):
    selected_item = obj.selection()[0]

    val = tuple(obj.item(selected_item)['values'])

    return val

def table_delete_selected_data(arg,obj):
    selected_item = obj.selection()[0]
    r = obj.delete(selected_item)

    return r
    
def hide(arg,h):
    h.obj.place_forget()
    arg.master.update()

def show(arg,h):
    h.obj.place(
            x=h.pos.x,
            y=h.pos.y,
            width=h.pos.w,
            height=h.pos.h,    
    )
    arg.master.update()

"""
MESSAGEBOX/ALERT BOX

@USAGE
gui.msgbox(arg,"Hello World")
gui.msgbox(arg,"Hello World",gui.msgtype.OK,gui.msgicon.INFO)

"""
def msgbox(arg,
    message="",
    MessageBoxButtons = "ok",
    MessageBoxIcon = "info",
    title=g.defaultMessageBoxTitle,
    ):
    obj = messagebox._show(
        message=message,
        _type=MessageBoxButtons,
        _icon=MessageBoxIcon,
        title=title)
    return obj


msgtype = sn(**{})

# types
msgtype.ABORTRETRYIGNORE = "abortretryignore" # RETURN retry, ignore, abort
msgtype.OK = "ok" # RETURN YES OR NO
msgtype.OKCANCEL = "okcancel" # RETURN TRUE OR FALSE
msgtype.RETRYCANCEL = "retrycancel" # RETURN TRUE OR FALSE
msgtype.YESNO = "yesno" # RETURN TRUE OR FALSE
msgtype.YESNOCANCEL = "yesnocancel" # RETURN Cancel=None Yes=True No=False

msgicon = sn(**{})
# icons
msgicon.ERROR = "error"
msgicon.INFO = "info"
msgicon.QUESTION = "question"
msgicon.WARNING = "warning"

'''#
|--------------------------------------------------------------------------
| Checkbox or Checkbutton
|--------------------------------------------------------------------------
| context
|
'''
def checkbox(arg,
    text,
    command):

    obj = ttk.Checkbutton(arg.master,text=text, command=command)

    return obj
# To set the state in code:
# chk.state(['selected'])  # check the checkbox
# chk.state(['!selected']) # clear the checkbox
# chk.state(['disabled'])  # disable the checkbox
# chk.state(['!disabled','selected']) # enable the checkbox and put a check in it!

# And here is a convenient way to check for a specific state:
# chk.instate(['selected'])  # returns True if the box is checked
def checkbox_val(arg,change_val=""):
    var = tk.IntVar()
    var = arg.get()

    return var

'''#
|--------------------------------------------------------------------------
| ComboBox or Dropdown List
|--------------------------------------------------------------------------
| context
|
'''
def combobox(arg,
    optionList1,
    command):
    # https://stackoverflow.com/questions/19138534/tkinter-optionmenu-first-option-vanishes
    # optionList1 = ('a', 'b', 'c')
    optionList1 = optionList1
    # Set up the StringVars for each OptionMenu
    v1 = tk.StringVar()
    obj = ttk.OptionMenu(arg.master,v1,*optionList1,command=command)

    return obj

'''#
|--------------------------------------------------------------------------
| ProgressBar
|--------------------------------------------------------------------------
| context
|
'''

def progressbar(arg,
    orient = HORIZONTAL,
    length = 100,
    mode = 'determinate'):

    # Progress bar widget 
    obj = ttk.Progressbar(arg.master, orient = orient, 
                  length = length, mode = mode)
    return obj

'''#
|--------------------------------------------------------------------------
| RadioButton
|--------------------------------------------------------------------------
| context
|
'''

# choices = [
#     ("Python",1),
#     ("Perl",2),
#     ("Java",3),
#     ("C++",4),
#     ("C",5)
# ]

# def radiobutton(arg,text=text,padx=20,variable,value,command):
def radiobutton(arg,text,variable,value,command):
    # v = tk.IntVar()
    
    # Progress bar widget 
    obj = ttk.Radiobutton(arg.master,
        text=text,
        # padx=20,
        variable=variable, 
        command=command,
        value=value)

    return obj



def hpropsobjs(arg,h):
    
    # Objects
    for hname in arg.hobjs.__dict__[arg.curpage].__dict__:

        if arg.hobjs.__dict__[arg.curpage].__dict__[hname].obj.winfo_class()=="TScrollbar":

            if arg.hobjs.__dict__[arg.curpage].__dict__[hname].orient == "vertical":
                        
                h.__dict__[hname + "_scroll"] = arg.hobjs.__dict__[arg.curpage].__dict__[hname]
                h.__dict__[hname + "_scroll"].pos = sn(**{
                    "x" : h.__dict__[hname].pos.x + h.__dict__[hname].pos.w - g.scrollWidth,
                    "y" : h.__dict__[hname].pos.y, 
                    "w" : g.scrollWidth,
                    "h" : h.__dict__[hname].pos.h 
                })

            else:

                h.__dict__[hname + "_scroll"] = arg.hobjs.__dict__[arg.curpage].__dict__[hname]
                h.__dict__[hname + "_scroll"].pos = sn(**{
                    "x" : h.__dict__[hname].pos.x,
                    "y" : h.__dict__[hname].pos.y + h.__dict__[hname].pos.h - g.scrollWidth, 
                    "w" : h.__dict__[hname].pos.w,
                    "h" : g.scrollWidth
                })

    
    ## Properties and Variables
    for hname in h.__dict__:
#        print(arg.curpage, hname)
        if h.__dict__[hname].obj.winfo_class()=="TEntry":
            h.__dict__[hname].bind = sn(**{})
            if "password" in arg.hprops.__dict__[arg.curpage].__dict__[hname].bind.__dict__:
                h.__dict__[hname].bind.password = True
            if "keyboard" in arg.hprops.__dict__[arg.curpage].__dict__[hname].bind.__dict__:
                h.__dict__[hname].bind.keyboard = True
    
#        if h.__dict__[hname].obj.winfo_class()=="Treeview":
#            
#            h.__dict__[hname].table = sn(**{
#                "columns" : arg.hvars.__dict__[arg.curpage].__dict__[hname].header,
#                "data" : arg.hvars.__dict__[arg.curpage].__dict__[hname].data,
#            })
            
                
                
        
#        
    
    
    # For Scrollbar
#    handle.listScroll = sn(**{
#        "obj" : ttk.Scrollbar(master, orient="vertical",
#            command=handle.profList.obj.yview),
#        "pos" : sn(**{
#            "x": 451,
#            "y": 100,
#            "w": 35,
#            "h": 350,
#        }),
#    })


    ##### SUB PROPERTIES OF THE ABOVE HANDLES     
#    handle.profList.obj.configure(yscrollcommand=handle.listScroll.obj.set);
    
    ## Must contain same obj names in handle
#    imgs = sn(**{
#        "bg" : gui.imgTk(arg,"img/bg.jpg",(800,480)),
#    })
    
#    for img in imgs.__dict__:
#        h.__dict__[img].obj.image = h.__dict__[img].obj.image;
    
#    h.__dict__["bg"].obj.config(image = h.__dict__["bg"].obj.image);




    
####### SETUP FUNCTIONS #########

def setupMaster(arg):
    master = tk.Tk()
    master.title(g.app_name)
    arg.tk = tk
    if g.fullScreen:
        master.attributes("-fullscreen",True)
    master.geometry(str(g.frameWidth) + "x" + str(g.frameHeight))
    master.configure(bg=g.bgColor)
    if not g.cursor:
         master.config(cursor='none');
    arg.master = master;

def setupPages(arg):
    ######## Main Handle Variable that contains All GUI Elements ########
    pages = glob.glob("pages/pg_*.py");
    for ctr in range(0,len(pages)):
        ## Remove .py
        pages[ctr] = pages[ctr][6:-3];


    
    ## IMPORT AND GENERATE HANDLES AND FUNCTION HOLDERS
    ##################### Acces to Page Functions #####################
    
    # fcn = sn(**{})
    handles = sn(**{})
    
    for pagename in pages:
        arg.curpage = pagename
        sys.path.append("pages")
        sys.path.append("functions")
        # handles.__dict__[pagename] = importlib.import_module("pages." + pagename).page(arg);
        handles.__dict__[pagename] = importlib.import_module(pagename).page(arg);
        
        fcnFilename = "fcn_" + pagename[3:]

        # arg.__dict__[fcnFilename] = importlib.import_module("functions." + fcnFilename)
        arg.__dict__[fcnFilename] = importlib.import_module(fcnFilename)
        # fcn.__dict__[fcnFilename] = importlib.import_module("functions." + fcnFilename)
    
    # arg.fcn = fcn
    arg.handles = handles



# def sample(arg):
#     path = "system/gui/buttons/"
#     pathdot = "system.gui.buttons."
#     mymodules = glob.glob("system/gui/buttons/*.py")
#     for ctr in range(0,len(mymodules)):
#         # print(mymodules[ctr][len(path):-3])
#         name = mymodules[ctr][len(path):-3]
#         importlib.import_module(pathdot + name)

    # print(mymodules)


####### DEBUGGING ########
    
def dbgview(arg, preshowfcn, preshow=False):
    
    if preshow:
        preshowfcn
        pass # Run Preshow

    handles = arg.handles
    for hname in handles.__dict__[arg.curpage].__dict__:
        
        handles.__dict__[arg.curpage].__dict__[hname].obj.place(
            x=handles.__dict__[arg.curpage].__dict__[hname].pos.x,
            y=handles.__dict__[arg.curpage].__dict__[hname].pos.y,
            width=handles.__dict__[arg.curpage].__dict__[hname].pos.w,
            height=handles.__dict__[arg.curpage].__dict__[hname].pos.h,
        )
        
    arg.master.mainloop()
