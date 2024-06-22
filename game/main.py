import random


def opcionCP(na):
    juego = ("piedra", "papel", "tijera")
    elije = f"{na}, por favor elige entre piedra, papel o tijera=> "
    aleat = random.choice(juego)
    jugad = input(elije)
    jugad = jugad.lower()
    return jugad, aleat


def comparacionInv(a1, b2):
    comparacion3 = a1 == b2
    comparacion2 = (
        (a1 == "piedra" and b2 == "tijera")
        or (a1 == "papel" and b2 == "piedra")
        or (a1 == "tijera" and b2 == "papel")
    )
    comparacion1 = (
        (a1 == "piedra" and b2 == "papel")
        or (a1 == "papel" and b2 == "tijera")
        or (a1 == "tijera" and b2 == "piedra")
    )
    return comparacion1, comparacion2, comparacion3


def mensajeContra(ju, al):
    mensajito = f"\nElejiste {ju} contra {al}\n"
    return mensajito


def chetWiner(gan, per):
    vitde = f"\nNumero de victorias {gan} \nNumero de derrotas {per}"
    if per > gan:
        print(f"\nPerdiste las partida, lo siento {vitde}")
    elif per < gan:
        print(f"\n¡¡¡Ganaste!!! Felicidades {vitde}")
    else:
        print(f"\n¡¡¡Empataste!!! {vitde}")


def chetPartida(pe, per, ga, gan, jugd, alert):
    mensajero = mensajeContra(jugd, alert)
    gar, ped, ep = comparacionInv(jugd, alert)
    if ep == True:
        print("empataste", mensajero)
    elif gar == True:
        pe += 1
        per += 1
        print("Lo siento, Perdiste", mensajero)
    elif ped == True:
        ga += 1
        gan += 1
        print("¡¡¡GANASTE!!!", mensajero)
    else:
        print("\nNo ingresaste ninguna opcion valida\n")
    return ga, gan, pe, per


def run_game():
    proceder = "si"
    ganar = 0
    perder = 0
    print("\n¡¡¡Bienvenido al Juego  piedra, papel o tiejera!!!\n")
    name = input("Insera el nombre de usuario=> ")
    name = name.title()
    while proceder == "si":
        perde = 0
        gana = 0
        while perde < 2 and gana < 2:
            jugador1, aleatorio = opcionCP(name)
            print("\n", "*" * 9, "\n  ROUND", (gana + perde) + 1, "\n", "*" * 9, "\n")
            gana, ganar, perde, perder = chetPartida(
                perde, perder, gana, ganar, jugador1, aleatorio
            )
        anuncio = '¿Deseas continuar? ingresa la palabra \n "si" o "no"\n=>'
        proceder = input(anuncio)
        proceder = proceder.lower()
    chetWiner(ganar, perder)


run_game()
