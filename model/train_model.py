# model/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import joblib

def train_model():
    df = pd.read_csv('data/features.csv')
    X = df.drop('label', axis=1)
    y = df['label']

    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    model = SVC(kernel='linear', probability=True)
    model.fit(X_train, y_train)

    joblib.dump(model, 'model/model_svm.pkl')
    joblib.dump(encoder, 'model/label_encoder.pkl')

    print(f"Modelo entrenado y guardado. Precisión: {model.score(X_test, y_test):.2f}")

if __name__ == "__main__":
    train_model()
