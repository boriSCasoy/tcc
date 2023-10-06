import RPi.GPIO as GPIO
import time


# ordem física da placa (gpio.bcm)
GPIO.setmode(GPIO.BOARD)

# config dos botoes
botao1_pin = 11
botao2_pin= 13

GPIO.setup(botao1_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botao2_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
i = 0

try:
    while i < 1000:
        time.sleep(0.01)
        
        # Ler o estado do botão
        estado_botao1 = GPIO.input(botao1_pin)
        estado_botao2 = GPIO.input(botao2_pin)

        if estado_botao1 == True:
            print("Botão pressionado")
        elif estado_botao1 == True:
            print("Botão pressionado")
        else:
            print("Botões soltos")
        print(i + )

except KeyboardInterrupt:
    # Lidar com a interrupção do teclado (Ctrl+C)
    pass

finally:
    # Limpar os recursos do GPIO
    GPIO.cleanup()