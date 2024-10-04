def quantidade_de_palavras(frase):
    lista_palvras = frase.split()
    return(len(lista_palvras))

frase = input("Escreva uma frase: ")

print(f'\nSua frase tem {quantidade_de_palavras(frase)} palavras\n')
