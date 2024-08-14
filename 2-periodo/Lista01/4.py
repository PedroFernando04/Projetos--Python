'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
    a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    b. A mensagem "Reprovado", se a média for menor do que sete;
    c. A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

notas_somadas = 0

for i in range(1, 3):
    nota = float(input(f"Insira sua {i}° nota: "))
    notas_somadas += nota

media = notas_somadas/2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
