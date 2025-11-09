import network
import ntptime
from machine import Pin, PWM
from utime import sleep, localtime, ticks_ms

# --- Configuration Wi-Fi ---
ssid = 'ssid'      # Nom du reseau Wi-Fi
password = 'code'  # Mot de passe Wi-Fi

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
print("Connexion au Wi-Fi...")
while not wlan.isconnected():  # Attendre la connexion
    sleep(1)
print("Connecte ! IP :", wlan.ifconfig()[0])

# --- Synchronisation de l'heure via NTP ---
ntptime.settime()
print("Heure synchronisee avec NTP")

# --- Configuration du servo ---
servo_pin = Pin(20)
servo = PWM(servo_pin)
servo.freq(50)  # Frequence standard pour servo (50Hz)

def angle_to_duty(angle):
    # Convertir un angle (0-180) en duty cycle pour PWM
    min_duty = 1545
    max_duty = 6700
    return int(min_duty + (angle / 180.0) * (max_duty - min_duty))

# --- Configuration du bouton ---
BUTTON = Pin(16, Pin.IN, Pin.PULL_DOWN)

# --- Fuseaux horaires et mode d'affichage ---
timezones = [0, 1, 2, -5]  # Liste des offsets UTC possibles
tz_index = 1                # Index du fuseau courant
UTC_OFFSET = timezones[tz_index]
mode_24h = False            # False = 12PM->6PM, True = mode 24h

# --- Detection double click ---
last_press_time = 0
double_click_delay = 500  # Delai max pour un double click en ms
single_click_pending = False

# --- Angles du servo pour le mode 24h ---
hour_angle_24h = {
    12: 180, 1: 165, 2: 150, 3: 135, 4: 120, 5: 105,
    6: 90, 7: 75, 8: 60, 9: 45, 10: 30, 11: 15, 0: 0
}

# --- Fonction pour calculer l'angle du servo selon l'heure ---
def compute_servo_angle(h, m, mode_24h):
    if mode_24h:
        # Mode 24h: ignore AM/PM, heures de 0 a 12
        h12 = h % 12
        # Cas special: transition de 11 -> 12
        if h12 == 11:
            base_angle = hour_angle_24h[11]  # 15 degres pour 11h
            next_angle = 0                   # objectif 0 degres pour 12h
            angle = base_angle + (next_angle - base_angle) * (m / 60)
            # Sauter a 180 degres exactement a 12:00
            if h % 12 == 0 and m == 0:
                return 180
            return angle
        else:
            # Interpolation normale pour autres heures
            next_h = (h12 + 1) % 12
            base_angle = hour_angle_24h[h12 if h12 != 0 else 12]
            next_angle = hour_angle_24h[next_h if next_h != 0 else 12]
            return base_angle + (next_angle - base_angle) * (m / 60)
    else:
        # Mode 12PM -> 6PM
        if 12 <= h <= 18:
            h12 = h - 12  # 12PM -> 0, 6PM -> 6
            # Interpolation lineaire entre 180 degres a 12PM et 90 degres a 6PM
            return 180 - ((h12 + m / 60) * 15)
        else:
            # En dehors de 12PM->6PM, le servo reste fixe a 180 degres
            return 180

# --- Boucle principale ---
while True:
    t = localtime()
    h = (t[3] + UTC_OFFSET) % 24  # Heure locale avec fuseau
    m = t[4]                      # Minutes
    s = t[5]                      # Secondes

    # --- Gestion du bouton ---
    if BUTTON.value() == 1:
        now = ticks_ms()
        # Detection double click
        if single_click_pending and (now - last_press_time <= double_click_delay):
            mode_24h = not mode_24h
            print("Double click detecte -> mode 24h:", mode_24h)
            single_click_pending = False
            sleep(0.3)
        else:
            # Premier clic, attente du second
            single_click_pending = True
            last_press_time = now
            while BUTTON.value() == 1:
                sleep(0.01)
            sleep(0.05)

    # --- Detection clic simple pour changer fuseau ---
    if single_click_pending and (ticks_ms() - last_press_time > double_click_delay):
        tz_index = (tz_index + 1) % len(timezones)
        UTC_OFFSET = timezones[tz_index]
        print("Single click detecte -> fuseau change. UTC offset:", UTC_OFFSET)
        single_click_pending = False

    # --- Calcul de l'angle du servo selon l'heure et le mode ---
    hour_angle = compute_servo_angle(h, m, mode_24h)

    # --- Deplacement du servo ---
    servo.duty_u16(angle_to_duty(hour_angle))

    # --- Debug: affichage heure et angle ---
    print("Heure actuelle: {:02d}:{:02d}:{:02d} | Angle servo: {:.2f}".format(h, m, s, hour_angle))
    sleep(0.02)
