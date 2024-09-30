def primo_for(numero):
    contador_numero_primo = 0

    for i in range(2, numero):
        if numero % i == 0:
            contador_numero_primo += 1
    if contador_numero_primo > 0:
        return False
    else:
        return True

def primo_recursao(numero, i = 2):
    if numero == i:
        return True
    elif numero % i == 0:
        return False
    else:
        return primo_recursao(numero, i + 1)

n = int(input("Informe um número intero: "))


print(f"\n{primo_for(n)}")
print("----")
print(f"{primo_recursao(n)}\n")

