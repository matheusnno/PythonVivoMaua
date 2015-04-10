import sys

soma = 0
count = 0
lista = []
while True:
    try:
        b = input("Digite a nota: ")
        if b == "" :
            break
        float(b)
        break
    except:
        print("Voce nao digitou um numero valido")
while True:
    if b == "":
        break
    try:
        b = float(b)
    except:
        print("Voce nao digitou um numero valido!")
        sys.exit(-1)
    if b >= 0 :
        soma += b
        count += 1
        lista.append(b)
        while True:
            try:
                b = input("Digite a nota: ")
                if b == "" :
                    break
                float(b)
                break
            except:
                print("Voce nao digitou um numero valido!")
    elif b < 0:
        break

try:
    print ("\nA media destes {0} numeros eh {1}".format(count, soma/count))
except:
    print("Voce digitou algo errado!")
print("\nA maior nota eh: ", max(lista))
