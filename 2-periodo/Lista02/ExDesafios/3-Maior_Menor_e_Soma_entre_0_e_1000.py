#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000

N = int(input("Informe a quantidade de números que serão inseridos: "))

lista_numeros = []
soma_numeros = 0

for i in range (0, N):
    numero = float(input(f"Informe o {i + 1}° número: "))
    while(numero < 0 or numero > 1000):
        print("\nValor inválido!\nInsira um número entre 0 e 1000\n")
        numero = float(input(f"Informe o {i + 1}° número: "))
    lista_numeros.append(numero)
    soma_numeros += numero

print(f"\nO menor número é: {min(lista_numeros):.2f}")
print(f"O maior número é: {max(lista_numeros):.2f}")
print(f"A soma de todos os valores é: {soma_numeros:.2f}\n")
