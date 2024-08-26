'''
Crie uma lista contendo dicionários de produtos de forma a representar:
    {
        'nome': 'Nome_Produto_1'
        'preco': 'Preço_Produto_1'
    }

    {
        'nome': 'Nome_Produto_2'
        'preco': 'Preço_Produto_2'
    }

    Mostre a usuário todos os produtos dessa lista:

    Produto 1 - 50 R$
    Produto 2 - 60 R$
    ...
    Produto N - xx R$
'''
lista = [
    {
        'nome':'O Espadachim de Carvão',
        'preco':34.99
    },

    {
        'nome':'Morte do Nilo',
        'preco':44.99
    },

    {
        'nome':'O curioso caso de Benjamin Button',
        'preco':39.90
    },

    {
        'nome':'Lawrence da Arábia',
        'preco':24.90
    },

    {
        'nome':'Quem mexeu no meu queijo?',
        'preco':56.90
    }
        ]
print('\n')
for i in range(0, len(lista)):
    print(f"{lista[i]['nome']} - R$ {lista[i]['preco']:.2f}")
print('\n')