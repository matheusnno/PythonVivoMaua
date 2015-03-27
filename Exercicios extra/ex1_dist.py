import math

def distancia(p1, p2):
    dist = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
    dist = math.sqrt(dist)
    return dist

p1 = []
p2 = []
p1.append(float(input("Digite o valor de X1: ")))
p1.append(float(input("Digite o valor de Y1: ")))
p2.append(float(input("Digite o valor de X2: ")))
p2.append(float(input("Digite o valor de Y2: ")))

print (distancia(p1, p2))
