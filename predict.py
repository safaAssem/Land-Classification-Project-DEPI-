import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# تأكد إن المسار صحيح وصيغة الموديل مظبوطة
keras_model = tf.keras.models.load_model("efficient_model_96.keras")  

classes = ["AnnualCrop", "Forest", "HerbaceousVegetation", "Highway", 
           "Industrial", "Pasture", "PermanentCrop", "Residential", "River", "SeaLake"]

def predict_image(model, img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_arr = image.img_to_array(img)
    img_arr = img_arr / 255.0
    img_arr = np.expand_dims(img_arr, axis=0)

    preds = model.predict(img_arr)
    class_id = np.argmax(preds)
    confidence = preds[0][class_id]

    print(f"\nTop Prediction: {classes[class_id]}  ({confidence*100:.2f}%)")

    top3 = preds[0].argsort()[-3:][::-1]
    print("\nTop 3 classes:")
    for i in top3:
        print(f"{classes[i]}: {preds[0][i]*100:.2f}%")

    return class_id

predict_image(keras_model, "test_images\Residential_43.jpg")
