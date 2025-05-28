# 🎙️ Detector Inteligente de Estados de Ánimo con Voz

Este proyecto implementa un sistema de detección de emociones a partir de la voz utilizando técnicas de **Machine Learning**, **procesamiento de audio**, y **comunicación con Arduino** para activar LEDs representativos de cada emoción. Además, los resultados se almacenan para análisis en **Power BI**.

---

## 🔧 Tecnologías y Herramientas Usadas

- `Python 3.10+`
- `Librosa` (para extracción de características MFCC)
- `scikit-learn` (para modelo SVM y codificador de etiquetas)
- `Joblib` (serialización del modelo)
- `PySerial` (comunicación con Arduino)
- `Arduino UNO` (control de LEDs)
- `Power BI` (visualización de emociones)
- `Tinkercad` (simulación y diagrama del circuito Arduino)

---

## 📁 Estructura del Proyecto
```
Detector_Emociones_2/
├── main.py
├── model/
│ ├── model_svm.pkl
│ └── label_encoder.pkl
├── powerbi/
│ └── emociones.csv
├── utils/
│ └── audio_capture.py
├── requirements.txt
└── README.md
```
## 🚀 Cómo Ejecutar el Proyecto

1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

Conecta tu Arduino por USB y asegúrate de que estás usando el puerto correcto (COM4 por defecto).

Ejecuta el programa:

bash
Copiar
Editar
python main.py

## 📊 Visualización de Datos
Los resultados se almacenan en powerbi/emociones.csv con la siguiente estructura:

fecha	hora	emoción	confianza	duracion	dispositivo	uuid	observación

Estos datos pueden ser conectados desde Power BI para visualizar gráficos de emociones por día, usuario, confianza promedio, etc.

## Recursos Adicionales
## 📘 Documentación del Proyecto:
https://deepwiki.com/EmanuRE/Detector_Emociones

## 📐 Diagrama de Arduino (Tinkercad):
https://www.tinkercad.com/things/6icK8JWV03i/editel?returnTo=%2Fdashboard&sharecode=GyviCjLefwxWs9z0A3eGxQG5o8DmW1O4wG3iGIt2H9k
