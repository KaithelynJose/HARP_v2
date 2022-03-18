import os

def builder_clean():
    filename = "__pycache__"

    if os.path.exists(filename):
        pass
        # os.remove(filename)

    mydicfolder = ["functions","pages","plugins","system","system/builder","system/gui","templates"]
    for i in mydicfolder:

        filename = i + "/" + filename  
        if os.path.exists(filename):
            print(filename)
            os.remove(filename)

    print("cleaning completed.")

    return

### RUN THIS FILE FOR QUICK VIEWING ###    
if __name__ == "__main__":
    builder_clean()