import math


def distancia(x1, y1, x2, y2):
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)
    return dist


x = []
y = []
distMax = 0

while True:
    a = input("Digite o valor de X ou Enter para sair: ")
    if a == "" :
        break
    else:
        b = input("Digite o valor de Y: ")
        x.append(float(a))
        y.append(float(b))

for i in range(len(x)):
    for j in range(len(y)):
        c = distancia(x[ j ], y[ j ], x[ i ], y[ i ])
        if c > distMax :
            distMax = c        

print("O valor maximo e: " + str(distMax))
