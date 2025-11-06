from ws2812 import WS2812
from machine import Pin, ADC
from utime import sleep, ticks_ms, ticks_diff
import urandom

# --- Initialisation ---
led = WS2812(18, 1)      # LED RGB sur GPIO 18
mic = ADC(1)             # Micro analogique sur ADC1

# --- Parametres ---
seuil = 120              # seuil de detection
delai_min = 150          # delai minimum entre deux battements (ms)
temps_dernier_battement = 0

# --- Variables pour le calcul du BPM ---
bpm_list = []            # liste des BPM detectes pendant la minute
temps_dernier_fichier = ticks_ms()  # pour suivre quand on enregistre dans le fichier

# --- Fonctions utilitaires ---
def couleur_aleatoire():
    """Renvoie une couleur RGB aleatoire."""
    return (urandom.getrandbits(8), urandom.getrandbits(8), urandom.getrandbits(8))

def ecrire_bpm_moyen(bpm_moyen):
    """Ecrit le BPM moyen dans un fichier texte."""
    try:
        with open("bpm_log.txt", "a") as f:
            f.write("BPM moyen : {:.2f}\n".format(bpm_moyen))
        print("BPM moyen ecrit dans le fichier :", bpm_moyen)
    except Exception as e:
        print("Erreur lors de l ecriture :", e)

# --- Boucle principale ---
print("Demarrage de la detection sonore et du calcul BPM...")

while True:
    valeur = mic.read_u16() / 256  # Normalisation sur 8 bits (0-255)
    maintenant = ticks_ms()

    # --- Detection de battement ---
    if valeur > seuil and ticks_diff(maintenant, temps_dernier_battement) > delai_min:
        # Calcul du BPM a partir du temps ecoule depuis le dernier battement
        if temps_dernier_battement != 0:
            intervalle_ms = ticks_diff(maintenant, temps_dernier_battement)
            bpm = 60000 / intervalle_ms  # 60000 ms = 1 minute
            bpm_list.append(bpm)
            print("Battement detecte ! BPM instantane :", round(bpm, 2))
        else:
            print("Premier battement detecte.")

        # Animation LED
        led.pixels_fill(couleur_aleatoire())
        led.pixels_show()
        temps_dernier_battement = maintenant

    # --- Enregistrement toutes les 60 secondes ---
    if ticks_diff(maintenant, temps_dernier_fichier) >= 60000:
        if len(bpm_list) > 0:
            bpm_moyen = sum(bpm_list) / len(bpm_list)
            ecrire_bpm_moyen(bpm_moyen)
            bpm_list.clear()
        else:
            print("Aucun battement detecte cette minute.")
        temps_dernier_fichier = maintenant

    
