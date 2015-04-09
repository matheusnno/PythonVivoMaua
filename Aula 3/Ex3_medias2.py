soma = 0
count = 0

b = input("Digite a nota: ")
while True:
    if b == "":  # excelente checkagem
        break
    b = float(b)
    if b >= 0 :
        soma += b
        count += 1
        b = input("Digite a nota: ")
    elif b < 0:
        break

print ("A media destes {0} numeros e {1}".format(count, soma/count))

# Nota: 1.0
# Comentario: bom cuidado com input do usuario
