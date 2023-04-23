import random

def victories():
    while True:
        max_wins = input("Elige la cantidad de victorias para ganar: ")

        if max_wins.isdigit():
            max_wins = int(max_wins)
            print("*" * 20)
            print("Jugaremos al mejor de", max_wins * 2 - 1)
            break
        else:
            print("*" * 20)
            print("Por favor elige una opción válida")
            continue
    
    return max_wins

def choose_options():
    options = ("piedra", "papel", "tijera")

    user_option = input("Piedra, papel o tijera: ").lower().strip()

    if user_option not in options:
        print("Ingresa una opción válida")
        # continue
        return None, None

    computer_option = random.choice(options)

    print("El jugador eligió =>", user_option)
    print("La computadora eligió =>", computer_option)

    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("¡Empate!")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("¡El jugador ganó!")
            print("Piedra gana a la tijera")
            user_wins += 1
        else:
            print("¡La computadora ganó!")
            print("Papel gana a piedra")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("¡El jugador ganó!")
            print("Papel gana a la piedra")
            user_wins += 1
        else:
            print("¡La computadora ganó!")
            print("Tijera gana a papel")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("¡El jugador ganó!")
            print("Tijera gana a la papel")
            user_wins += 1
        else:
            print("¡La computadora ganó!")
            print("Piedra gana a tijera")
            computer_wins += 1
        
    return user_wins, computer_wins

def check_winner(max_wins, user_wins, computer_wins):
    if user_wins == max_wins:
        print("*" * 20)
        print("¡Felicidades! Has ganado la partida")
        return True
    elif computer_wins == max_wins:
        print("*" * 20)
        print("La computadora ha ganado... mejor suerte la próxima vez")
        return True

def run_game():
    user_wins = 0
    computer_wins = 0
    round = 1

    print("¡Bienvenido a Piedra, Papel o Tijera!")

    max_wins = victories()

    while True:
        print("*" * 20)
        print("RONDA", round)
        print("*" * 20)

        user_option, computer_option = choose_options()

        if not user_option: continue

        round += 1

        print("*" * 20)

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        print("*" * 20)

        print(f"MARCADOR => Jugador: {user_wins} - Computadora: {computer_wins}")
        
        if check_winner(max_wins, user_wins, computer_wins): break
        
run_game()