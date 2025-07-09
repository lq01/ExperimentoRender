import psycopg2

conexao = psycopg2.connect(
            dbname="DBJulhoExperimento",
            user="postgres",
            password="luique1810",
            host="localhost",
            port="5432",
        )


def criarBanco():
    with conexao as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            # Execute a command: this creates a new table
            cur.execute("""
                CREATE TABLE test (
                    id serial PRIMARY KEY,
                    nome text)
                """)

            # Make the changes to the database persistent
            conn.commit()

def registrarNome(nome):

    with conexao as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO test (nome) VALUES (%s)", (nome,))
        conexao.commit()