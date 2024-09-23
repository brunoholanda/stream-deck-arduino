// Definindo os pinos para os botões
const int buttonPins[] = {2, 3, 4, 5, 6, 7};
const int numButtons = 6;

void setup() {
  // Inicializa os pinos dos botões como entradas
  for (int i = 0; i < numButtons; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
  Serial.begin(9600); // Inicia a comunicação serial
}

void loop() {
  for (int i = 0; i < numButtons; i++) {
    if (digitalRead(buttonPins[i]) == LOW) { // Botão pressionado
      Serial.print(i + 1); // Envia o número do botão pressionado
      Serial.println();
      delay(200); // Debounce delay
    }
  }
}