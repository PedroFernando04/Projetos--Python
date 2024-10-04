#Q1
def positvo_negativo_ou_zero(numero):
    if numero > 0:
        return print('P')
    else:
        return print('N')
#Q2    
def quantidade_de_digitos(numero):
    contador_digito = 0
    for i in numero:
        contador_digito += 1
    return contador_digito

#Q3
def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return print("ERRO - Divisão por 0")
    
#Q4
def calcular(n1, n2, op):
    resultado = 0

    match op:
        case 1:
            resultado = n1 + n2
        case 2: 
            resultado = n1 - n2
        case 3: 
            resultado = n1 * n2
        case 4: 
            if n2 != 0:
                resultado = n1 / n2
            else:
                print("ERRO - Divisão por 0")
                return 0
        case _: 
            print("Valor inválido!")

    return print(resultado)

#Q5

usuarios = [
    {
        'username': 'teste',
        'password': 'admin'
    },
    {
        'username': 'teste2',
        'password': 'admin2'
    },
    {
        'username': 'teste3',
        'password': 'admin4'
    },
    {
        'username': 'teste4',
        'password': 'admin4'
    }
]

def autenticar(login, senha):

    contador_usuario_errado = 0

    for i in range (len(usuarios)):
        if login == usuarios[i]['username']:
            print("\nUsuário Válido!")
            if senha == usuarios[i]['password']:
                print("Senha Válida!\n")
                break
            else:
                print("Senha inválida!\n")
                senha = input("Informa a senha: ")
                autenticar(login, senha)
        else:
            contador_usuario_errado += 1

    if contador_usuario_errado == len(usuarios):
        print("\nUsuário não encontrado!\n")
        login = input("Informe o login: ")
        autenticar(login, senha)

#Q6

def quantidade_de_vogais(palavra):
    contador_vogais = 0

    for i in palavra:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            contador_vogais += 1
    if contador_vogais == 1:
        print(f"\n\"{palavra}\" tem {contador_vogais} vogal\n")
    else:
        print(f"\n\"{palavra}\" tem {contador_vogais} vogais\n")

#Q7

def fatorial_for(numero):
    resultado = numero

    if numero == 0:
        print("0! = 1\n")
    elif numero < 0:
        print("\nValor inválido!\nNão é possível calcular fatorial de um número negativo\n")
    else:
        for i in range(1, numero):
            resultado *= (numero - i)
        print(f"{numero}! = {resultado}\n")

def fatorial_recursao(numero):
    if numero == 0:
        print("0! = 1\n")
    elif numero < 0:
        print("\nValor inválido!\nNão é possível calcular fatorial de um número negativo\n")
    elif numero == 1:
        return numero
    else:
        return numero * fatorial_recursao(numero - 1)
    
#Q8

def primo_for(numero):
    contador_numero_primo = 0

    for i in range(2, numero):
        if numero % i == 0:
            contador_numero_primo += 1
    if contador_numero_primo > 0:
        return False
    else:
        return True

def primo_recursao(numero, i = 2):
    if numero == i:
        return True
    elif numero % i == 0:
        return False
    else:
        return primo_recursao(numero, i + 1)

#Q9

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

#Q10

def quantidade_de_palavras(frase):
    lista_palvras = frase.split()
    return(len(lista_palvras))

#Q11

from FUNCTIONS import pf

def media_lista():

    lista = pf.criar_lista()
    soma = pf.soma_lista(lista)
    media = soma / len(lista)

    return media

#Q12

def celsius_fahrenheit(temperatura_atual):
    print("\nInforme a conversão que deseja fazer: ")
    print("\n1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    conversao = float(input("\n"))

    match(conversao):
        case 1:
            tipo_temperatura_inicial = '°C'
            temperatura_final = (temperatura_atual * 9/5) + 32
            tipo_temperatura_final = '°F'
        case 2:
            tipo_temperatura_inicial = '°F'
            temperatura_final = (temperatura_atual - 32) * 5/9
            tipo_temperatura_final = '°C'
        case _:
            print("ERRO: Dígito inválido!")
            celsius_fahrenheit(temperatura_atual)
    
    return temperatura_final, tipo_temperatura_inicial, tipo_temperatura_final

#Q13

def validar_email(email):
    if '@' in email:
        print("\nE-mail válido!\n")
        return True
    else:
        print("\nFormato inválido!")
        email = input("\nInforme o seu e-mail: ")
        validar_email(email)
