##### HELPER FUNCTIONS #######
import g
from urllib import request, parse, error
import json
from tkinter import messagebox


def db(arg,api,data={},suppress=False):
    print("HTTP REQUEST: " + g.serverurl + "index.php/apis/" + api)
    print("HTTP DATA: ", data)

    postdata = parse.urlencode(data).encode()
 
    try:
        rsp = request.urlopen(g.serverurl + "index.php/apis/" + api, data=postdata)
        rsp = rsp.read().decode("utf-8")
        print("--- HTTP RESPONSE: " + rsp + " :HTTP RESPONSE END: --- ")
    except Exception as e:
    	# errorMsg = e.read().decode("utf-8")
    	# print("HTTP ERROR: " + errorMsg)

        print("HTTP ERROR: - Exception Error:" + str(e))
    	# if not suppress:
    	#     messagebox.showerror("Network Error", errorMsg)
        return []


    rspdict = json.loads(rsp)
    
    return rspdict













### TO MAKE JSON REPONSE NAMESPACED

# def http(arg,urlmethod,data={}):  ###### String URL, dictionary data
        
#     ## URLLIB POST
#     postdata = parse.urlencode(data).encode();
#     try:
#         rsp = request.urlopen(g.serverurl + "index.php/apis/" + urlmethod, data=postdata)
#         rsp = rsp.read().decode("utf-8");
#     except Exception as e:
#         return {
#             "stat" : False,
#             "title" : "Network Error",
#             "msg" : "A network error has occured:\n\n" + str(e),    
#         }
    
#     ## JSON DECODE - CI: echo json_encode($result->result());
#     rspjson = json.loads(rsp);
    
#     return rspjson

# def httpval(arg,rsp):
#     if rsp["stat"]:
#         return False;
#     else:
#         messagebox.showerror(rsp["title"],rsp["msg"]);
#         return True;

# def httpvalok(arg,rsp):
#     messagebox.showinfo(rsp["title"],rsp["msg"]);