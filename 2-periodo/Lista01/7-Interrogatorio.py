'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    a. "Telefonou para a vítima?"
    b. "Esteve no local do crime?"
    c. "Mora perto da vítima?"
    d. "Devia para a vítima?"
    e. "Já trabalhou para a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 
como "Cúmplice" e com 5 como "Assassino". 

Caso contrário, ela será classificado como "Inocente"
'''

print("\nResponda as perguntas relacionando você à vítima utilizando 'S' para \"sim\" e 'N' para \"Não\"")

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou para a vítima?"]
contador = 0

for i in range(0, 5):
    resposta = input(f'\n{perguntas[i]} ').lower()
   
    if resposta == 's':
        contador += 1

if contador == 5:
    print("Resultado: Assassino")
elif contador == (3 or 4):
    print("Resultado: Cúmplice")
elif contador == 2:
    print("Resultado: Suspeita")
else:
    print("Resultado: Inocente")
