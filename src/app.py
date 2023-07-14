from flask import request, Flask, jsonify
import tensorflow as tf
import numpy as np
from datetime import datetime


app = Flask(__name__)

model_name = "Freight Quote Classifer: Sklearn/RandomForest"
model_file = 'Models/model.dat.gz'
version = "v1.0.0"
port=8080

loaded_model = tf.keras.models.load_model('Models/quote.keras', compile=False)
loaded_model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), optimizer=tf.keras.optimizers.Adam(1e-4),  metrics=['accuracy'])


def model_predict(text: str) -> int:
    predictions = loaded_model.predict(np.array([text]))
    prediction = predictions[0][0]
    prediction_datetime = datetime.now()
    if prediction > 0.5:
        label = 1
    else:
        label = 0
    model_response = {"prediction": label, "probability": float(prediction), "datetime": str(prediction_datetime)}
    return jsonify(model_response)


@app.route('/info', methods=['GET'])
def info():
    result = {}
    result["name"] = model_name
    result["version"] = version
    return result


@app.route("/predict", methods=['POST'])
def predict():
    try:
        text=request.get_json()
        text=text['text']
        response=model_predict([text])
        return response
    except ValueError as e:
        return jsonify({'error': str(e).split('\n')[-1].strip()}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)






