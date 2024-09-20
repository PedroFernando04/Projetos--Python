numero = int(input("Informe um valor inteiro maior que 100 e menor que 1000: "))

for i in range(1, numero + 1):
    dezenas = (i % 100) // 10 == 4

    if numero <= 100 or numero >= 1000:
        numero = int(input(
            "valor invalido,Informe um valor inteiro maior que 100 e menor que 1000: "))
    elif i == numero:
        break
    else:
        if i % 4 == 0 or i % 10 == 4 or i // 10 == 4:
            print('PIN')
        elif i // 100 == 4 or dezenas:
            print('PIN')
        else:
            print(i)

# by : Paulo e Pedro
