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
    RRLR=f"Voici une liste des armes et de leurs fonctionnement : \nLa {GREATSWORD} est une arme de CAC terriblement efficace, elle inflige énormement de dégat mais elle requière un maniement délicat ceux qui rend très lent l'utilisateur. Pour les joueurs patient et précis.\nLa {LANCE} est une arme de CAC aux dégats décent. Elle comporte un bouclier qui permet aux joueurs de résister aux assauts. Pour les joueurs tank.\nLe {HEAVY_BOWGUN} est une arme à distance. Elle offre une puissance de feu conséquente contre une cadence de tir réduite et une mobilité réstreinte. Pour les joueurs assistant.\nLa {HUNTING_HORN} est l'arme de soutien par excellence. Elle offre la possibilité de renforcer les stats de vos cooéquipier contre des dégats médiocre. Pour les joueurs assistant.\nLa {SWORD_AND_SHIELD} est l'arme de base recomandée au débutant. Capacité offensive décente et bonne mobilité. Pour les joueurs nerveux.\nLes {DUAL_BLADES} sont comme les {SWORD_AND_SHIELD} en + rapide mais + risqué. Pour les joueurs nerveux.\nLe {BOW} est une arme à distance. Elle offre une puissance de feu décente pour une mobilité correcte. Pour les joueurs assistant.\nLe {LIGHT_BOWGUN} est la version - puissante et + rapide du {HEAVY_BOWGUN}. Pour les joueurs assistant.\nLa {LONGSWORD} est la version - puissante et + rapide de la {GREATSWORD}. Pour les joueurs agressif.\nLe {HAMMER} est une arme de CAC, elle inflige énormement de dégat mais elle souffre d'une portée restreinte et d'une mobilité déplorable. Pour les joueurs agressifs/assistant.\nLa {GUNLANCE} équivaut à la {LANCE} avec + d'artifice. Pour les jouers tank.\nLes {CHARGE_BLADE}, {SWITCH_AXE}, and{INSECT_GLAIVE} sont des armes polyvalentes mais compliqué à maitriser. Recommandé aux experts."
    RLRL=f"Voici une liste des armes et de leurs fonctionnement : \nLa {GREATSWORD} est une arme de CAC terriblement efficace, elle inflige énormement de dégat mais elle requière un maniement délicat ceux qui rend très lent l'utilisateur. Pour les joueurs patient et précis.\nLa {LANCE} est une arme de CAC aux dégats décent. Elle comporte un bouclier qui permet aux joueurs de résister aux assauts. Pour les joueurs tank.\nLe {HEAVY_BOWGUN} est une arme à distance. Elle offre une puissance de feu conséquente contre une cadence de tir réduite et une mobilité réstreinte. Pour les joueurs assistant.\nLa {HUNTING_HORN} est l'arme de soutien par excellence. Elle offre la possibilité de renforcer les stats de vos cooéquipier contre des dégats médiocre. Pour les joueurs assistant.\nLa {SWORD_AND_SHIELD} est l'arme de base recomandée au débutant. Capacité offensive décente et bonne mobilité. Pour les joueurs nerveux.\nLes {DUAL_BLADES} sont comme les {SWORD_AND_SHIELD} en + rapide mais + risqué. Pour les joueurs nerveux.\nLe {BOW} est une arme à distance. Elle offre une puissance de feu décente pour une mobilité correcte. Pour les joueurs assistant.\nLe {LIGHT_BOWGUN} est la version - puissante et + rapide du {HEAVY_BOWGUN}. Pour les joueurs assistant.\nLa {LONGSWORD} est la version - puissante et + rapide de la {GREATSWORD}. Pour les joueurs agressif.\nLe {HAMMER} est une arme de CAC, elle inflige énormement de dégat mais elle souffre d'une portée restreinte et d'une mobilité déplorable. Pour les joueurs agressifs/assistant.\nLa {GUNLANCE} équivaut à la {LANCE} avec + d'artifice. Pour les jouers tank.\nLes {CHARGE_BLADE}, {SWITCH_AXE}, and{INSECT_GLAIVE} sont des armes polyvalentes mais compliqué à maitriser. Recommandé aux experts."

    L="Voici une liste des commandes suivi de leur fonction:\n!hist : permet de consulter l'historique de commande\n!cls : permet de vider l'historique\n!help : affiche cette discussion"

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
