import math

pi = float(math.pi)
raio = float(input("Digite o valor do raio:"))
Comprimento_circuferencia = float(2* pi* raio)
area_circulo = float(pi *(raio**2))
Area_esfera = float(4*pi*(raio**2))
Volume_esfera = float(4//3*pi*(raio**3))
print(f'''\nO comprimente do circuferencia é {Comprimento_circuferencia:6f} \nA area do circulo é {area_circulo:6f} \n
 a area da esfera é {Area_esfera:6f} \nO volume da esfera é {Volume_esfera:6f}''')
