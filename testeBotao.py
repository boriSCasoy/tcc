import RPi.GPIO as GPIO
import time

button1_pin = 16  # Botão 1
button2_pin = 18  # Botão 2

GPIO.setmode(GPIO.BCM)  
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # pressionado == 1
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #pud_up pra 0

try:
    while True:
        time.sleep(0.05)
        
        # Ler o estado do botão
        #estado_botao1 = GPIO.input(botao1_pin)
        #estado_botao2 = GPIO.input(botao2_pin)
        botao1 = GPIO.input(button1_pin)
        botao2 = GPIO.input(button2_pin)

        print(botao1, "  -  ", botao2)
    

except KeyboardInterrupt:
    # Lidar com a interrupção do teclado (Ctrl+C)
    pass