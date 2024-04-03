#!/usr/bin/python3
import sys
import requests
from matplotlib import image

def main(argv):
    print(argv)
    inputfile = argv[0]
    img = image.imread(inputfile)

    # make the POST request passing the sinlge test case as the `image` field:
    rsp = requests.post("http://172.17.0.1:5000/models/hurricane_damage/v1", json={"image": img.tolist()})

    # print the json response
    rsp.json()

if __name__ == "__main__":
   main(sys.argv[1:])