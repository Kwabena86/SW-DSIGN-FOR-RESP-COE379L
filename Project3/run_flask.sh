#!/bin/bash


docker build -t jakewendling/ml-hurricane-api .
docker run -it --rm -p 5000:5000 jakewendling/ml-hurricane-api
