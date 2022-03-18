from sys import platform


os = ""
if (platform == "linux") or (platform == "linux2"):
    os = "linux"
elif platform == "darwin": 
    os = "mac"
elif platform == "win32": 
    os = "win"

print("current os: ", os)

######## Function Holder for all Constant Global Variables ########
app_name = "HARP Guitar Tab Generator"
device = "laptop" if os=="win" else "rpi" 

server_root_folder_name = ""


####### Program Settings #######
dbg = False  ## SET TRUE FOR DEBUGGING PURPOSES
# serverurl = "http://localhost/myserver/"
if os == "mac":
    serverurl = "http://localhost:8083/" + server_root_folder_name + "/"
else:
    serverurl = "http://localhost/" + server_root_folder_name + "/"


projectNameLength = 3

# Set this to True if you want to set the application to fullscreen
activate_fullscreen = True if device=="rpi" else False


######## GUI Variables ########
defaultPage = "pg_main"
fullScreen = True if device=="rpi" else False
frameWidth = 800
frameHeight = 480
bgColor = "#F1F1F1"
bgColorBlack = "#000000"
cursor = False if device=="rpi" else True
scrollWidth = 30


####### Keyboard Variables ########
useKeyboard = True
kbshift = False
kbpage = ""
kbelement = ""
kbcurstring = ""
kbpassword = False

####### Keyboard Settings ########    
kbwadj = 4 ## HORIZONTAL MARGIN BETWEEN BUTTONS
kbhadj = 4 ## VERTICAL MARGIN BETWEEN BUTTONS


####### System Settings #######



#_____ BUILDER SETTINGS _____#
builder_title = "Visual"
builder_title_sub = "Py Builder 1.0"
builder_font = "isometric4"
defaultMessageBoxTitle = ""
#_____ BUILDER SETTINGS _____#



####### System Settings #######
