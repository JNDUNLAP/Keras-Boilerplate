from flask import request, Flask, jsonify
import tensorflow as tf
import numpy as np



app = Flask(__name__)

model_name = "Freight Quote Classifer: Sklearn/RandomForest"
model_file = 'Models/model.dat.gz'
version = "v1.0.0"
port=8080

loaded_model = tf.keras.models.load_model('Models/quote.keras', compile=False)
loaded_model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), optimizer=tf.keras.optimizers.Adam(1e-4),  metrics=['accuracy'])


def model_predict(text: str) -> int:
    predictions = loaded_model.predict(np.array([text]))
    print(predictions)
    return predictions[0][0]


@app.route('/info', methods=['GET'])
def info():
    result = {}
    result["name"] = model_name
    result["version"] = version
    return result


@app.route("/predict", methods=['POST'])
def predict():
    try:
        text = request.get_json()
        text = text['text']
        pred = str(model_predict([text]))
        response = {'prediction':pred}
        return jsonify(response)
    except ValueError as e:
        return jsonify({'error': str(e).split('\n')[-1].strip()}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)






