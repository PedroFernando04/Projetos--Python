#Faça um programa, utilizando while, que permita o usuário fazer contas de adição enqunato quiser
while(1):
    print("Operação - Adição!\n")

    numeros = 0

    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))

    print(f"\n{n1} + {n2} = {n1 + n2}\n")

    resposta = input("Deseja realizar mais uma soma? [S ou N] ").lower()
    print(f"Resposta: {resposta}")
    if resposta == 'n':
        break
    elif resposta != 'n' and resposta != 's':
        print("Resposta inválida!")
        resposta = input("Deseja realizar mais uma soma? [S ou N] ").lower()
