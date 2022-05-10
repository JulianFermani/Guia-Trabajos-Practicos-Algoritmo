# Leer un número positivo, calcular su 
# cuadrado y su cubo. Imprimir los resultados.

numero = input("Ingrese un numero para calcular su cuadrado ")
numero = int(numero)

if numero < 0:
    print("Por favor, ingresa un numero positivo")
else:
    numeroAlCuadrado = numero * numero
    numeroAlCubo = numero * numero * numero

    print('El cuadrado de ' + str(numero) + ' es ' + str(numeroAlCuadrado))
    print('El cubo de ' + str(numero) + ' es ' + str(numeroAlCubo))
