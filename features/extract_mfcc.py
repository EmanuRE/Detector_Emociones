# data/features_extraction.py

import os
import librosa
import numpy as np
import pandas as pd

DATASET_PATH = "data/ravdess"
OUTPUT_CSV = "data/features.csv"

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=22050)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfcc.T, axis=0)
    return mfcc_mean

def get_label(filename):
    emotion_map = {
        "01": "neutral",
        "02": "triste",
        "03": "feliz",
        "04": "enojado",
        "05": "miedo",
        "06": "disgustado",
        "07": "sorprendido",
        "08": "calmado"
    }
    emotion_code = filename.split("-")[2]
    return emotion_map.get(emotion_code, "desconocido")

def main():
    features = []
    for root, _, files in os.walk(DATASET_PATH):
        for file in files:
            if file.endswith(".wav"):
                file_path = os.path.join(root, file)
                data = extract_features(file_path)
                label = get_label(file)
                if label != "desconocido":
                    features.append(np.append(data, label))

    columns = [f"mfcc{i+1}" for i in range(13)] + ["label"]
    df = pd.DataFrame(features, columns=columns)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Características extraídas a: {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
