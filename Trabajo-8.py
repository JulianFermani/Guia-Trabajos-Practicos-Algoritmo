# Leer un número e informar si es entero.

numero = input("Ingresar un numero para ver si es entero ")

if numero.isnumeric():
    print("Este numero es entero")
else:
    print("Este numero no es entero")