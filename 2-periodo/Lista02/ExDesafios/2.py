#Faça um programa que, dado um conjunto N de números, determine menor o valor, o maior valor e a soma dos valores

N = int(input("Informe a quantidade de números que serão inseridos: "))

lista_numeros = []
soma_numeros = 0

for i in range (0, N):
    numero = float(input(f"Informe o {i + 1}° número: "))
    lista_numeros.append(numero)
    soma_numeros += numero

print(f"\nO menor número é: {min(lista_numeros):.2f}")
print(f"O maior número é: {max(lista_numeros):.2f}")
print(f"A soma de todos os valores é: {soma_numeros:.2f}\n")