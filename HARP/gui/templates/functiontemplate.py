import sys
sys.path.append("..")
sys.path.append("../plugins")
sys.path.append("../pages")
sys.path.append("../system")

## IMPORT PLUGINS AND MODULES
import g, gui, styles


def preshow(arg):
    
    if "quickpreview" in arg.__dict__:
        ## Quick View Functions Here
    
        return True
    
    ## Main Functions Here
    
    
    return True

def postshow(arg):
    
    if "quickpreview" in arg.__dict__:
        ## Quick View Functions Here
    
        return True
    
    ## Main Functions Here
    
    
    return True

