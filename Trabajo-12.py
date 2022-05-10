# Teniendo como dato la hipotenusa y el ángulo que forma ésta con la base de un triángulo
# rectángulo. calcular e imprimir los datos y ángulos restantes.

import math

hipotenusa = input("Ingrese el valor de la hipotenusa en cm ")
anguloDelTriangulo = input("Ingrese el valor del angulo que forma la hipotenusa con la base del rectangulo ")

hipotenusa = float(hipotenusa)
anguloDelTriangulo = float(anguloDelTriangulo)

senoDelAngulo = math.sin(anguloDelTriangulo)
catetoOpuesto = hipotenusa * senoDelAngulo
catetoOpuesto = round(catetoOpuesto, 2)




print('La medida del cateto opuesto es de ' + str(catetoOpuesto) + ' cms' )
print
