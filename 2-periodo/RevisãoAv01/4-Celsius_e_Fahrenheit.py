'''
Você foi designado para desenvolver um programa que converta temperaturas entre diferentes escalas. Suas tarefas são as seguintes:

a) Escreva um programa em Python que exiba um menu com as seguintes opções:

    Converter de Celsius para Fahrenheit

    Converter de Fahrenheit para Celsius

b) Caso o usuário selecione 1 (Converter C° para F°)

    Realize a conversão da temperatura utilizando a fórmula: F° = (C° * 9/5) + 32.
    Exiba o resultado da conversão

c) Caso o usuário selecione 2 (Converter F° para C°)

    Realize a conversão da temperatura utilizando a fórmula: C° = (F° - 32) * 5/9.
    Exiba o resultado da conversão
'''

print("Bem-vindo ao Conversor de Temperaturas!\n")
print("Escolha uma opção:\n\n1 - Converter de Celsius para Fahrenheit\n2 - Converter de Fahrenheit para Celsius")
tipo_de_conversao = int(input(""))

if tipo_de_conversao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius:.1f} graus Celsius é igual a {fahrenheit:.1f} graus Fahrenheit\n")

elif tipo_de_conversao == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit:.1f} graus Fahrenheit é igual a {celsius:.1f} graus Celsius\n")

else:
    print("Opção inválida!")
