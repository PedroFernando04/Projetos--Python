from FUNCTIONS import pf

def media_lista():

    lista = pf.criar_lista()
    soma = pf.soma_lista(lista)
    media = soma / len(lista)

    return media

print(f"\nA média da sua lista é: {media_lista()}\n")
