'''
A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500
'''

i = 0
aux = 1

while 1:
    if i > 500:
        print(i)
        break

    fibo = i + aux
    print(i)
    i = aux
    aux = fibo
