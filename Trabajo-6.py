# Un pintor sabe que con una pintura determinada puede pintar 3,6 metros cuadrados 
# por cada medio litro. Sabiendo la altura y el largo de la pared a pintar, informar
# cuántos litros de pintura utilizará. (Altura y Largo en metros).
import math

alturaDeLaPared = input("Ingrese la altura en metros de la pared a pintar ")
largoDeLaPared = input("Ingrese el largo en metros de la pared a pintar ")

alturaDeLaPared = float(alturaDeLaPared)
largoDeLaPared = float(largoDeLaPared)

rendimientoPinturaPorLitro = 7.2 #metros al cuadrado

superficieAPintar = alturaDeLaPared * largoDeLaPared

totalPinturaAUsar = superficieAPintar / rendimientoPinturaPorLitro
totalPinturaAUsar = math.ceil(totalPinturaAUsar)

print('Debera usar ' + str(totalPinturaAUsar) + ' litros de pintura')