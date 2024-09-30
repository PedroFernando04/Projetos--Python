def quantidade_de_vogais(palavra):
    contador_vogais = 0

    for i in palavra:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            contador_vogais += 1
    if contador_vogais == 1:
        print(f"\n\"{palavra}\" tem {contador_vogais} vogal\n")
    else:
        print(f"\n\"{palavra}\" tem {contador_vogais} vogais\n")

palavra = input("\nInforme uma palavra: ")

quantidade_de_vogais(palavra)
