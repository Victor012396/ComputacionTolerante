import sys
import time
import os
print("Seminario de Solucion de Problemas de Traductores de Lenguaje II")
print("Velasco Hernandez, Victor Manuel ")
while True:
    print("Bienvenido a la Calculadora 3000- Tolerante a fallos \U0001F4BB \U0001F511")
    print("Escoge el proceso que desees realizar:\n1)Suma\n2)Resta\n3)Multiplicacion\n4)Division\n5)Salir")

    try:
        opc=int(input("Introduce tu opcion:"))
        if opc==5:
            break
        else:
            while True:
                try:
                    num1 = int(input("Introduce el primer numero:"))
                    num2 = int(input("Introduce un segundo numero:"))
                    if opc==1:
                        print("El resultado de la suma de ",num1," + ",num2," =",num1+num2)
                        time.sleep(3)
                        False
                    if opc == 2:
                        print("El resultado de la resta de ", num1, " - ", num2, " =", num1 -num2)
                        time.sleep(3)
                        False
                    if opc == 3:
                        print("El resultado de la multiplicacion de ", num1, " * ", num2, " =", num1 * num2)
                        time.sleep(3)
                        False
                    if opc == 4:
                        print("El resultado de la division de ", num1, "/", num2, " =", num1 / num2)
                        time.sleep(3)
                        False
                    else:
                        print("Volviendo al menu principal")
                except ValueError:
                    print("Valor incorrecto, introduce un digito, vuelve a intentarlo \U0001F641")
                    time.sleep(3)
                except ZeroDivisionError:
                    print("La divison entre cero, ha producido un error, vuelve a intentarlo \U0001F641")
                    time.sleep(3)

    except ValueError:
        print("Valor incorrecto, introduce un digito,vuelve a intentarlo \U0001F641")
        time.sleep(3)

    except KeyboardInterrupt:
                opc2= input("\nSeguro que deseas salir?(S/N)?")
                if opc2=="S"or opc2=="s":
                    print("Hasta la proxima!")
                    break
                    sys.exit()
                if opc2=="N" or opc2=="n":
                    print("Volviendo al menu principal!")



