import spidev
import time

#import RPi.GPIO as GPIO

# Configuração inicial
spi = spidev.SpiDev()
spi.open(0, 0) #tem q ver se as portas estão certas, o primeiro numero é a porta
spi.max_speed_hz = 1000000 #taxa de comunicação
config_byte = 0x20 #


# Função para ler dados do ADS1210
def read_ads1210(channel):
	adc_data = spi.xfer2([config_byte | ((channel & 0x07) << 4), 0, 0])
	raw_value = (adc_data[1] << 8) | adc_data[2]
	return raw_value

try:
    while True:
        time.sleep(0.1)
		a = read_ads1210(0)
		print("Config Byte", config_byte)
		print("A", a)
		
except KeyboardInterrupt:
    # Lidar com a interrupção do teclado (Ctrl+C)
    pass