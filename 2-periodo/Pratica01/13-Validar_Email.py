def validar_email(email):
    if '@' in email:
        print("\nE-mail válido!\n")
        return True
    else:
        print("\nFormato inválido!")
        email = input("\nInforme o seu e-mail: ")
        validar_email(email)

email = input("\nInforme o seu e-mail: ")

validar_email(email)
