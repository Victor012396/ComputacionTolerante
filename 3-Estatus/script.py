#Seminario de Solución de Problemas de Traductores de Lenguajes 2 |D02| |2022A|
#Victor Manuel Velasco Hernández

import sys
import psutil

def checar_argumento():#Revisa que se haya pasado algún argumento
    if len(sys.argv) == 1:
        print('Este programa no funciona sin argumentos')
        sys.exit(0)

def fijar_objetivo():#Se pasa un argumento del servicio a cerrar

    targets = sys.argv[1:]

    i = 0
    while i < len(targets):

        if not targets[i].endswith('.exe'):
            targets[i] = targets[i] + '.exe'

        i += 1

    return targets

def fijar_ataque(target):#En caso de que el proceso se haya encontrado se preparara para cerrarlo
    for proc in psutil.process_iter():
        if proc.name().lower() == target.lower():
            proc.kill()


if __name__ == '__main__':

    checar_argumento()
    targets = fijar_objetivo()

    while True:
        for target in targets:
            fijar_ataque(target)