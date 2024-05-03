#!/bin/bash

docker build -t jakewendling/ml_diagnosis .
# docker pull jakewendling/ml_diagnosis
docker run -it --rm -p 5000:5000 jakewendling/ml_diagnosis
