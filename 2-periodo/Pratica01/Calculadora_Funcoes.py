def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return print("ERRO - Divisão por 0")
    
print("Bem vindo(a) a calculadora!\n")
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

print("\nAgora informe a operação que deseja realizar: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = input("\n")
resultado = 0
match(op):
    case '1':
        resultado = somar(n1, n2)
    case '2':
        resultado = subtrair(n1, n2)
    case '3':
        resultado = multiplicar(n1, n2)
    case '4':
        resultado = dividir(n1, n2)
    case _:
        print("Valor inválido!")
print(resultado)
