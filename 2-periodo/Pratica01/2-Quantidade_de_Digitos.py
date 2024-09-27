"""
Escreva uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""

def quantidade_de_digitos(numero):
    contador_digito = 0
    for i in numero:
        contador_digito += 1
    return contador_digito

n = input("Informe um número inteiro: ")

print(f"{n} tem {quantidade_de_digitos(n)} dígito(s)")
