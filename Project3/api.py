import tensorflow as tf
model = tf.keras.models.load_model('clothes.keras')

from flask import Flask

app = Flask(__name__)

@app.route('/models/hurricane_damage/v1', methods=['GET'])
def model_info():
   return {
      "version": "v1",
      "name": "hurricane_damage",
      "description": "Classify images containing buildings after a hurricane (damaged or not damaged)",
      "number_of_parameters": 0
   }

@app.route('/models/hurricane_damage/v1', methods=['POST'])
def classify_clothes_image():
   im = request.json.get('image')
   if not im:
      return {"error": "The `image` field is required"}, 404
   try:
      data = preprocess_input(im)
   except Exception as e:
      return {"error": f"Could not process the `image` field; details: {e}"}, 404
   return { "result": model.predict(data).tolist()}

def preprocess_input(im):
   """
   Converts user-provided input into an array that can be used with the model.
   This function could raise an exception.
   """
   # convert to a numpy array
   d = np.array(im)
   # then add an extra dimension
   return d.reshape(1, 28, 28)

# start the development server
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')