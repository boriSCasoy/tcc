import time
i = 0

try:
    while i <= 100:
        time.sleep(0.05)
        
        # Ler o estado do botão
        #estado_botao1 = GPIO.input(botao1_pin)
        #estado_botao2 = GPIO.input(botao2_pin)
        botao1 = 1
        botao2 = 0 # linha pra testar só no código

        print(botao1, "      ", botao2)
        i+=1

except KeyboardInterrupt:
    # Lidar com a interrupção do teclado (Ctrl+C)
    pass