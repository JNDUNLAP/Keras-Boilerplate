from flask import request, Flask, jsonify
import numpy as np

import os
from datetime import datetime
from src.model import loaded_model
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
PORT = int(os.getenv('PORT'))


def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Text must be a string.")
    # Todo: add preprocssing at the server level
    return text


@app.route("/predict", methods=['POST'])
def predict():
    try:
        data=request.get_json()
        text=validate_input(data['text'])
        predictions = loaded_model.predict(np.array([text]))
        prediction = predictions[0][0]
        prediction_datetime = datetime.now()
        label = 1 if prediction > 0.5 else 0
        return jsonify(
            prediction=label,
            probability=float(prediction),
            datetime=str(prediction_datetime)
        )
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)






