print("Bem vindo(a) a Calculadora!\n\nSelecione a operção que deseja realizar:")
print("\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")

op = [["Adição", '+'], ["Subtração", '-'], ["Multiplicação", 'x'], ["Divisão", '%']]

operacao = int(input())

print(f"\nVocê selecionou - {op[operacao - 1][0]}\n")
print("Agora informe os números que serão utilizados nessa operação:")

n1 = int(input("\nInforme o primeiro número: "))
n2 = int(input("Informe o segundo número: "))

match(operacao):
    case 1:
        resultado = n1 + n2
    case 2: 
        resultado = n1 - n2
    case 3:
        resultado = n1 * n2
    case 4:
        resultado = n1 / n2

print(f"\n{n1} {op[operacao - 1][1]} {n2} = {resultado}")
