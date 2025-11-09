## Introduction
Ce dossier contient des projets qui connecte le rasoberry pico au réseau Wifi.
## Exercice 5 
### Introduction
Cet exercice utilise un servomoteur, un bouton-poussoir et un Raspberry Pi Pico, bien sûr. Le but de l’exercice est de simuler une horloge à l’aide de l’heure réelle, récupérée via le réseau, et d’un servomoteur qui pointera vers la bonne heure en fonction du temps réel.
### Fonctionnalité du code
Le script connecte le Raspberry Pi Pico à un réseau Wi-Fi, synchronise automatiquement l’heure réelle à l’aide du protocole NTP, puis contrôle un servomoteur pour simuler une horloge analogique.

Connexion au Wi-Fi :
Le programme se connecte au réseau sans fil à l’aide des identifiants fournis et affiche l’adresse IP du Pico une fois la connexion établie.

Synchronisation de l’heure :
Une fois connecté, le Pico récupère l’heure exacte via un serveur NTP (Network Time Protocol) afin de toujours afficher l’heure réelle, même sans horloge interne précise.

Contrôle du servomoteur :
Le servomoteur est commandé en fonction de l’heure actuelle. Chaque position de l’aiguille correspond à un angle calculé pour représenter les heures de 12 h à 11 h. Le mouvement du servo varie progressivement selon les minutes pour obtenir une rotation fluide entre deux heures.

Pour simuler l’horloge, j’ai dessiné une horloge sur du papier où 6 h correspond à 90° et 12 h à 180°, ce qui fait que chaque heure est séparée de 15°. 12 AM est fixé à 0° et 12 PM à 180°.

Le programme comporte deux modes principaux :

Mode 24 h :

- Dans ce mode, on ignore la distinction AM/PM.

- Le servo se déplace de manière linéaire pour représenter les heures de 12 AM à 12 PM.

- Chaque heure correspond à un angle défini dans le dictionnaire hour_angle_24h.

- Pour l’heure spéciale 11 → 12, le servo descend progressivement de 15° à 0° pendant l’heure 11, puis saute directement à 180° à 12:00. Cela permet de représenter le passage de 11 à 12 sans ambiguïté et sans différencier AM et PM.

Mode 12 PM → 6 PM :

- Ce mode ne couvre que la période de 12 PM à 6 PM.

- Le servo part de 180° à 12 PM et descend progressivement jusqu’à 90° à 6 PM.

- Les heures intermédiaires sont interpolées en fonction des minutes pour un mouvement fluide.

- Si l’heure est en dehors de la plage 12 PM–6 PM, le servo reste fixe à 180°.

Ces modes permettent de représenter l’heure de manière réaliste sur le servo tout en simulant l’aiguille d’une horloge classique.
Gestion du bouton-poussoir :
Le bouton permet d’interagir avec le programme :

- Un clic simple modifie le décalage horaire (UTC,UTC+1,UTC+2,UTC-5).

- Un double clic active ou désactive le mode 24 heures.

Affichage et suivi :
Le script affiche en continu l’heure locale, le fuseau horaire sélectionné et l’angle du servomoteur correspondant. Il fonctionne en boucle, tout en vérifiant en temps réel les interactions avec le bouton.

