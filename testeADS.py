import spidev
import time

# Configuração inicial
spi = spidev.SpiDev()
spi.open(0, 0)  # Verifique se as portas estão corretas, o primeiro número é a porta
spi.max_speed_hz = 1000000  # Taxa de comunicação
config_byte = 0x20

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
