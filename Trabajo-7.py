# Ingresar un número por teclado e 
# imprimir el valor absoluto del número.

numero = input("Ingrese un numero para que le devuelva su valor absoluto ")
numero = int(numero)

if numero < 0: 
    print('El valor abosoluto de ' + str(numero) + ' es ' + str(abs(numero)))
else:
    print('El valor abosoluto de ' + str(numero) + ' es ' + str(numero))
