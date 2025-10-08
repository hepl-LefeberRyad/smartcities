# GPIO
## Introduction
Ce dossier contient les travaux qui ont été effectués à l'aide d'une LED simple ou avec un bouton poussoir.
## Exercice 1 
### Introduction
Pour le premier exercice j'ai dû changer la fréquence de clignotement d'une LED avec chaque impulsion de l'interrupteur. Le bouton poussoire et la LED sont inclus dans un Kit de développment et ils sont facilement connectées au Raspberry à l'aide du Grove Shield décrit dans le README.md du main.
### Fonctionnement du Code
Ce programme permet de contrôler une LED à l’aide d’un bouton poussoir, en alternant entre plusieurs modes de clignotement. À chaque pression sur le bouton, le mode actif change, selon une séquence cyclique de trois états. Le bouton est connecté à une entrée numérique configurée avec une résistance de tirage vers le bas, tandis que la LED est reliée à une sortie numérique.

Lorsque le bouton est pressé, une variable de contrôle est incrémentée afin de passer au mode suivant. Si la variable dépasse la valeur 3, elle revient à 1, permettant de faire tourner les modes en boucle. Chaque mode correspond à un comportement spécifique de la LED :

- En mode 1, la LED clignote lentement, avec un temps d’allumage et d’extinction d’ une seconde.

- En mode 2, la LED clignote plus rapidement, avec des cycles de 0,5 seconde.

- En mode 3, la LED reste éteinte en permanence.

Un court délai est ajouté après chaque détection de pression pour éviter les effets de rebond, un phénomène courant avec les boutons mécaniques. De plus, pendant l’exécution des modes 1 et 2, le programme vérifie constamment si le bouton est à nouveau pressé, afin de permettre un changement de mode immédiat sans attendre la fin du cycle en cours.
