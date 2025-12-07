
# utils.py
import numpy as np
from PIL import Image
import os


IMG_SIZE = (224, 224)
CLASS_NAMES = ['AnnualCrop', 'Forest', 'HerbaceousVegetation', 'Highway', 'Industrial', 'Pasture', 'PermanentCrop', 'Residential', 'River', 'SeaLake']
LAND_INFO = {
    "AnnualCrop": {
        "description": "Land used for short-term crops such as wheat and corn that require annual renewal.",
        "recommended_uses": ["Seasonal agriculture", "Agricultural experiments", "Grain production"],
        "warnings": ["Highly affected by weather fluctuations", "Soil erosion risk when vegetation cover is low"],
        "suggestions": ["Improve irrigation during dry periods", "Use crop rotation to preserve soil quality"]
    },
    "Forest": {
        "description": "Areas dominated by dense tree cover and natural ecosystems.",
        "recommended_uses": ["Eco-tourism", "Biodiversity conservation", "Afforestation"],
        "warnings": ["High wildfire risk during heat waves", "Deforestation negatively affects soil stability"],
        "suggestions": ["Monitor humidity and temperature", "Avoid open fires near forested areas"]
    },
    "HerbaceousVegetation": {
        "description": "Natural or grazing land covered by low herbaceous plants.",
        "recommended_uses": ["Livestock grazing", "Environmental conservation", "Agricultural rehabilitation"],
        "warnings": ["Degradation risk due to overgrazing", "Fire risk in dry seasons"],
        "suggestions": ["Regulate grazing activity", "Monitor rainfall and soil moisture"]
    },
    "Highway": {
        "description": "Major transportation roads designed for high-density traffic between cities.",
        "recommended_uses": ["Ground transportation", "Logistics and distribution"],
        "warnings": ["High accident risk", "Noise and air pollution"],
        "suggestions": ["Use safe pedestrian crossings", "Add green barriers to reduce pollution"]
    },
    "Industrial": {
        "description": "Areas containing industrial facilities, warehouses, and production lines.",
        "recommended_uses": ["Commercial and industrial activities", "Storage and logistics"],
        "warnings": ["Air and water pollution risk", "Not suitable for housing or farming"],
        "suggestions": ["Monitor air quality regularly", "Create green buffer zones"]
    },
    "Pasture": {
        "description": "Land dedicated to livestock grazing and animal farming.",
        "recommended_uses": ["Cattle and sheep grazing", "Meat and dairy production"],
        "warnings": ["Soil degradation due to excessive grazing", "High dependency on rainfall"],
        "suggestions": ["Implement rotational grazing", "Provide water sources during dry seasons"]
    },
    "PermanentCrop": {
        "description": "Land used for long-term crops such as olives, grapes, and fruit orchards.",
        "recommended_uses": ["Horticulture", "Long-term agricultural investment"],
        "warnings": ["High water consumption", "Sensitive to frost and extreme heat"],
        "suggestions": ["Install efficient irrigation systems", "Monitor weather conditions closely"]
    },
    "Residential": {
        "description": "Urban or suburban areas containing housing and community services.",
        "recommended_uses": ["Residential living", "Community services", "Small commercial activities"],
        "warnings": ["Possible traffic congestion", "Limited green spaces"],
        "suggestions": ["Expand public parks", "Improve traffic management"]
    },
    "River": {
        "description": "Flowing freshwater bodies such as rivers and streams.",
        "recommended_uses": ["Irrigation", "Fishing", "Hydropower generation"],
        "warnings": ["Seasonal flooding risk", "Water pollution affects wildlife"],
        "suggestions": ["Monitor water levels", "Avoid waste dumping near the river"]
    },
    "SeaLake": {
        "description": "Large water bodies such as lakes or coastal areas with environmental and tourism value.",
        "recommended_uses": ["Fishing", "Tourism", "Water-based activities"],
        "warnings": ["High soil salinity near the shoreline", "Risk of coastal flooding and storms"],
        "suggestions": ["Build protective barriers", "Manage water resources sustainably"]
    }
}


def predict_image(model, pil_image):
    """
    Function to predict a single image
    Input: PIL Image
    Output: class_id, class_label, confidence
    """
    img = pil_image.resize((224, 224)).convert('RGB')
    img_arr = np.array(img) / 255.0
    img_arr = np.expand_dims(img_arr, axis=0)

    preds = model.predict(img_arr)
    class_id = np.argmax(preds)
    confidence = float(preds[0][class_id])

    # Top 3 predictions 
    top3_idxs = preds[0].argsort()[-3:][::-1]
    top3 = [
        {"class": CLASS_NAMES[i], "conf": float(preds[0][i])}
        for i in top3_idxs
    ]

    return class_id, CLASS_NAMES[class_id], confidence, top3




def save_overlay(original_pil, predicted_class, out_path):
# Simple overlay: write predicted label on the image and save
 img = original_pil.copy()
 from PIL import ImageDraw, ImageFont
 draw = ImageDraw.Draw(img)

 try:
    font = ImageFont.truetype("arial.ttf", 20)
 except Exception:
    font = ImageFont.load_default()

 text = f"Pred: {predicted_class}"
 draw.rectangle([(0,0),(img.width,30)], fill=(255,255,255,200))
 draw.text((5,5), text, fill=(0,0,0), font=font)
 
 os.makedirs(os.path.dirname(out_path), exist_ok=True)
 img.save(out_path)
 return out_path