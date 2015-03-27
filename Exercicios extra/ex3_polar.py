import math

def distancia(p1, p2):
    dist = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
    dist = math.sqrt(dist)
    return dist

def angulo_rad(p1, p2):
    ang = math.atan2(( p2[1] - p1[1] ) , ( p2[0] - p1[0] ))
    return ang

p1 = []
p2 = []
p1.append(float(input("Digite o valor de X1: ")))
p1.append(float(input("Digite o valor de Y1: ")))
p2.append(float(input("Digite o valor de X2: ")))
p2.append(float(input("Digite o valor de Y2: ")))
dist = distancia(p1, p2)
angulorad = angulo_rad(p1, p2)
angulo = angulorad / math.pi * 180
print("Modulo: " + str(dist))
print("Fase em radianos: " + str(angulorad))
print("Fase em graus: " + str(angulo))
