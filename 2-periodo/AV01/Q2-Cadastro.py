print("Bem vindo a cadastro")
print("informe qual opção com numeral indicado")


while True:
    print("1 - cadastro \n2 - entrar no sistema \n3 - se deseja sair")
    resposta = int(input())
    match resposta:
        case 1:
            nome = (input("Qual nome do usuário? "))
            senha = (input("Qual senha? "))
        case 2:
            verifica_nome = input("Digite nome do seu usuário: ")
            verifica_senha = input("Digite sua senha: ")
            print(verifica_nome == nome and verifica_senha == senha)
        case 3:
            print("FIm do Programa")
            break

# by : Paulo e Pedro
