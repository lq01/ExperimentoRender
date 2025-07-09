import psycopg2

conexao = psycopg2.connect(
            dbname="experimentodb",
            user="experimentodb_user",
            password="QpZyNprNbfLSB3DF613YiRb9dulneftu",
            host="dpg-d1mu0mre5dus7388ul60-a",
            port="5432",
        )



with conexao as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Execute a command: this creates a new table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS test (
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