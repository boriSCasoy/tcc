import RPi.GPIO as GPIO

# Configuração do dispositivo SPI (mesmo código da resposta anterior)
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000
config_byte = 0x20

# Função para ler dados do ADS1210
def read_ads1210(channel):
	adc_data = spi.xfer2([config_byte | ((channel & 0x07) << 4), 0, 0])
	raw_value = (adc_data[1] << 8) | adc_data[2]
	return raw_value
