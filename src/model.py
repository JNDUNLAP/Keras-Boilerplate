import tensorflow as tf
import os
from dotenv import load_dotenv
load_dotenv()
MODEL_PATH = os.path.join(os.getcwd(), os.getenv('MODEL_PATH'))


def load_model(model_path):
    model = tf.keras.models.load_model(model_path, compile=False)
    model.compile(
        loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
        optimizer=tf.keras.optimizers.Adam(1e-4),  
        metrics=['accuracy']
    )
    return model


loaded_model = load_model(MODEL_PATH)