"""
Faça um programa, com uma função que necessite de um parâmetro 'número'.
A função retorna o valor de caractere 'P', se o valor for positivo, e 'N', se seu valor for zero ou negativo
"""

def positvo_negativo_ou_zero(numero):
    if numero > 0:
        return print('P')
    else:
        return print('N')
    
n = int(input("informe um número inteiro: "))

positvo_negativo_ou_zero(n)
