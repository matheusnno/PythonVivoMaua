def par(x):
    if (x % 2 == 0) :
        return "E par!"
    else:
        return "E impar!"

number = int(input("Digite o numero: "))
print (par(number))
