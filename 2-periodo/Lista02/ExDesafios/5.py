'''
Faça um programa que peça um número inteiro e determine de ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1
'''
numero = int(input("Informe um número inteiro: "))

contador = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        contador += 1
    if contador > 2:
        print("Não é primo!")
        exit()
if contador <= 2:
    print("É primo!")
