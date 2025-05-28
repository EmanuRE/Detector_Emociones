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
from uuid import uuid4

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

    # Obtener probabilidad si está disponible
    if hasattr(modelo, "predict_proba"):
        probas = modelo.predict_proba(caracteristicas)[0]
        confianza = max(probas)
    else:
        confianza = "N/A"

    # Enviar emoción al Arduino
    if arduino:
        arduino.write(f"{emocion}\n".encode())
        print("📤 Emoción enviada a Arduino.")

    # Preparar datos para guardar en CSV
    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    duracion_audio = 4  # segundos
    fuente = "micrófono"
    id_sesion = str(uuid4())[:8]
    comentario = input("💬 Comentario (opcional): ")

    # Ruta del archivo CSV
    archivo_csv = "powerbi/emociones.csv"

    # Escribir encabezado si no existe
    escribir_encabezado = not os.path.isfile(archivo_csv)

    with open(archivo_csv, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        if escribir_encabezado:
            writer.writerow([
                "fecha", "hora", "emocion", "confianza", "duracion_audio",
                "fuente", "id_sesion", "comentario"
            ])
        writer.writerow([
            fecha, hora, emocion, f"{confianza:.2f}" if isinstance(confianza, float) else confianza,
            duracion_audio, fuente, id_sesion, comentario
        ])

    print("✅ Emoción registrada en CSV.")

except Exception as e:
    print("❌ Error durante la detección de emoción:", e)
