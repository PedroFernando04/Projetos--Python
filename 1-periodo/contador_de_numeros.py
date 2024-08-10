i = 0

contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0

array = [0] * 5

while i < 5:
    array[i] = float(input())
    i+=1
    
for num in array:
    if num % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
    if num > 0:
        contador_positivos += 1
    elif num < 0:
        contador_negativos += 1

print("{:.0f} valor(es) par(es)".format(contador_pares))
print("{:.0f} valor(es) impar(es)".format(contador_impares))
print("{:.0f} valor(es) positivo(s)".format(contador_positivos))
print("{:.0f} valor(es) negativo(s)".format(contador_negativos))
