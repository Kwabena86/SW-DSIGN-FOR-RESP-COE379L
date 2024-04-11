#!/usr/bin/python3
import sys
import requests
from matplotlib import image

def main(argv):
    if argv[0] == "info":
        rsp = requests.get("http://172.17.0.1:5000/models/hurricane_damage/v1")
        print(rsp.json())
    else:
        for inputfile in argv:
            try:
                img = image.imread(inputfile)
            except Exception as e:
                print(e)
                return
            
            # make the POST request passing the single test case as the `image` field:
            rsp = requests.post("http://172.17.0.1:5000/models/hurricane_damage/v1", json={"image": img.tolist()})

            # print the json response
            result = rsp.json()['result']
            print(f"{inputfile}\n {result}")

if __name__ == "__main__":
   main(sys.argv[1:])