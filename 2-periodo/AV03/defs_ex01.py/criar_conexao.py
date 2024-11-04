import psycopg2

def criar_conexao():
    try:
        conn = psycopg2.connect(
            dbname = "exercicio1",
            user = 'postgres',
            password = '123456',
            host = 'localhost',
            port = '5432'
        )
        return conn
    
    except Exception as e:
        print(f"DEU PAU: {e}")
        return None
