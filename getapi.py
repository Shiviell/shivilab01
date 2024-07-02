import sys
import requests

menue_str = """    
+------------------------------+
|   valid commend line argv    |
+------------------------------+
+ 1. /                         +
+ 2. /env                      +
+ 3. /env/<path>               +
+ 4. /dir                      +
+ 5. /dir/<name>               +
+------------------------------+
"""
def getapi(selection):
    try:
        url = ("http://localhost:5000/%s" % selection )
        r = requests.get(url)
        print (str(r))
        print (r.text)
    except:
        print ("fail http get request")
        print (menue_str)

if __name__ == "__main__":
    try:
        getapi(sys.argv[1])
    except:
        print ("fail http get request")
        print (menue_str)