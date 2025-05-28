// Arduino.ino

void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT); // Feliz - Verde
  pinMode(3, OUTPUT); // Triste - Azul
  pinMode(4, OUTPUT); // Enojado - Rojo
  pinMode(5, OUTPUT); // Miedo - Amarillo
  pinMode(6, OUTPUT); // Neutral - Blanco
  pinMode(7, OUTPUT); // Sorprendido
}

void loop() {
  if (Serial.available()) {
    String emocion = Serial.readStringUntil('\n');
    emocion.trim();

    // Apagar todos los LEDs primero
    for (int i = 2; i <= 6; i++) {
      digitalWrite(i, LOW);
    }

    if (emocion == "feliz") {
      digitalWrite(2, HIGH);
    } else if (emocion == "triste") {
      digitalWrite(3, HIGH);
    } else if (emocion == "enojado") {
      digitalWrite(4, HIGH);
    } else if (emocion == "miedo") {
      digitalWrite(5, HIGH);
    } else if (emocion == "neutral") {
      digitalWrite(6, HIGH);
    } else if (emocion == "sorprendido") {
      // Puedes usar otro pin, por ejemplo el 7 para sorprendido
      pinMode(7, OUTPUT);
      digitalWrite(7, HIGH);
    }
  }
}


void apagarTodos() {
  for (int i = 2; i <= 6; i++) {
    digitalWrite(i, LOW);
  }
}

