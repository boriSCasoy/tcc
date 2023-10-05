import RPi.GPIO as GPIO
import time

# Configurar a numeração dos pinos GPIO
GPIO.setmode(GPIO.BOARD)

# Configurar o pino do botão como entrada
botao_pin1 = 11
botao_pin2= 13

GPIO.setup(botao_pin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(botao_pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        time.sleep(0.01)
        # Ler o estado do botão
        estado_botao1 = GPIO.input(botao_pin)
        estado_botao2 = GPIO.input(botao_pin)

        # Verificar se o botão foi pressionado (estado == False)
        if estado_botao == False:
            print("Botão pressionado")
        else:
            print("Botão solto")

except KeyboardInterrupt:
    # Lidar com a interrupção do teclado (Ctrl+C)
    pass

finally:
    # Limpar os recursos do GPIO
    GPIO.cleanup()
