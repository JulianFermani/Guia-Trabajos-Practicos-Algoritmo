# Teniendo como dato el lado de un cuadrado, 
# calcular e imprimir la superficie y perímetro

medidaLadoCuadrado = input("Ingrese la medida del lado del cuadrado en cm ")
medidaLadoCuadrado = int(medidaLadoCuadrado)

perimetroDelCuadrado = 4 * medidaLadoCuadrado
superficieDelCuadrado = medidaLadoCuadrado * medidaLadoCuadrado

print('El perimetro del cuadrado es ' + str(perimetroDelCuadrado) + 'cm')
print('La superficie del cuadrado es ' + str(superficieDelCuadrado) + 'cm²')