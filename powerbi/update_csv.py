import csv
from datetime import datetime
import os

def guardar_emocion_csv(emocion, archivo='powerbi/emociones.csv'):
    os.makedirs(os.path.dirname(archivo), exist_ok=True)
    ahora = datetime.now()
    fila = [ahora.strftime('%Y-%m-%d'), ahora.strftime('%H:%M:%S'), emocion]

    archivo_existe = os.path.exists(archivo)
    
    with open(archivo, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not archivo_existe:
            writer.writerow(['Fecha', 'Hora', 'Emocion'])
        writer.writerow(fila)
        print(f"📊 Emoción registrada en CSV: {fila}")
