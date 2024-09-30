def soma_lista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma
def criar_lista():
    n = int(input("Informe o tamanho da lista: "))
    lista = []
    print('')
    for i in range(0, n):
        lista.append(float(input(f"Informe o {i + 1}° número da lista: ")))
    return lista

print(f"\nA soma total da lista inserida é: {soma_lista(criar_lista())}\n")
