positivo = 0
negativo = 0
zero = 0

for i in range(0, 10):
    numero = int(input(f"Digite o {i+1}º numero: "))
    if numero > 0:
        positivo += 1
    elif numero == 0:
        zero += 1
    else:
        negativo += 1

print(f"Positivos: {positivo}")
print(f"negativos: {negativo}")
print(f"zero: {zero}")
# by : Paulo e Pedro
