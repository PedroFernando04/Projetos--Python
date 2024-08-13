#Faça um programa que peça dois números e imprima o maior deles

numero1 = int(input("Digite o 1° número: "))

numero2 = int(input("Digite o 2° número: "))

if numero1 > numero2:
    print(numero1)
elif numero2 > numero1:
    print(numero2)
else:
    print("São iguais!")
