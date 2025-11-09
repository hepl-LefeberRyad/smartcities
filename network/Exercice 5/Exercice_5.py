import network
import ntptime
from machine import Pin, PWM
from utime import sleep, localtime, ticks_ms

# --- Configuration du Wi-Fi ---
ssid = 'ssid'  # Nom du reseau Wi-Fi
password = 'code'        # Mot de passe du reseau

# Initialisation de la connexion Wi-Fi en mode station
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connexion au Wi-Fi...")
# On attend tant que le Pico n'est pas connecte au Wi-Fi
while not wlan.isconnected():
    sleep(1)
print("Connecte ! IP :", wlan.ifconfig()[0])  # Affiche l'adresse IP attribuee

# --- Synchronisation de l'heure avec NTP ---
ntptime.settime()  # On recupere l'heure exacte depuis un serveur NTP
print("Heure synchronisee avec NTP")

# --- Configuration du servomoteur ---
servo_pin = Pin(20)         # Pin sur laquelle le servo est branche
servo = PWM(servo_pin)      # Utilisation du PWM pour controler le servo
servo.freq(50)              # Frequence du servo standard 50Hz

# Fonction pour convertir un angle (0-180) en valeur PWM
def angle_to_duty(angle):
    min_duty = 1545          # Valeur correspondant a 0 degres
    max_duty = 6700          # Valeur correspondant a 180 degres
    return int(min_duty + (angle / 180.0) * (max_duty - min_duty))

# --- Configuration du bouton poussoir ---
BUTTON = Pin(16, Pin.IN, Pin.PULL_DOWN)  # Bouton branche sur la pin 16 avec resistance pull-down

# --- Gestion des fuseaux horaires et du mode 24h ---
timezones = [0, 1, 2, -5]  # Liste des decalages UTC disponibles, ajout de UTC+2 pour l'heure d'ete
tz_index = 1                # Index initial du fuseau horaire (UTC+1 au demarrage)
UTC_OFFSET = timezones[tz_index]  # Decalage horaire actuel

mode_24h = False            # Mode 24h desactive par defaut

# --- Mapping des heures sur angles du servo (horloge 12h) ---
hour_angle_12h = {
    12: 180,
    1: 165,
    2: 150,
    3: 135,
    4: 120,
    5: 105,
    6: 90,
    7: 75,
    8: 60,
    9: 45,
    10: 30,
    11: 15,
    0: 0   # Minuit ou midi
}

# --- Variables pour la detection du double-clic ---
last_press_time = 0
double_click_delay = 500  # Delai max pour detecter un double clic en millisecondes
single_click_pending = False

# --- Boucle principale ---
while True:
    # --- Recuperation de l'heure locale avec decalage UTC ---
    t = localtime()
    h = (t[3] + UTC_OFFSET) % 24  # Heure ajustee selon le fuseau horaire
    m = t[4]                       # Minutes
    s = t[5]                       # Secondes

    # --- Detection et gestion du bouton ---
    if BUTTON.value() == 1:
        now = ticks_ms()  # Temps actuel en millisecondes
        # Verification si un double clic a ete effectue
        if single_click_pending and (now - last_press_time <= double_click_delay):
            mode_24h = not mode_24h  # Toggle du mode 24h
            print("Double click detected → 24h mode:", mode_24h)
            single_click_pending = False
            sleep(0.3)  # Debounce pour eviter les rebonds
        else:
            # Premier clic
            single_click_pending = True
            last_press_time = now
            # Attente que le bouton soit relache
            while BUTTON.value() == 1:
                sleep(0.01)
            sleep(0.05)

    # --- Action du clic simple (changer le fuseau horaire) ---
    if single_click_pending and (ticks_ms() - last_press_time > double_click_delay):
        tz_index = (tz_index + 1) % len(timezones)  # Passage au fuseau suivant
        UTC_OFFSET = timezones[tz_index]           # Mise a jour du decalage
        print("Single click detected → Timezone changed. UTC offset:", UTC_OFFSET)
        single_click_pending = False

    # --- Calcul de l'angle du servo selon l'heure ---
    if mode_24h:
        # Mode 24h : interpolation fluide entre les heures
        h12 = h % 12
        next_h = (h12 + 1) % 12
        base_angle = hour_angle_12h[h12 if h12 != 0 else 12]
        next_angle = hour_angle_12h[next_h if next_h != 0 else 12]
        hour_angle = base_angle + (next_angle - base_angle) * (m / 60)
    else:
        # Mode 12h-6h : uniquement de midi a 18h
        if 12 <= h <= 18:
            base_angle = hour_angle_12h[h - 12 + 12]
            next_hour = min(h + 1, 18)
            next_angle = hour_angle_12h[next_hour - 12 + 12]
            hour_angle = base_angle + ((next_angle - base_angle) * (m / 60))
        else:
            # Pour les heures en dehors de midi-18h, servo fixe sur 12h ou 6h
            hour_angle = hour_angle_12h[12] if h < 12 else hour_angle_12h[6]

    # --- Deplacement du servo ---
    servo.duty_u16(angle_to_duty(hour_angle))  # Conversion de l'angle en PWM et envoi au servo

    # --- Affichage de l'heure et de l'angle pour debug ---
    print("Heure actuelle: {:02d}:{:02d}:{:02d} | Angle servo: {:.2f}".format(h, m, s, hour_angle))

    sleep(0.02)  # Petite pause pour detection fiable du bouton

