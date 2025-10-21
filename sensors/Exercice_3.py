from machine import Pin, I2C, ADC, PWM
from time import sleep
import dht
from lcd1602 import LCD1602

# Initialisation DHT11
sensor = dht.DHT11(Pin(20))

# Initialisation potentiomètre sur A0
pot = ADC(0)  # A0

# Initialisation LED sur D18
led = Pin(18, Pin.OUT)

# Initialisation buzzer PWM sur A1 (GP1)
buzzer = PWM(Pin(1))
buzzer.duty_u16(0)  # buzzer éteint

# Initialisation LCD
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
lcd = LCD1602(i2c, 2, 16)
lcd.clear()

# Fonction pour mapper valeur ADC sur plage 15–33
def map_temp(adc_value):
    return 15 + (adc_value / 65535) * (33 - 15)#

# Fréquence du buzzer
FREQ_BUZZER = 2000 

while True:
    try:
        # Lecture température DHT
        sensor.measure()
        temp = sensor.temperature()

        # Lecture potentiomètre et conversion en température cible
        pot_val = pot.read_u16()
        temp_set = int(map_temp(pot_val))

        # Affichage sur LCD
        lcd.setCursor(0, 0)
        lcd.print(f"Set:{temp_set:2d}C    ")  # ligne du haut
        lcd.setCursor(0, 1)
        lcd.print(f"Ambient:{temp:2d}C  ")    # ligne du bas

        # Console
        print(f"Temp: {temp}C | Target: {temp_set}C")

        # Gestion LED et buzzer selon écart
        if temp > temp_set + 3:
            # Clignotement rapide (1 Hz) + buzzer
            led.value(1)
            buzzer.freq(FREQ_BUZZER)
            buzzer.duty_u16(32768)  # 50% duty cycle
            sleep(0.5)
            led.value(0)
            buzzer.duty_u16(0)  # buzzer off
            sleep(0.5)
        elif temp > temp_set:
            # Clignotement lent (0,5 Hz) sans buzzer
            led.value(1)
            buzzer.duty_u16(0)
            sleep(1)
            led.value(0)
            sleep(1)
        else:
            # Temp OK → LED et buzzer éteints
            led.value(0)
            buzzer.duty_u16(0)
            sleep(1)

    except OSError:
        print("Failed to read sensor.")
        sleep(1)
