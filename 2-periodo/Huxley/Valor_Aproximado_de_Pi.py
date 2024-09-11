"""
Sendo pi = (S*32)^(1/3). Fazer um programa para calcular e escrever o valor de pi utilizando n termos da série dada.

O valor aproximado de pi pode ser calculado usando-se a série:
S = 1/1^3 - 1/3^3 + 1/5^3 - 1/7^3 + 1/9^3 - ...

"""

qnt_S = int(input())
valor_S = 0


for i in range(0, qnt_S):
    if i % 2 == 0:
        valor_S += 1/(1 + 2 * i)**3
    else:
        valor_S -= 1/(1 + 2 * i)**3


pi = (valor_S*32)**(1/3)

print("{:.5f}".format(pi))
