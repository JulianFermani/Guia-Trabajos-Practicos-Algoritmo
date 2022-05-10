# Leer tres números, calcular e 
# imprimir los seis posibles cocientes.

print("Ingrese tres numeros para calcular los posibles cocientes entre ellos")

numeroUno = input("Ingrese el primer numero ")
numeroUno = int(numeroUno)

numeroDos = input("Ingrese el segundo numero ")
numeroDos = int(numeroDos)

numeroTres = input("Ingrese el tercer numero ")
numeroTres = int(numeroTres)

primerCociente = numeroUno / numeroDos
segundoCociente = numeroUno / numeroTres
tercerCociente = numeroDos / numeroUno
cuartoCociente = numeroDos / numeroTres
quintoCociente = numeroTres / numeroUno
sextoCociente = numeroTres / numeroDos

print('El cociente entre ' + str(numeroUno) + ' y ' + str(numeroDos) + ' es ' + str(primerCociente))
print('El cociente entre ' + str(numeroUno) + ' y ' + str(numeroTres) + ' es ' + str(segundoCociente))
print('El cociente entre ' + str(numeroDos) + ' y ' + str(numeroUno) + ' es ' + str(tercerCociente))
print('El cociente entre ' + str(numeroDos) + ' y ' + str(numeroTres) + ' es ' + str(cuartoCociente))
print('El cociente entre ' + str(numeroTres) + ' y ' + str(numeroUno) + ' es ' + str(quintoCociente))
print('El cociente entre ' + str(numeroTres) + ' y ' + str(numeroDos) + ' es ' + str(sextoCociente))