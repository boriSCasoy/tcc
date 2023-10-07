from os import set_inheritable
import spidev
import time
import RPi.GPIO as GPIO

### Configurações Iniciais

# Interface com o ADS
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000
config_byte = 0x20

# Ler dados do ADS1210
def read_ads1210(channel):
	adc_data = spi.xfer2([config_byte | ((channel & 0x07) << 4), 0, 0])
	raw_value = (adc_data[1] << 8) | adc_data[2]
	return raw_value

# Configuração dos pinos GPIO
button1_pin = 17  # Botão 1
button2_pin = 18  # Botão 2
led_pin = 27  # Pino do LED


GPIO.setmode(GPIO.BCM)
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # pressionado == 1
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #pud_up pra 0
GPIO.setup(led_pin, GPIO.OUT)

# Variáveis para controlar o comportamento
max_value = 0
led_intensity = 60  # Inicialmente, 60% do valor máximo
running = False

try:
	while True:
    	# Verifica o estado dos botões
    	button1_state = GPIO.input(button1_pin)
    	button2_state = GPIO.input(button2_pin)

    	# Iniciar a leitura quando o botão 1 for pressionado
    	if button1_state == GPIO.LOW and not running:
        	running = True
        	max_value = 0  # Reinicia o valor máximo
        	GPIO.output(led_pin, GPIO.HIGH)  # Liga o LED

    	# Altera a intensidade do LED quando o botão 2 for pressionado
    	if button2_state == GPIO.LOW:
        	led_intensity = 40  # Muda para 40% do valor máximo

    	# Se o programa estiver em execução, faça a leitura e atualize o LED
    	if running:
        	value = read_ads1210(0)  # Lê o canal 0 do ADS1210
        	if value > max_value:
            	max_value = value

        	# Calcula a intensidade do LED com base no valor máximo
        	led_value = (max_value * led_intensity) // 100
        	# Limita o valor do LED para não ultrapassar o máximo
        	led_value = min(led_value, max_value)

        	# Define a intensidade do LED
        	GPIO.output(led_pin, GPIO.HIGH if led_value > 0 else GPIO.LOW)

    	time.sleep(0.1)

except KeyboardInterrupt:
	pass

finally:
	# Desliga o LED e faz a limpeza dos pinos GPIO antes de sair
	GPIO.output(led_pin, GPIO.LOW)
	GPIO.cleanup()

	# Fecha o dispositivo SPI
	spi.close()
```


continue working on this set_inheritable