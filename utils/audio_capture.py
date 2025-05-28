import sounddevice as sd
from scipy.io.wavfile import write

def grabar_audio(duracion=4, nombre_archivo="temp.wav"):
    fs = 22050  # Frecuencia de muestreo
    print(f"🎙️ Grabando audio durante {duracion} segundos...")
    audio = sd.rec(int(duracion * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Esperar a que termine la grabación
    write(nombre_archivo, fs, audio)
    print("✅ Grabación finalizada.")
    return nombre_archivo

