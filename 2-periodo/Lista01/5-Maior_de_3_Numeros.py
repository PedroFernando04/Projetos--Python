#Faça um programa que leia três números e mostre o maior deles

numero = float(input(f"Informe o 1° número: "))
auxiliar = numero

for i in range(0,2):
    numero = float(input(f"Informe o {i + 2}° número: "))
    if numero >= auxiliar:
        auxiliar = numero
print(auxiliar)
    
