"""
Feita a questão 3 crie uma função calcular que recebe 3 parâmetros:
    numero1, numero2 e operação (pode ser somar; subtrair; multiplicar e dividir)
"""
resultado = 0

def calcular(n1, n2, op):
    resultado = 0

    match op:
        case 1:
            resultado = n1 + n2
        case 2: 
            resultado = n1 - n2
        case 3: 
            resultado = n1 * n2
        case 4: 
            if n2 != 0:
                resultado = n1 / n2
            else:
                print("ERRO - Divisão por 0")
                return 0
        case _: 
            print("Valor inválido!")

    return print(resultado)

print("Bem vindo(a) a calculadora!\n")
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

print("\nAgora informe a operação que deseja realizar: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input("\n"))

calcular(n1, n2, op)
