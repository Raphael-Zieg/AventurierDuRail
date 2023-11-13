# Projet Création automatique de board pour le jeu l'Aventurier du Rail

Le projet consiste à développer des nouvelles planches de jeu pour le jeu l'Aventurier du rail. L'idée est de créer un agent RL qui jouera les parties et qui estimera l'équilibrage du jeu. Un autre module servira à paramétrer le jeu selon un set de villes et de missions.

Le but final est donc de trouver des villes et des missions qui permettront de créer une plache de jeu équilibrée.

## Les constantes du jeu :

* Nombre de couleurs de wagons: 8
* Nombre de cartes de wagon par couleurs : 12
* Nombre de locomotives : 14
* Maximum de routes parallèles : 2
* Les autres règles


## Les hyperparamètres (constantes du jeu choisi par nous) :

* Nombre de joueurs (3 à 6) : Il faudra certainement un nombre élevé pour que les agents se battent entre eux. Car nous n'implémenterons pas la malice des humains (à voir si cette malice pourra être apprise automatiquement)
* Nombre de petites missions à trouver : 50
* Nombre de grandes missions à trouver : 10
* La portée entre les monopoles et les autres villes
* Proportions
* Nombre de villes environ
* Nombre de chemins max par villes
* Maximum de chemins de chaque type

## Les paramètres à estimer :

* Les villes retenues
* La distance entre les villes (équivalentes aux points)
* Les missions

## Conception du projet :

### Cadres de la création de la carte

#### Paramétrisation manuelle

* Créer un set de villes avec les distances réelles
* Créer un set de monopoles qui définira un point central ainsi que toutes les villes admissibles dans le jeu selon la portée définie et qui. Les distances réelles seront alors converti en distance dans le jeu
* Implémenter toutes les règles

#### Modèle de créations des chemins et des missions
* Coloration des chemins : 
    * on regardera les chemins critiques par apprès et on estimera quels chemins doit avoir des locomotives
    * Quels chemins devrait être en double
    * Répartitions équilibrées des couleurs sans juxtapositions
    * Séléction des chemins

* Création des missions :
    * Il faut estimer les paramètres de distribution pour que chaque joueur possède environ les mêmes points à gagner lors de tirage aléatoire
    * Estimer les points de missions selon la difficulté de trajet
        * Définir ce qu'est la difficulté d'un trajet :
            * Longueur
            * concurrence
            * réduction des points si les trajets possibles permettent déjà de gagner des points car longues distances



### Création de l'agent :

Plusieurs agents de RL joueront contre les autres et nous observerons si la partie était sérée:

* Implémenter une intelligence dans les agents :
    * Algorithme de recherche du plus court chemin possible
    * Estimer la faisabilité des missions
    * Estimer le bénéfice de tirer à nouveau des missions

* Système de récompenses : 
    * Les récompeneses seront assez simple c'est tout simplement les scores du jeu obtenu : le modèle devra apprendre le paramètre de l'apprentissage futur


## Liste des prérequis pour créer une board :

* Toutes les couleurs doivent avoir un de chemins ainsi qu'une longueur totale presque égale sauf le gris 

