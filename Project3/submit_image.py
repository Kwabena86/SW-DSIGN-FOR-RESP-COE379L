#!/usr/bin/python3
import sys
import requests
from matplotlib import image

def main(argv):
    # print(argv)
    for inputfile in argv:
        # inputfile = argv[0]
        try:
            img = image.imread(inputfile)
        except Exception as e:
            print(e)
            return
        
        # make the POST request passing the single test case as the `image` field:
        rsp = requests.post("http://172.17.0.1:5000/models/hurricane_damage/v1", json={"image": img.tolist()})

        # print the json response
        print(rsp.json())
        # d = np.array(im)

if __name__ == "__main__":
   main(sys.argv[1:])