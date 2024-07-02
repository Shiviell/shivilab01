import os
import sys

def main(path) :
    try:
        print (path[0])
        print (os.listdir(path[0]))
    except:
        print("error: chack path")
if __name__=="__main__":
    main(sys.argv[1:])

