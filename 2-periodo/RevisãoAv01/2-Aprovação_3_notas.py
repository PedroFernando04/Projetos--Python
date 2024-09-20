'''
Desenvolva um algoritmo em Python que receba 3 notas e faça a média. O sistema deverá exibir:

    - Aprovado: se a média for maior ou igual a 7;
    - Reposição: se a média for menor que 7 mas maior ou igual a 4;
    - Reprovado: se a média for menor que 4.
'''
notas = 0

for i in range(1, 4):
    nota = float(input(f"Informe sua {i}° nota: "))
    while nota < 0 or nota > 10:
        print("\nValor inválido!\n")
        nota = float(input(f"Informe sua {i}° nota: "))
    notas += nota
      

if notas/3 >= 7:
   print("Aprovado")
elif notas/3 >= 4:
   print("Reposição")
else:
   print("Reprovado")
