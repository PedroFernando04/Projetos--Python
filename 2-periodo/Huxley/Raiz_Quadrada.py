"""
Uma das maneiras de se conseguir a raiz quadrada de um n�mero � subtrair do n�mero os �mpares consecutivos a partir de 1, at� que o resultado da subtra��o seja menor ou igual a zero. O n�mero de vezes que se conseguir fazer a subtra��o � a raiz quadrada exata (resultado 0) ou aproximada do n�mero (resultado negativo). Fa�a um programa para calcular a raiz quadrada de um n�mero inteiro dado.

16 - 1 = 15 - 3 = 12 - 5 = 7 - 7 = 0
raiz � 4
"""

numero = int(input())

contador_raiz = 0

while(numero > 0):
    numero -= 1 + (2 * contador_raiz)
    contador_raiz += 1

print(contador_raiz)
