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

def controlador_usuario(login, senha):

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
                controlador_usuario(login, senha)
        else:
            contador_usuario_errado += 1

    if contador_usuario_errado == len(usuarios):
        print("\nUsuário não encontrado!\n")
        login = input("Informe o login: ")
        controlador_usuario(login, senha)
