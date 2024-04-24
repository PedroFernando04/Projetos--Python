entrada = int(input("Digite um número: "))
if(entrada == 0 or entrada == 1):
    print(f"O fatorial de {entrada} é: {entrada}")
    exit()
else:
    i = 1
    p = entrada
    loop = 0
    print(f"O fatorial de {entrada} é", end="")
    while(1):
        fator = p - i
        if(fator < 1):
            break
        else:
            resultado =(entrada * fator) 
        #print(f"{entrada} * {fator} = {resultado}")
            entrada = resultado
            loop += 1
            i += 1
    print(":",resultado)
