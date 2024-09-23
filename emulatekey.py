import serial
import time
import keyboard

# Configura a porta serial (ajuste conforme necessário)
arduino_port = 'COM3'  # Substitua pela porta correta
baud_rate = 9600

# Conecta ao Arduino
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Aguarda a conexão estabilizar

try:
    while True:
        if ser.in_waiting > 0:
            button_value = ser.readline().decode('utf-8').strip()
            if button_value:
                button_num = int(button_value)
                print(f'Botão {button_num} pressionado!')

                # Emula um atalho de teclado com base no botão pressionado
                if button_num == 1:
                    keyboard.send('ctrl+alt+c')  # Ctrl + Alt + C
                elif button_num == 2:
                    keyboard.send('ctrl+alt+b')  # Ctrl + Alt + B
                elif button_num == 3:
                    keyboard.send('ctrl+alt+d')  # Ctrl + Alt + D
                elif button_num == 4:
                    keyboard.send('ctrl+alt+e')  # Ctrl + Alt + E
                elif button_num == 5:
                    keyboard.send('ctrl+alt+f')  # Ctrl + Alt + F
                elif button_num == 6:
                    keyboard.send('ctrl+alt+g')  # Ctrl + Alt + G

except KeyboardInterrupt:
    print("Saindo...")
finally:
    ser.close()
