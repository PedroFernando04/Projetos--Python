'''
Escreva um programa em Python que solicite ao usuário um valor inteiro(denominado como 'n').

O programa deve exibir o dobro desse valor para todos os números de 1 até 'n', ou seja,
para cada número no intervalo de 1 até 'n', você deverá caluclar e mostrar o dobro desse número.

Saída esperada:
    Digite um valor inteiro: 5

    Dobro dos números de 1 até 5:
    1: 2
    2: 4
    3: 6
    4: 8
    5: 10
'''

N = int(input("Informe um valor inteiro: "))

print(f"Dobro dos números de 1 até {N}:")

for i in range (1, N + 1):
    print(f"{i}: {i * 2}")