# Project 4: Diagnosing Symptoms
The dataset we are looking at contains symptoms and their corresponding diagnoses. We are trying to use transformers and RNNs to diagnose input text that describes symptoms.

## Installation
Install this project by cloning the repository, making the scripts executable, and extracting the model:
```bash
git clone https://github.com/Kwabena86/SW-DSIGN-FOR-RESP-COE379L.git
cd SW-DSIGN-FOR-RESP-COE379L
cd ProjectFinal
chmod u+x run_flask.py
chmod u+x submit_text.py
```

Download the models.zip from https://drive.google.com/file/d/1OhvRgPe6iE53rW28TWskvlunqdle09Sz/view?usp=sharing
and move it into the ProjectFinal folder and unzip it:
```bash
unzip models.zip
```

## Running the Code
To use the model, first you must start the model flask server:
```bash
./run_flask.sh
```
Then, you can submit images using the python script:
```bash
./submit_text.py "<symptoms>"
```

### Examples
For example:
```bash
./submit_text.py "I have itchy red spots on my skin"
```
The output should be:
```bash
['I have itchy red spots on my skin']
 {'diagnosis': 'chicken pox', 'score': 0.9349539875984192}
```

To get model information, you can submit a request to the flask serve:
```bash
./submit_text.py info
```
The output should be:
```bash
{
    'description': 'Classify text containing symptoms (one of 22 diagnoses)', 
    'diagnoses': 
        ['allergy', 'arthritis', 'bronchial asthma', 'cervical spondylosis', 'chicken pox', 'common cold', 'dengue', 'diabetes', 'drug reaction', 'fungal infection', 'gastroesophageal reflux disease', 'hypertension', 'impetigo', 'jaundice', 'malaria', 'migraine', 'peptic ulcer disease', 'pneumonia', 'psoriasis', 'typhoid', 'urinary tract infection', 'varicose veins'], 
    'name': 'diagnosis_model', 
    'pretrained_model': 'distilbert-base-uncased', 
    'version': 'v1'
}
```