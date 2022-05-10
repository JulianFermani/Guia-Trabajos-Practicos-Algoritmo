# Leer dos números reales, calcular e imprimir
# los dos posibles cocientes entre ellos.

print("Ingrese dos numeros para calcular los posibles cocientes entre ellos")

numeroUno = input("Ingrese el primer numero ")
numeroUno = float(numeroUno)

numeroDos = input("Ingrese el segundo numero ")
numeroDos = float(numeroDos)

primerCociente = numeroUno / numeroDos
segundoCociente = numeroDos / numeroUno

print('El cociente entre ' + str(numeroUno) + ' y ' + str(numeroDos) + ' es ' + str(primerCociente))
print('El cociente entre ' + str(numeroDos) + ' y ' + str(numeroUno) + ' es ' + str(segundoCociente))