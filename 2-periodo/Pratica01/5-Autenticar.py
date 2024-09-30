from Usuarios import controlador_usuario

login = input("Informe o login: ")
senha = input("Informa a senha: ")

controlador_usuario.autenticar(login, senha)
