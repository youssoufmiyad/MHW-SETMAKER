def elementEmoji(weapon):
    if weapon.elements:
        element = weapon.elements[0]["type"]
    else:
        return""
    match element:
        case "fire":
            return " <:Fire:1192522472151584909>"
        case "water":
            return " <:water:1192522477008588871>"
        case "ice":
            return " <:ice:1192522473418264667>"
        case "thunder":
            return " <:thunder:1192522474877878423>"
        case "dragon":
            return " <:Dragon:1192522469521756265>"
        case "sleep":
            return " <:sleep:1192524799973543997>"
        case "paralysis":
            return " <:paralysis:1192524796500656128>"
        case "poison":
            return " <:poison:1192524798706843738>"
        case _:
            return ""
