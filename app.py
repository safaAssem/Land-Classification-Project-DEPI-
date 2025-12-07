# app.py
import os
from flask import Flask, request, render_template, send_from_directory, jsonify
from utils import predict_image, save_overlay, CLASS_NAMES, LAND_INFO
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow import keras

app = Flask(__name__)

MODEL_PATH = os.path.join('models', 'efficient_model_96.keras')
model = keras.models.load_model(MODEL_PATH)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'no file uploaded'}), 400
    
    file = request.files['image']
    pil = Image.open(file.stream)

    class_id, label, confidence, top3 = predict_image(model, pil)
    
    info = LAND_INFO[label]

    out_filename = os.path.join('static', 'output', f'result_{np.random.randint(1e9)}.png')
    save_overlay(pil, f"{label} ({confidence:.2f})", out_filename)

    return render_template(
        'result.html',
        label=label,
        confidence=confidence *100,
        output_image='/' + out_filename,
        info=info,
        top3=top3
    )


@app.route('/static/output/<path:filename>')
def serve_output(filename):
    return send_from_directory('static/output', filename)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 7860))  # HF يعطي PORT تلقائي
    app.run(host="0.0.0.0", port=port, debug=True)
