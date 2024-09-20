'''
Faça um programa que leia e valide as seguintes informações:
    1. Nome: maior que 3 caracteres;
    2. Idade: entre 0 e 150;
    3. Salário: maior que zero;
    4. Sexo: 'f' ou 'm';
    5. Estado civil: 's', 'c', 'v', 'd';
    5. Use a função len(string) para saber o tamanho de um texto(número de caracteres).
'''

print("Vamos realizar o seu cadastro:\n")

nome = input("Nome: ")
idade = int(input("Idade: "))
salario = int(input("Salário: "))
sexo = input("Sexo: ").upper()
estado_civil = input("Estado Civil: ").upper()
print('\n')

dado_requisito = [[nome, "o nome deve ter mais que 3 caracteres", len(nome) > 3], 
                  
                  [idade, "a idade deve ser entre 0 e 150", idade >= 0 and idade <= 150], 
                  
                  [salario, "o salário deve ser maior que zero", salario > 0], 
                  
                  [sexo, "informe o sexo como: 'F' ou 'M'", sexo == 'F' or sexo == 'M'], 
                  
                  [estado_civil,"informe o estado civil como: 'S', 'C', 'V', 'D'", estado_civil == 'S' or estado_civil == 'C' or estado_civil == 'V' or estado_civil == 'D']]

def valido(dado):
    print(f"{dado} (Válido!)")
def invalido(dado, requisito):
    print(f"\n{dado} - Inválido!\n{requisito}")


for i in range(0, 5):
    if dado_requisito[i][2]:
        valido(dado_requisito[i][0]) 
    else:
        invalido(dado_requisito[i][0], dado_requisito[i][1])
print("\n")
