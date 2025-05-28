import pandas as pd
import librosa
import numpy as np
import joblib
import serial
import time
from datetime import datetime
import csv
import os
from utils.audio_capture import grabar_audio

# Cargar modelos entrenados
modelo = joblib.load("model/model_svm.pkl")
encoder = joblib.load("model/label_encoder.pkl")

# Conectar con Arduino
try:
    arduino = serial.Serial("COM4", 9600)  # Cambia COM4 si tu puerto es diferente
    time.sleep(2)
    print("🔌 Conexión con Arduino establecida.")
except Exception as e:
    arduino = None
    print("⚠️ No se pudo conectar con Arduino:", e)

# Grabar audio
archivo_audio = grabar_audio(duracion=4)

# Extraer características MFCC
def extraer_mfcc(ruta_audio):
    y, sr = librosa.load(ruta_audio, sr=22050)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfcc.T, axis=0)
    columnas = [f"mfcc{i+1}" for i in range(13)]
    return pd.DataFrame([mfcc_mean], columns=columnas)

try:
    caracteristicas = extraer_mfcc(archivo_audio)
    prediccion = modelo.predict(caracteristicas)
    emocion = encoder.inverse_transform(prediccion)[0]
    print(f"🧠 Emoción detectada: {emocion}")

    # Enviar emoción al Arduino
    if arduino:
        arduino.write(f"{emocion}\n".encode())
        print("📤 Emoción enviada a Arduino.")

    # Guardar en CSV (para Power BI)
    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    archivo_csv = "powerbi/emociones.csv"

    # Escribir encabezado solo si no existe el archivo
    escribir_encabezado = not os.path.isfile(archivo_csv)

    with open(archivo_csv, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if escribir_encabezado:
            writer.writerow(["fecha", "hora", "emocion"])
        writer.writerow([fecha, hora, emocion])

    print("✅ Emoción registrada en CSV.")

except Exception as e:
    print("❌ Error durante la detección de emoción:", e)
