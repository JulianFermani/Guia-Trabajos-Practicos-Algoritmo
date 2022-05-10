# Dados dos lados de un triángulo, calcular la hipotenusa mediante Pitágoras.

import math

ladoUno = input("Ingrese la medida de un lado del triangulo en cm ")
ladoDos = input("Ingrese la medida del otro lado del triangulo en cm ")

ladoUno = int(ladoUno)
ladoDos = int(ladoDos)

sumaDeCatetos = math.pow(ladoUno, 2) + math.pow(ladoDos, 2) 
hipotenusa = math.sqrt(sumaDeCatetos)

print('La hipotenusa del triangulo dado es ' + str(hipotenusa) + 'cm')