import RPi.GPIO as GPIO
import time

# Configurar a numeração dos pinos GPIO
GPIO.setmode(GPIO.BCM)

# Configurar o pino do botão como entrada
botao_pin = 16  # Substitua pelo número do pino GPIO que você está usando
GPIO.setup(botao_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        time.sleep(0.1)
        # Ler o estado do botão
        estado_botao = GPIO.input(botao_pin)

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
