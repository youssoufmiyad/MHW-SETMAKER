# Fonctions permettant de décider quel branche emprunté dans l'arbre en fonction de la réponse de l'utilisateur


def rightOrLeft(message):
    if message == "oui" or message in "fonctionnement" or message in "monstres" or message in "1":
        return "right"
    elif message == "non" or message in "commandes" or message in "armes" or message in "2":
        return "left"


def rightOrLeftReaction(reaction):
    print("REACT = ", str(reaction))
    match str(reaction):
        case "✅" | "🇫" | "🐉":
            return "right"
        case "❌" | "⌨️" | "<:greatsword:1191087208581574726>":
            return "left"


# Envoi de la réponse du bot (commande !help)


async def send(ctx, disscussion):
    botAnswer = await ctx.channel.send(disscussion.show_message())
    return botAnswer
