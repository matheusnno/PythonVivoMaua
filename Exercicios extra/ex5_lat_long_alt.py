import math

def latitude(x, y) :
    return math.atan(y / x)

def LongAlt(x, y, z):
    count = 0
    E = 0.00669454185
    a = 6378160
    h = 0
    N = 1
    P = math.sqrt((x ** 2) + (y ** 2))
    tangTheta = (z / P) * (1 - E * N / (N + h)) ** -1
    Theta = math.atan(tangTheta)
    
    while count < 5 :
        N = a / (math.sqrt(1 - E * math.sin(Theta) ** 2))
        h = P / (math.cos(Theta)) - N
        tangTheta = ((z / P) / (1 - E * N / (N + h)))
        count += 1
        
    Theta = math.atan(tangTheta)
    aux = [Theta, h]   
    return aux

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
z = float(input("Digite o valor de z: "))

lat = math.degrees(latitude(x, y))
aux = LongAlt(x, y, z)
long = math.degrees(aux[0])
alt = aux[1] * 1000
print("Latitude: {0}º , Longitude: {1}º , Altitude: {2} m".format(lat, long, alt))
