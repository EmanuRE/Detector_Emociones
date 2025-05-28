# model/predict.py

import joblib
from features.extract_mfcc import extract_features

# Cargar el modelo y el codificador
modelo = joblib.load('model/model_svm.pkl')
encoder = joblib.load('model/label_encoder.pkl')

def predecir_emocion(ruta_audio):
    # Extraer las mismas características que se usaron para entrenar
    features = extract_features(ruta_audio).reshape(1, -1)
    
    # Predecir emoción codificada
    emocion_codificada = modelo.predict(features)[0]

    # Decodificar la emoción a etiqueta en español
    emocion = encoder.inverse_transform([emocion_codificada])[0]
    return emocion
