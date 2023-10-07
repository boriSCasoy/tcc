import RPi.GPIO as GPIO
import spidev
import time

# Mapeamento das portas GPIO para o Raspberry Pi 4 (modelo BOARD)
MISO = 21  # Pino 40 - Master In Slave Out
MOSI = 19  # Pino 35 - Master Out Slave In
SCLK = 23  # Pino 33 - Serial Clock
CS = 24    # Pino 18 - Chip Select

# Configuração inicial
GPIO.setmode(GPIO.BOARD)

# Configura as portas GPIO como saídas ou entradas conforme necessário
GPIO.setup(MISO, GPIO.IN)
GPIO.setup(MOSI, GPIO.OUT)
GPIO.setup(SCLK, GPIO.OUT)
GPIO.setup(CS, GPIO.OUT)

# Configuração do SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Certifique-se de que as portas estão corretas (SPI0, dispositivo 0)
spi.max_speed_hz = 1000000  # Taxa de comunicação
config_byte = 0x20asdasdd

# Função para ler dados do ADS1210
def read_ads1210(channel):
    # Comunicar-se com o ADS1210 usando as portas GPIO configuradas
    GPIO.output(CS, GPIO.LOW)  # Ativar o Chip Select
    adc_data = spi.xfer2([config_byte | ((channel & 0x07) << 4), 0, 0])
    GPIO.output(CS, GPIO.HIGH)  # Desativar o Chip Select
    raw_value = (adc_data[1] << 8) | adc_data[2]
    return raw_value

try:
    while True:
        time.sleep(0.1)
        a = read_ads1210(0)
        print("A", a)
        
except KeyboardInterrupt:
    # Lidar com a interrupção do teclado (Ctrl+C)
<<<<<<< HEAD
    pass

#pamonha

print("iahsdsa")
=======
    GPIO.cleanup()  # Limpar as configurações GPIO ao sair


asdasdasdasdas
>>>>>>> 67f40b429fa1351342e22b68be6154d9a7b8550c


!@#WASdaisdia!