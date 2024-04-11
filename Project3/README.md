# Project 3: Detecting Damage After Hurricane Harvey
The dataset we are looking at is images of buildings and land after Hurricane Harvey. We are trying to use Convolutional Neural Networks to predict whether the image contains damage or no damage. The images are 128x128 pixels with RGB values.

## Installation
Install this project by cloning the repository, making the scripts executable, and installing matplotlib For example:
```bash
git clone https://github.com/Kwabena86/SW-DSIGN-FOR-RESP-COE379L.git
pip install matplotlib --user
cd Project3
chmod u+x run_flask.py
chmod u+x submit_image.py
```

## Running the Code
To use the model, first you must start the model flask server:
```bash
./run_flask.sh
```
Then, you can submit images using the python script:
```bash
./submit_image.py <image_file>
```

### Examples
For example:
```bash
./submit_image.py test_image_damage.jpeg
```
The output should be:
```bash
test_image_damage.jpeg
 contains damage
```
If you want to submit a directory of images, you can put a star after the directory name:
For example:
```bash
./submit_image.py test_images/*
```
The program will output each image one by one:
```bash
test_images/-95.06356_29.831358.jpeg
 contains damage
test_images/-95.063575_30.036872.jpeg
 contains damage
test_images/-95.06363_29.831315000000004.jpeg
 contains damage
```
To get model information, you can submit a request to the flask serve:
```bash
./submit_image.py info
```
The output should be:
```bash
{
    'description': 'Classify images containing buildings after a hurricane (damaged or not damaged)', 
    'name': 'hurricane_damage', 
    'number_of_parameters': 2601153, 
    'version': 'v1'
}
```