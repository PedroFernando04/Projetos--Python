from defs_ex01.criar_conexao import criar_conexao
import os

def liste_input(ent):
    sair = 1
    while(True):
        conn = criar_conexao()
        try:
            cursor = conn.cursor()
            query = f"SELECT titulo FROM ex01.jogos WHERE titulo ILIKE '%{ent}%'"
            cursor.execute(query)
            conn.commit()
            row = cursor.fetchall()
            print("")
            if row:
                for i in range (0, len(row)):
                    print(row[i])
            else:
                print("Nenhum jogo encontrado!")
            
            print("\n1 - Pesquisar\n2 - Sair")
            sair = input("Deseja fazer uma nova pesquisa? ")
            if sair == '2':
                return row
            elif sair == '1':
                os.system("cls" or "clear")
                ent = input("Título: ")
            else:
                os.system("cls" or "clear")
                print("Valor inválido!")
                print("Informe um dos valores da tabela\n")
        except Exception as e:
            print(f"ERRO: {e}")
        finally:
            cursor.close()
            conn.close()