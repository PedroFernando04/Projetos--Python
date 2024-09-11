"""
A série de Fetuccine é gerada da seguinte forma: os dois primeiros termos são fornecidos pelo usuário; a partir daí, os termos são gerados com a soma ou subtração dos dois termos anteriores

3 números inteiros na mesma linha representando: o primeiro termo, o segundo termo e o número de termos da série (maior ou igual a 2), respectivamente.

"""
valores = input().split()

n1 = int(valores[0])
n2 = int(valores[1])
qnt_numeros = int(valores[2])

print(f"\n{n1}\n{n2}")

for i in range (2, qnt_numeros):
    if (i + 1) % 2 != 0:
        prox_num = n1 + n2
    else:
        prox_num = n2 - n1

    print(prox_num)

    n1 = n2
    n2 = prox_num
