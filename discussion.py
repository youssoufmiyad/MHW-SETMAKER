FIRST_MESSAGE="Bonjour , je suis un bot ayant pour but de t'aider à composer ton set dans le jeu MONSTER HUNTER WORLD.\nAs-tu des questions sur mes commandes ou sur mon fonctionement ?\nSaisissez la commande !exit pour quitter la conversation à tout moment"
R="Connait tu la licence Monster Hunter ?"
RL="Comme le nom l'indique, notre but est de chasser des monstres. Chacune des créatures a des forces et des faiblesse (physique et élémentaire). Pour se faire, nous avons à disposition plusieurs type d'armes ce qui nous permet de jouer selon nos affinité (de manière plutot agressive, à distance, avec ruse, etc...).\nJ'ai pour mission de t'aider à découvrir quelles armes te correspondent le plus et quelles armures te serait le plus utile. Je vais te poser des questions afin de mieux cerner ta personalité et tes besoins et à partir des réponses je te proposerai un set adéquat que tu pourras enregistrer. As-tu besoin de plus d'info ?"
RR="J'ai pour mission de t'aider à découvrir quelles armes te correspondent le plus et quelles armures te serait le plus utile. Je vais te poser des questions afin de mieux cerner ta personalité et tes besoins et à partir des réponses je te proposerai un set adéquat que tu pourras enregistrer. As-tu besoin de plus d'info ?"
RRR="Veux tu parler des monstres ou des armes ?"
RLR="Veux tu parler des monstres ou des armes ?"
RRRR="Voici une liste des monstres et de leurs faiblesses : "
RLRR="Voici une liste des monstres et de leurs faiblesses : "
RRLR="Voici une liste des armes et de leurs fonctionnement : "
RLRL="Voici une liste des armes et de leurs fonctionnement : "

L="Voici une liste des commandes suivi de leur fonction:\n!hist : permet de consulter l'historique de commande\n!cls : permet de vider l'historique\n!help : affiche cette discussion"

from data_structures.arbre import Discusion_tree
Disscussion = Discusion_tree()
Disscussion.add_first_message(FIRST_MESSAGE)
Disscussion.add_message(R,"right",FIRST_MESSAGE)
Disscussion.add_message(RL,"left",R)
Disscussion.add_message(RR,"right",R)
Disscussion.add_message(RRR,"right",RR)
Disscussion.add_message(RLR,"right",RL)
Disscussion.add_message(RRRR,"right",RRR)
Disscussion.add_message(RRLR,"left",RRR)
Disscussion.add_message(RLRR,"right",RLR)
Disscussion.add_message(RLRL,"left",RLR)
Disscussion.add_message(L,"left",FIRST_MESSAGE)
