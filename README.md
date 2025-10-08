# Projet Smartcities

## Introduction
Dans ce dépôt Github je vais documenter le travail effectuer au long du cours de Projet SmartcitiesIOT.
Le dépôt contient plusieurs dossiers: 
- GPIO : LED simple,Bouton poussoire
- AD-PWM : lecture du potentiomètre, PWM (LED, musique, servo)
- LCD : documentation des fonctions de la librairie, affichage de la valeur du potentiomètre
- LED_NEO : utilisation des LEDs néopixel, documentation des fonctions de la librairie, arc-en-ciel
- network : accès réseau avec le RPi Pico.
- sensors : Température et humidité, luminosité, PIR
## Raspberry Pico W
Le Raspberry Pi Pico W est une carte microcontrôleur basée sur la puce RP2040. Elle est équipée d’un processeur dual-core ARM Cortex-M0+ cadencé à 133 MHz, de 264 Ko de RAM, et ajoute la connectivité Wi-Fi par rapport au modèle Pico original.
C’est une carte compacte, peu coûteuse, idéale pour les projets IoT et embarqués.
### Pinout du Raspberry Pi Pico
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/eb88469c-6eab-4b56-b656-c31beb64dd05" />
### Datasheet Raspberry Pico W
https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf
### Grove Shield for Pi Pico
J'ai également utilisé une extension de board qui facilite la connexion des différents modules sur le raspberry pico. 
L'extension utilisée est le Grove Shield for Pi Pico : https://www.seeedstudio.com/Grove-Shield-for-Pi-Pico-v1-0-p-4846.html

## Micropython
Pour programmer le Raspberry Pi Pico W, j'ai utilisé le langage MicroPython, une version allégée de Python spécialement conçue pour les microcontrôleurs. MicroPython a été développé par Damien P. George en 2013 dans le but de rendre la programmation embarquée plus accessible, tout en conservant la simplicité et la puissance du langage Python.

### Visual Studio
<img width="474" height="104" alt="image" src="https://github.com/user-attachments/assets/4e928384-ecb7-4bf4-ba47-d6fef911ac6a" />

Pour télécharger les différents codes sur le Raspberry Pi Pico, j'utilise Visual Studio Code. Pour accomplir ceci, j'ai dû télécharger une extension appelée MicroPico.
L’extension MicroPico facilite la connexion entre le Pico et l’éditeur, permettant de flasher facilement le firmware MicroPython, de transférer les fichiers (scripts .py) vers la carte. Elle automatise plusieurs étapes du processus de développement, ce qui simplifie grandement le travail avec MicroPython, surtout lorsqu'on débute avec les microcontrôleurs.

<img width="256" height="256" alt="image" src="https://github.com/user-attachments/assets/df7c7b63-1ead-417d-b8d8-e82640a81637" />



