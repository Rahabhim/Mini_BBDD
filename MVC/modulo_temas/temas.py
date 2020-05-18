import shelve
import random


def EleccionTema(var_temas):
    with shelve.open("MVC/modulo_temas/OpcionTemas") as db:
        db["tema1"] = "#8B0000"
        db["tema2"] = "#00BFFF"

        if var_temas.get() == 1:
            return db["tema1"]

        elif var_temas.get() == 2:
            return db["tema2"]

        elif var_temas.get() == 3:
            return RandomHex()


def RandomHex():
    opciones = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    r1 =random.choice(opciones)
    r2 =random.choice(opciones)
    r3 =random.choice(opciones)
    r4 =random.choice(opciones)
    r5 =random.choice(opciones)
    r6 =random.choice(opciones)
    color_hex = '#' + r1 + r2 + r3 + r4 +r5 + r6
    return color_hex
