op = [["Adição", '+'], ["Subtração", '-'], ["Multiplicação", 'x'], ["Divisão", '%']]

print("Bem vindo(a) a Calculadora!\n")

while 1:
    print("\nSelecione a operção que deseja realizar:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")

    operacao = int(input())

    print(f"\nVocê selecionou - {op[operacao - 1][0]}\n")
    print("Agora informe os números que serão utilizados nessa operação:")

    n1 = float(input("\nInforme o primeiro número: "))
    n2 = float(input("Informe o segundo número: "))

    match(operacao):
        case 1:
            resultado = n1 + n2
        case 2: 
            resultado = n1 - n2
        case 3:
            resultado = n1 * n2
        case 4:
            while(n2 == 0):
                print("\nValor inválido!\nO denominador não pode ser 0!\n")
                n2 = float(input("Informe o segundo número: "))

            resultado = n1 / n2

    print(f"\n{n1:.2f} {op[operacao - 1][1]} {n2:.2f} = {resultado:.2f}\n")

    loop = input("Deseja fazer uma nova operação?[S/N]").lower()
    if loop == 'n':
        print("Encerrando...")
        break
