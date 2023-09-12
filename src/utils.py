import psycopg2

def create_database(database_name: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных о каналах и видео."""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE hh (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                url TEXT,
                salary_from INTEGER DEFAULT 0,
                salary_to INTEGER DEFAULT 0,
                requirement VARCHAR(255),
                responsibility VARCHAR(255),
                experience VARCHAR(255),
                date DATE
            )
        """)

    conn.commit()
    conn.close()