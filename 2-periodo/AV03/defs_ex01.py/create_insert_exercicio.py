from defs_ex01.criar_conexao import criar_conexao
conn = criar_conexao()
try:
    cursor = conn.cursor()
    query_create = "CREATE TABLE jogos(id serial primary key, titulo varchar(255) not null, subtitulo varchar(255));"
    cursor.execute(query_create)
    conn.commit()
    query_insert =  """
                    INSERT INTO jogos(titulo, subtitulo)
                    VALUES
                        ('The legend of Zelda', 'Breath of the Wild'),
                        ('Final Fantasy VII', 'Remake'),
                        ('Dark Souls', 'Prepare to Die'),
                        ('Red Dead Redemption 2', 'A Wild West Saga'),
                        ('The Witcher 3', 'Wild hunt'),
                        ('God of War', 'Ragnarok'),
                        ('Hollow Knight', 'Silksong'),
                        ('Minecraft', 'Explore, Build, Survive'),
                        ('Cyberpunk 2077', 'Night City Awaits'),
                        ('Overwatch', 'Join the Fight');
                    """
    cursor.execute(query_insert)
    conn.commit()
    print("SUCESSO!")
except Exception as e:
    print(f"ERROR: {e}")
else:
    print("SUCESSO")
finally:
    cursor.close()
    conn.close()
