'''
Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino ou N-noturno.
Imprima a mensagem "Bom dia!", "Boa tarde!" ou "Boa noite!" ou "Valor inválido!", conforme o caso.
'''

turno = input("Informe o horário que você estuda: ").lower()

match turno:
    case 'm':
        print("Bom dia!")
    case 'v':
        print("Boa tarde!")
    case 'n':
        print("Boa noite!")
    case _:
        print("Valor inválido!")