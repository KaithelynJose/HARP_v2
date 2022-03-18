import os

def index(pagename):
    

    # filename = os.path.basename(__file__)
    # path = os.path.dirname(__file__)
    # filepath = path + "/../../g.py"
    # print(path)
    # print(os.path.dirname(__file__))
    # f=open(path, "r")
    # if f.mode == 'r':
    #     contents = f.read()
    #     print(contents)
    # f.close()

    # print("Success changing default page to: " + pagename)

    # with open(filepath) as fp:
    #     line = fp.readline()
    #     cnt = 1
    #     while line:
    #         if line.startswith('defaultPage'):
    #             print("Default PAGE found Line {}: {}".format(cnt, line.strip()))
    #             line[cnt] = "defaultPage = \"New Value\""
    #         print("Line {}: {}".format(cnt, line.strip()))
    #         line = fp.readline()
    #         cnt += 1

    # f = open(filepath, "r")
    # lines = f.readlines()
    # f.close()
    # for i, line in enumerate(lines):
    #     # if line.split('=')[0].strip(' \n') == key:
    #     if line.startswith('defaultPage'):
    #         lines[i] = 'defaultPage = ' + '"pg_' + pagename +  '"' + '\n'
    # f = open(filepath, "w")
    # f.write("".join(lines))
    # f.close()
    # print("Default page has been successfully set to: " + 'pg_' + pagename)

    # print("Default page has been successfully set to: " + 'pg_' + pagename)

    # Source path source = "templates/pagetemplate.py"          
    # Destination path 
    filename = "pages/pg_" + pagename + ".py"
    # Copy the content of 
    # source to destination 

    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")

    # dest = shutil.copyfile(source, destination) 
    # print("Successfully created: " + dest)

    # Source path 
    # filename = "templates/functiontemplate.py"          
    # Destination path 
    filename = "functions/fcn_" + pagename + ".py"  
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")        
    # Copy the content of 
    # source to destination 
    # dest = shutil.copyfile(source, destination) 


    print("Page w/ functions has been deleted.")
    return

### RUN THIS FILE FOR QUICK VIEWING ###    
if __name__ == "__main__":
    index()