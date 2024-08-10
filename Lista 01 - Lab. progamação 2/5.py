#Faça um programa que leia três números e mostre o maior deles

auxiliar = 0

for i in range(1,4):
    numero = float(input(f"Informe o {i}° número: "))
    if numero >= auxiliar:
        auxiliar = numero
print(auxiliar)
    