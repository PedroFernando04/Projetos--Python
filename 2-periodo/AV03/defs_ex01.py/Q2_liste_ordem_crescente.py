from defs_ex01.criar_conexao import criar_conexao

def liste_ordem_crescente():
    conn = criar_conexao()
    cursor = conn.cursor()
    query = "SELECT titulo FROM ex01.jogos ORDER BY titulo"
    cursor.execute(query)
    conn.commit()
    row = cursor.fetchall()
    for i in range(0, len(row)):
        print(row[i])
    cursor.close()
    conn.close()
