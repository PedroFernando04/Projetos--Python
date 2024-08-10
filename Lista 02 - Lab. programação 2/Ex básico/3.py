#Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser

while(1):

    print("\nOperação - Adição")

    n1 = int(input("\nDigite o primeiro número: "))
    n2 = int(input("\nDigite o segundo número: "))

    soma = n1 + n2

    print(f"\n{n1} + {n2} = {soma}")

    loop = input(("\nDeseja realizar mais uma soma? [S ou N] ")).lower()
    print(f"\nResposta: {loop}")

    if(loop == 'n'):
        break