import sys
import time
import pickle
import os

print("Seminario de Solucion de Problemas de Traductores de Lenguaje II")
print("Velasco Hernandez, Victor Manuel ")
checkpoint = {}
found = False

def saveProcess():
    pickle_out=open("dict.pickle","wb")
    pickle.dump(checkpoint,pickle_out)
    pickle_out.close()

def recoverProcess():
    try:
        with open("dict.pickle", "r") as data:
            #checkpoint.readline()
            print("Se ha encontrado un Checkpoint")
            pickle_in = open("dict.pickle", "rb")
            data = pickle.load(pickle_in)
            #print(data)
            pickle_in.close()
            return data
    except FileNotFoundError:
        print("No se ha encontrado un Checkpoint")
        return {}




finalizado=True
checkpoint=recoverProcess()
opc=0
while True:
    finalizado=True
    if opc==5:
        print("Hasta la proxima!")

        break
    print("Bienvenido a la Calculadora 3000- Tolerante a fallos con Checkpoint \U0001F4BB \U0001F511")
    if 'NUM2' in checkpoint:
        decision = int(input("Se han detectado de un proceso ya finalizado, desea volver a cargarlos? 0==Si o 1==No\n"))
        if decision == 1:
            checkpoint = {}
    if checkpoint == {}:
        print("Escoge el proceso que desees realizar:\n1)Suma\n2)Resta\n3)Multiplicacion\n4)Division\n5)Salir")
    else:
        print("Restaurando punto de control")


    while finalizado:
        try:
            if checkpoint:
                opc = checkpoint['OPC']
                if opc==1:
                    print("Volviendo al proceso de suma")
                elif opc==2:
                    print("Volviendo al proceso de resta")
                elif opc==3:
                    print("Volviendo al proceso de multiplicacion")
                elif opc==4:
                    print("Volviendo al proceso de Division")
                elif opc==5:
                    finalizado==False
                    False
            else:
                opc = int(input("Introduce tu opcion:"))

            if opc == 5:
                break
            else:
                checkpoint['OPC'] = opc
                saveProcess()
                while finalizado:
                    try:
                        if 'NUM1' in checkpoint:
                                num1=checkpoint['NUM1']
                                if 'NUM2' in checkpoint:
                                    num2=checkpoint['NUM2']
                                else:
                                    num2 = int(input("Introduce un segundo numero:"))
                                    checkpoint['NUM2'] = num2
                                    saveProcess()
                        else:
                            num1 = int(input("Introduce el primer numero:"))
                            checkpoint['NUM1'] = num1
                            saveProcess()
                            num2 = int(input("Introduce un segundo numero:"))
                            checkpoint['NUM2'] = num2
                            saveProcess()

                        if opc==1:
                            print("El resultado de la suma de ",num1," + ",num2," =",num1+num2)
                            time.sleep(3)
                            finalizado=False
                            False
                        elif opc == 2:
                            print("El resultado de la resta de ", num1, " - ", num2, " =", num1 -num2)
                            time.sleep(3)
                            finalizado = False
                            False
                        elif opc == 3:
                            print("El resultado de la multiplicacion de ", num1, " * ", num2, " =", num1 * num2)
                            time.sleep(3)
                            finalizado = False
                            False
                        elif opc == 4:
                            print("El resultado de la division de ", num1, "/", num2, " =", num1 / num2)
                            time.sleep(3)
                            finalizado = False
                            False
                        else:
                            print("Volviendo al menu principal")
                            finalizado = False
                        #checkpoint={}
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



