#F° = (C° * 9/5) + 32.
#C° = (F° - 32) * 5/9.

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

temperatura = int(input("\nInforme a temperatura que deseja converter: "))

retorno_da_função = celsius_fahrenheit(temperatura)

print(f"\n{temperatura}{retorno_da_função[1]} = {retorno_da_função[0]}{retorno_da_função[2]}")


