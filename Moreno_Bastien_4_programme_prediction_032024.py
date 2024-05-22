import tensorflow as tf
from flask import Flask, jsonify, request
from PIL import Image, ImageOps,ImageFilter
from keras.preprocessing.image import img_to_array
import io
import numpy as np
import pickle

app = Flask(__name__)

# Chargement du modèle
model_path = './model_xception.h5'
model = tf.keras.models.load_model(model_path)

# Chargement des labels
with open('index_to_class.pkl', 'rb') as file:
    classes_labels = pickle.load(file)

# Fonction de preprocessing
def preprocess(img):
    img_resized = img.resize((299, 299))
    img_autocontrast = ImageOps.autocontrast(img_resized)
    img_equalized = ImageOps.equalize(img_autocontrast)
    img_filtered = img_equalized.filter(ImageFilter.GaussianBlur(radius=2))
    return img_filtered

@app.route("/predict", methods=['POST'])
def predict():
    # Récupérer l'image
    file = request.files['file']
    image = file.read()

    # Ouvrir l'image
    img = Image.open(io.BytesIO(image))

    # Traitement de l'image
    img_processed = preprocess(img)

    # Convertir l'image en tableau numpy
    img_array = img_to_array(img_processed)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array/255

    # Prédiction
    pred = model.predict(img_array)[0]
    max_index = np.argmax(pred)
    max_label = classes_labels[max_index]
    max_proba = pred[max_index]

    return jsonify({'prediction': {'label': max_label, 'probability': float(max_proba)}})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
