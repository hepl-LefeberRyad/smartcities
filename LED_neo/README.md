## Exercice 4
### Introduction
Cet exercice permet de contrôler une LED RGB qui change de couleur au rythme de la musique. Le script utilise un microphone pour détecter les battements et peut calculer le BPM de la musique et enregistrer la moyenne dans un fichier texte sur le raspberry pico.
### Fonctionalité du code
Le script lit en continu les données du microphone et contrôle une LED RGB en fonction des battements détectés :

Battement détecté :

- La couleur de la LED RGB change de manière aléatoire à chaque battement.

- Le temps entre deux battements est mesuré pour calculer le BPM instantané.

Calcul du BPM moyen :

- Toutes les 60 secondes, le script calcule la moyenne des BPM détectés pendant cette période.

- La valeur moyenne est enregistrée dans le fichier bpm_log.txt sur le Raspberry Pi Pico W.

Premier battement :

- Si c’est le premier battement détecté, seul un message est affiché et aucun BPM n’est calculé.

Sécurité et gestion des fichiers :

- Le script vérifie que la liste de BPM n’est pas vide avant d’écrire dans le fichier.

- Les erreurs lors de l’écriture dans le fichier sont capturées et affichées.

