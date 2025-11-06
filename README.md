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
J'ai également utilisé une extension de carte qui facilite la connexion des différents modules au Raspberry Pi Pico.
L'extension utilisée est le Grove Shield for Pi Pico : https://www.seeedstudio.com/Grove-Shield-for-Pi-Pico-v1-0-p-4846.html

Le kit de développement que j'ai utilisé tout au long de ces travaux est le Grove Starter Kit for Raspberry Pi Pico : https://www.seeedstudio.com/Grove-Starter-Kit-for-Raspberry-Pi-Pico-p-4851.html

Tous les composants utilisés dans ces différents travaux sont inclus dans ce kit.
### Librairies
Pour certains codes, j’ai dû implémenter certaines librairies qui se trouvent sur ce dépôt : https://github.com/TinkerGen/Pico-micropython.
Pour que cela fonctionne, il faut ouvrir les différents fichiers dans l’environnement de travail MicroPython, puis faire un clic droit sur chaque fichier et sélectionner “Update file to Pico”.

## Micropython
Pour programmer le Raspberry Pi Pico W, j'ai utilisé le langage MicroPython, une version allégée de Python spécialement conçue pour les microcontrôleurs. MicroPython a été développé par Damien P. George en 2013 dans le but de rendre la programmation embarquée plus accessible, tout en conservant la simplicité et la puissance du langage Python.


### Visual Studio
Pour télécharger les différents codes sur le Raspberry Pi Pico, j'ai utilisé le logiciel Visual Studio Code. Pour accomplir ceci, j'ai dû télécharger une extension appelée MicroPico.
L’extension MicroPico facilite la connexion entre le Pico et l’éditeur, permettant de flasher facilement le firmware MicroPython, de transférer les fichiers (scripts .py) vers la carte. Elle automatise plusieurs étapes du processus de développement, ce qui simplifie grandement le travail avec MicroPython, surtout lorsqu'on débute avec les microcontrôleurs.

<img width="256" height="256" alt="image" src="https://github.com/user-attachments/assets/df7c7b63-1ead-417d-b8d8-e82640a81637" />



