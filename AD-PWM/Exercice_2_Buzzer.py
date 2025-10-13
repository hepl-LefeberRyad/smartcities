from machine import Pin, PWM, ADC  # Importer les classes pour gérer les broches, le PWM et l'ADC
import utime                       # Importer la bibliotheque pour gérer les delais 


# --- Configuration du materiel ---
buzzer = PWM(Pin(27))          # Buzzer connecte sur le pin 27 (PWM)
ROTARY_ANGLE_SENSOR = ADC(0)   # Potentiometre sur ADC0 pour ajuster le volume
led = Pin(18, Pin.OUT)         # LED connectee sur le pin 18
switch = Pin(16, Pin.IN, Pin.PULL_UP)  # Bouton pour changer de melodie

# --- Variables globales ---
current_melody = 0     # 0 = Mario, 1 = Imperial March
interrupt_flag = False # Drapeau pour interrompre une melodie en cours

# --- Dictionnaires de notes ---
mario_notes = {  
    'E7': 2637, 'C7': 2093, 'G7': 3136, 'G6': 1568,
    'A6': 1760, 'B6': 1976, 'F7': 2794, 'D7': 2349,
    'E6': 1319, 'A7': 3520, 'R': 0 
}

imperial_notes = {  
    'A4': 440, 'A5': 880, 'F4': 349, 'F5': 698,
    'C5': 523, 'C6': 1047, 'E5': 659, 'D5': 587,
    'D6': 1175, 'R': 0
}

# --- Melodies ---
mario_melody = [  
    ('E7', 0.125), ('E7', 0.125), ('R', 0.125), ('E7', 0.125),
    ('R', 0.125), ('C7', 0.125), ('E7', 0.125), ('R', 0.125),
    ('G7', 0.125), ('R', 0.375), ('G6', 0.125), ('R', 0.375),
    ('C7', 0.125), ('R', 0.25), ('G6', 0.125), ('R', 0.25),
    ('E6', 0.125), ('A6', 0.125), ('B6', 0.125), ('A6', 0.125),
    ('G6', 0.083), ('E7', 0.083), ('G7', 0.083), ('A7', 0.125),
    ('F7', 0.125), ('G7', 0.125), ('R', 0.125), ('E7', 0.125),
    ('C7', 0.125), ('D7', 0.125), ('B6', 0.125)
]

imperial_melody = [  
    ('A4', 0.5), ('A4', 0.5), ('F4', 0.25), ('C5', 0.25),
    ('A4', 0.5), ('F4', 0.25), ('C5', 0.25), ('A4', 1.0),
    ('E5', 0.5), ('E5', 0.5), ('E5', 0.5), ('F5', 0.25),
    ('C6', 0.25), ('A5', 0.5), ('F5', 0.25), ('C6', 0.25), ('A5', 1.0),
    ('A4', 0.5), ('A4', 0.5), ('A4', 0.5), ('F4', 0.25),
    ('C5', 0.25), ('A4', 0.5), ('F4', 0.25), ('C5', 0.25), ('A4', 1.0)
]

tempo = 1  # Variable de temps pour gerer la vitesse de la melodie

# --- Fonction pour gerer le bouton ---
def switch_melody(pin):
    global current_melody, interrupt_flag
    current_melody = 1 - current_melody  # Alterne entre Mario et Imperial March
    interrupt_flag = True
    print("Melodie changee :", "Imperial March" if current_melody else "Mario")

# Configuration de l'interruption sur le bouton
switch.irq(trigger=Pin.IRQ_FALLING, handler=switch_melody)

# --- Fonction pour jouer une note ---
def play_tone(note, duration, notes_dict):
    global interrupt_flag
    if interrupt_flag:  # Interrompt si le bouton est presse
        return

    freq = notes_dict.get(note, 0)             # Recupere la frequence de la note
    pot_value = ROTARY_ANGLE_SENSOR.read_u16() # Lecture du potentiometre pour le volume
    volume = int(pot_value / 2)                # Ajuste le PWM pour le volume

    if freq == 0:  # Pause
        buzzer.duty_u16(0)
        led.value(0)
        utime.sleep(duration)
        return

    buzzer.freq(freq)        # Reglage de la frequence du buzzer
    buzzer.duty_u16(volume)  # Reglage du volume
    led.value(1)             # Allume la LED pendant la note
    utime.sleep(duration)    # Joue la note pendant la duree
    led.value(0)             # Eteint la LED
    buzzer.duty_u16(0)       # Coupe le son
    utime.sleep(0.01)        # Petite pause entre les notes

# --- Boucle principale ---
while True:
    interrupt_flag = False  # Reinitialisation du drapeau
    melody = mario_melody if current_melody == 0 else imperial_melody
    notes = mario_notes if current_melody == 0 else imperial_notes

    # Lecture de chaque note
    for note, length in melody:
        if interrupt_flag:  # Interruption si le bouton est presse
            break
        play_tone(note, length * tempo, notes)
