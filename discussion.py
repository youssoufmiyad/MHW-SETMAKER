from API import MONSTERS
from assets.emoji import *
monstre = ""
monsterWeakness=""
nb=0
for m in MONSTERS:
    if nb != 24:
        for weakness in m.weaknesses:
            if weakness["stars"] == 3:
                monsterWeakness = weakness["element"]
                break
        monstre += f"Nom: {m.name} espèce: {m.species}. habitat: {m.locations[0]["name"]} faiblesse: {monsterWeakness}\n\n"
        nb+=1
    else:
        break
class Messages:
    FIRST_MESSAGE="Bonjour , je suis un bot ayant pour but de t'aider à composer ton set dans le jeu MONSTER HUNTER WORLD.\nAs-tu des questions sur mes commandes ⌨️ ou sur mon fonctionement :regional_indicator_f: ?\nSaisissez la commande !exit pour quitter la conversation à tout moment"
    R="Connait tu la licence Monster Hunter ?"
    RL="Comme le nom l'indique, notre but est de chasser des monstres. Chacune des créatures a des forces et des faiblesse (physique et élémentaire). Pour se faire, nous avons à disposition plusieurs type d'armes ce qui nous permet de jouer selon nos affinité (de manière plutot agressive, à distance, avec ruse, etc...).\nJ'ai pour mission de t'aider à découvrir quelles armes te correspondent le plus et quelles armures te serait le plus utile. Je vais te poser des questions afin de mieux cerner ta personalité et tes besoins et à partir des réponses je te proposerai un set adéquat que tu pourras enregistrer. As-tu besoin de plus d'info ?"
    RR="J'ai pour mission de t'aider à découvrir quelles armes te correspondent le plus et quelles armures te serait le plus utile. Je vais te poser des questions afin de mieux cerner ta personalité et tes besoins et à partir des réponses je te proposerai un set adéquat que tu pourras enregistrer. As-tu besoin de plus d'info ?"
    RRR="Veux tu parler des monstres 🐉 ou des armes <:greatsword:1191087208581574726> ?"
    RLR="Veux tu parler des monstres 🐉 ou des armes <:greatsword:1191087208581574726> ?"
    RRRR=f"{monstre}"
    RLRR=f"{monstre}"
    RRLR=f"Voici une liste des armes et de leurs affinités : \n\n{GREATSWORD} : type : CAC, dégats : ⭐⭐⭐, difficulté : ⭐⭐⭐, mobilité : ⭐. Pour les joueurs patient et précis.\n\n{LANCE} : type : CAC dégats : ⭐⭐, difficulté: ⭐, mobilité : ⭐. Pour les joueurs tank.\n\n{HEAVY_BOWGUN} : type : arme à distance dégats : ⭐⭐ difficulté : ⭐⭐, mobilité : ⭐. Pour les joueurs assistant.\n\n{HUNTING_HORN} : type : CAC/soutien, dégats : ⭐ difficulté : ⭐⭐⭐ mobilité : ⭐⭐. Pour les joueurs assistant.\n\n{SWORD_AND_SHIELD} : type : CAC dégats : ⭐ difficulté : ⭐ mobilité : ⭐⭐⭐.Pour les joueurs nerveux.\n\n{DUAL_BLADES} : type : CAC dégats : ⭐⭐ difficulté : ⭐⭐ mobilité : ⭐⭐⭐.Pour les joueurs nerveux.\n\n{BOW} : type : arme à distance. dégats : ⭐⭐ difficulté : ⭐, mobilité : ⭐⭐. Pour les joueurs assistant.\n\n {LIGHT_BOWGUN} : type : arme à distance, dégats : ⭐ difficulté : ⭐⭐, mobilité : ⭐⭐. Pour les joueurs assistant.\n\n{LONGSWORD} : type : CAC, dégats : ⭐⭐⭐ difficulté : ⭐⭐, mobilité : ⭐⭐. Pour les joueurs agressif.\n\n{HAMMER} : type : CAC, dégats : ⭐⭐⭐ difficulté : ⭐, mobilité : ⭐. Pour les joueurs agressifs/assistant.\n\n{GUNLANCE} : type : CAC dégats : ⭐⭐, difficulté: ⭐, mobilité : ⭐. Pour les joueurs tank.\n\n{CHARGE_BLADE} : type : CAC , dégats : ⭐⭐, difficulté: ⭐⭐⭐, mobilité : ⭐⭐. Pour les joueurs experts.\n\n{SWITCH_AXE} : type : CAC , dégats : ⭐⭐, difficulté: ⭐⭐⭐, mobilité : ⭐⭐. Pour les joueurs experts.\n\n{INSECT_GLAIVE} : type : CAC/distance , dégats : ⭐⭐⭐, difficulté: ⭐⭐⭐, mobilité : ⭐⭐⭐. Pour les joueurs experts."
    RLRL=f"Voici une liste des armes et de leurs affinités : \n\n{GREATSWORD} : type : CAC, dégats : ⭐⭐⭐, difficulté : ⭐⭐⭐, mobilité : ⭐. Pour les joueurs patient et précis.\n\n{LANCE} : type : CAC dégats : ⭐⭐, difficulté: ⭐, mobilité : ⭐. Pour les joueurs tank.\n\n{HEAVY_BOWGUN} : type : arme à distance dégats : ⭐⭐ difficulté : ⭐⭐, mobilité : ⭐. Pour les joueurs assistant.\n\n{HUNTING_HORN} : type : CAC/soutien, dégats : ⭐ difficulté : ⭐⭐⭐ mobilité : ⭐⭐. Pour les joueurs assistant.\n\n{SWORD_AND_SHIELD} : type : CAC dégats : ⭐ difficulté : ⭐ mobilité : ⭐⭐⭐.Pour les joueurs nerveux.\n\n{DUAL_BLADES} : type : CAC dégats : ⭐⭐ difficulté : ⭐⭐ mobilité : ⭐⭐⭐.Pour les joueurs nerveux.\n\n{BOW} : type : arme à distance. dégats : ⭐⭐ difficulté : ⭐, mobilité : ⭐⭐. Pour les joueurs assistant.\n\n {LIGHT_BOWGUN} : type : arme à distance, dégats : ⭐ difficulté : ⭐⭐, mobilité : ⭐⭐. Pour les joueurs assistant.\n\n{LONGSWORD} : type : CAC, dégats : ⭐⭐⭐ difficulté : ⭐⭐, mobilité : ⭐⭐. Pour les joueurs agressif.\n\n{HAMMER} : type : CAC, dégats : ⭐⭐⭐ difficulté : ⭐, mobilité : ⭐. Pour les joueurs agressifs/assistant.\n\n{GUNLANCE} : type : CAC dégats : ⭐⭐, difficulté: ⭐, mobilité : ⭐. Pour les joueurs tank.\n\n{CHARGE_BLADE} : type : CAC , dégats : ⭐⭐, difficulté: ⭐⭐⭐, mobilité : ⭐⭐. Pour les joueurs experts.\n\n{SWITCH_AXE} : type : CAC , dégats : ⭐⭐, difficulté: ⭐⭐⭐, mobilité : ⭐⭐. Pour les joueurs experts.\n\n{INSECT_GLAIVE} : type : CAC/distance , dégats : ⭐⭐⭐, difficulté: ⭐⭐⭐, mobilité : ⭐⭐⭐. Pour les joueurs experts."

    L="Voici une liste des commandes suivi de leur fonction:\n\n!historique : Permet de consulter l'historique de commande.\n!cls : Vide l'historique.\n!help : Affiche cette discussion.\n!new_set nom_de_l'armure nom_de_l'arme :  Enregistre un nouveau set au nom de l'utilisateurs d'après les informations renseignées.\n!make_set : Enregistre un nouveau set au nom de l'utilisateurs selon ses besoins.\n!get_set numéro_du_set : Renvoi le set choisi par l'utilisateur.\n!get_sets : Renvoi tout les sets enregistrés au nom de l'utilisateur.\n!delete_set numéro_du_set : Supprime un set choisi par l'utilisateur.\n!stat_set numéro_du_set : Montre les statistique du set choisi par l'utilisateur."

from data_structures.arbre import Discusion_tree
Disscussion = Discusion_tree()
Disscussion.add_first_message(Messages.FIRST_MESSAGE)
Disscussion.add_message(Messages.R,"right",Messages.FIRST_MESSAGE)
Disscussion.add_message(Messages.L,"left",Messages.FIRST_MESSAGE)

Disscussion.add_message(Messages.RL,"left",Messages.R)
Disscussion.add_message(Messages.RR,"right",Messages.R)
Disscussion.add_message(Messages.RRR,"right",Messages.RR)
Disscussion.add_message(Messages.RLR,"right",Messages.RL)
Disscussion.add_message(Messages.RRRR,"right",Messages.RRR)
Disscussion.add_message(Messages.RRLR,"left",Messages.RRR)
Disscussion.add_message(Messages.RLRR,"right",Messages.RLR)
Disscussion.add_message(Messages.RLRL,"left",Messages.RLR)
