
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

vet = []
vet.append(a)
vet.append(b)
vet.append(c)
vet.sort()

if ((vet[2] ** 2) == vet[1] ** 2 + vet[0] ** 2):
    print("E um triangulo retangulo !!")
    area = (vet[1] * vet[0] / 2)
    print("A area do triangulo e: " + str(area))
else:
    print("Nao e um triangulo retangulo !!")
    print("A = {0}, B = {1}, C = {2}".format(a, b, c))
