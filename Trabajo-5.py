# Si un lote de terreno tiene X metros de frente por Y metros de fondo: calcular e imprimir la
# cantidad da metros de alambre para cercarlo. (X e Y serán leídos al comenzar el programa).

print("Calculadora de metros de alambre para cercar")

metrosDeFrente = input("Ingrese la cantidad de metros que tiene el frente ")
metrosDeFrente = int(metrosDeFrente)

metrosDeFondo = input("Ingrese la cantidad de metros que tiene de fondo ")
metrosDeFondo = int(metrosDeFondo)

cantidadDeMetrosDeAlambre = metrosDeFondo + metrosDeFrente + metrosDeFondo + metrosDeFrente

print('Se necesitaran ' + str(cantidadDeMetrosDeAlambre) + 'mts de alambre para cercar el terreno de ' + str(metrosDeFrente) + 'mts' + ' x ' + str(metrosDeFondo) + 'mts')