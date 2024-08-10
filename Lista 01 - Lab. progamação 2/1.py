#Faça um programa que peça um número inteiro e determine se ele par ou ímpar. Dica: Utilize o operador módulo(resto de divisão[%])

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("É par!")
else:
    print("É ímpar!")