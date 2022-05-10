#   Leer un número e imprimirlo junto con sus primeros múltiplos,
#   ejemplifique para los primeros 4 múltiplos del número ingresado.

from ast import Mod

print("Hola, ingrese un numero para sacarle los multiplos")

numero = input()
numero = int(numero)

multiplos = 1

def encontrarMultiplos(numero, multiplos):
    if numero % multiplos == 0:
        print('El ' + str(multiplos) + ' es multiplo de ' + str(numero))
   
for i in range(5):
    encontrarMultiplos(numero, multiplos)
    multiplos = multiplos + 1
