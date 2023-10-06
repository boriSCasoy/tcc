import time
i = 0

try:
    while i < 60:
        time.sleep(0.5)
        
        # Ler o estado do botão
        #estado_botao1 = GPIO.input(botao1_pin)
        #estado_botao2 = GPIO.input(botao2_pin)
        estado_botao1 = 1
        estado_botao2 = 0

        if estado_botao1:
            print("Botão 1")
        else
        if estado_botao2:
            print("Botão 2")
        else print("2 off")


        print (str(i)+"/60")
        i+=1

except KeyboardInterrupt:
    # Lidar com a interrupção do teclado (Ctrl+C)
    pass