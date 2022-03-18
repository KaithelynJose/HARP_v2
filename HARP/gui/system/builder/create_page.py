import os
import shutil

def index(pagename):
    
    # print("Default page has been successfully set to: " + 'pg_' + pagename)

    # Source path source = "templates/pagetemplate.py"          
    # Destination path 
    source = "templates/pagetemplate.py"
    destination = "pages/pg_" + pagename + ".py"

    if os.path.exists(destination):
        # os.remove(filename)
        print("The file already exists")
    else:
        # print("The file does not exist")

        # Copy the content of 
        # source to destination 
        dest = shutil.copyfile(source, destination) 
        print("Successfully created: " + dest)

        # Source path 
        source = "templates/functiontemplate.py"          
        # Destination path 
        destination = "functions/fcn_" + pagename + ".py"          
        # Copy the content of 
        # source to destination 
        dest = shutil.copyfile(source, destination) 
            
        print("Successfully created: " + dest)
    

    return

### RUN THIS FILE FOR QUICK VIEWING ###    
if __name__ == "__main__":
    index()