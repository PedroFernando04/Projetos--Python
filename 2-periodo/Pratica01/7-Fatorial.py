def fatorial_for(numero):
    resultado = numero

    if numero == 0:
        print("0! = 1\n")
    elif numero < 0:
        print("\nValor inválido!\nNão é possível calcular fatorial de um número negativo\n")
    else:
        for i in range(1, numero):
            resultado *= (numero - i)
        print(f"{numero}! = {resultado}\n")

def fatorial_recursao(numero):
    if numero == 0:
        print("0! = 1\n")
    elif numero < 0:
        print("\nValor inválido!\nNão é possível calcular fatorial de um número negativo\n")
    elif numero == 1:
        return numero
    else:
        return numero * fatorial_recursao(numero - 1)
        

n = int(input("\nInforme um número inteiro não negativo: "))

fatorial_for(n)

print(f"{n}! = {fatorial_recursao(n)}")
