# Introduction
Ce dossier contient des projets effectués à l'aide des capteurs de Température et humidité, luminosité, PIR.
## Exercice 3
### Introduction
Le but de cet exercice est de concevoir un système d'alarme qui mesure la temperature à partir d'un capteur de température DHT11 et qui déclenche certaines alertes en fonction de la temperature mesurée. La température de déclenchement peut être contrôlé à partir d'un potentiomètre et elle peut varier de 15°C à 35°C.
### Fonctionalité du code
Les valeurs mesurées par le DHT11 et les valeurs qui peuvent variées à partir du potentiomètre sont affichées sur un écran LCD. Selon l’écart entre la température actuelle et la température cible :

- Température > cible + 3 °C : LED clignote rapidement (période 1 s, 0,5 s allumée / 0,5 s éteinte) et buzzer sonne à 2 kHz.

- Température > cible mais ≤ cible + 3 °C : LED clignote lentement (période 2 s, 1 s allumée / 1 s éteinte), buzzer éteint.

- Température ≤ cible : LED et buzzer éteints.
