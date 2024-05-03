#!/usr/bin/python3
import sys
import requests
from matplotlib import image

def main(argv):
    if argv[0] == "info":
        rsp = requests.get("http://172.17.0.1:5000/models/diagnosis_model/v1")
        print(rsp.json())
    else:
        input = argv
        # for input in argv:
        # make the POST request passing the single test case as the `image` field:
        rsp = requests.post("http://172.17.0.1:5000/models/diagnosis_model/v1", json={"text": input})

        # print the json response
        result = rsp.json()#['result']
        print(f"{input}\n {result}")

if __name__ == "__main__":
   main(sys.argv[1:])