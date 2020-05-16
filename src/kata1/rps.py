from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):

    player = player.lower()
    ai = ai.lower()

    if player == ai:
        return 'Empate!'
    
    if player == "piedra":
        if ai == "papel":
            return "Perdiste!"
        return "Ganaste!"
    elif player == "papel":
        if ai == "tijeras":
            return "Perdiste!"
        return "Ganaste!"
    elif player == "tijeras":
        if ai == "piedra":
            return "Perdiste!"
        return "Ganaste!"
    else:
        return "BANANA"

    return "PAPAYA"

# Entry Point
def Game():
    #
    #
    
    #
    #
    
    winner = quienGana(player, ai)

    print(winner)

