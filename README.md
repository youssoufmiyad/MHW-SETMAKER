# MHW-SETMAKER

## Fonctionalités de base
:white_check_mark: = opérationel :construction: = en cours :hourglass_flowing_sand: = prévu
- Historique des commandes :white_check_mark:
    - Voir la dernière commande :white_check_mark:
    - Se déplacer dans l'historique (optionnel) :hourglass_flowing_sand:
    - Vider l'historique :white_check_mark:
- Arbre de discussion :white_check_mark:
    - reset :white_check_mark:
    - speak about X :white_check_mark:
- Avancement de la conversation dans hashtable :white_check_mark:
- Stockage des données à l'arret du bot :white_check_mark:

## Commandes
### new_set(armor_name : str, weapon_name : str):
    Enregistre un nouveau set au nom de l'utilisateurs.

    Parametres:
    - armor_name
        Nom du set de l'armure

        Type : str
    - weapon_name
        Nom de l'arme

        Type : str

### make_set():
    Enregistre un nouveau set au nom de l'utilisateurs selon ses besoins.

    
### get_set(number : int):
    Renvoi le set choisi par l'utilisateur.

    Parametres:
    - number
        Numéro du set

        type : int

### get_sets():
    Renvoi tout les sets enregistrés au nom de l'utilisateur.

### delete_set(number : int):
    Supprime un set choisi par l'utilisateur

    Parametres:
    - number
        Numéro du set

        type : int

### stat_set(number : int):
    Montre les statistique du set choisi par l'utilisateur

    Parametres:
    - number
        Numéro du set

        type : int