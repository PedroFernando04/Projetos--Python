notas_somadas = 0

for i in range(1, 4):
    nota_entrada = float(input(f"Digite sua {i}° nota: "))
    notas_somadas += nota_entrada

media = notas_somadas/3

print(f"Sua média é: {media}")