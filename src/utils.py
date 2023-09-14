import psycopg2
from typing import Any

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
                    employer_name VARCHAR(255) NOT NULL,
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    url TEXT,
                    salary_from TEXT,
                    salary_to TEXT,
                    requirement VARCHAR(255),
                    responsibility VARCHAR(255),
                    experience VARCHAR(255),
                    date DATE
                )
            """)

    conn.commit()
    conn.close()

def save_data_to_database(data: list[dict[str, Any]], database_name: str, params: dict) -> None:
    """Сохранение данных канала и видео"""

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for job in data:



            cur.execute(
                """
                INSERT INTO hh (employer_name, id, name, url, salary_from,
                 salary_to, requirement, responsibility, experience, date)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,

                (job['employer_name'], job['id'], job['name'], f"https://www.hh.com/{job['url']}",
                 job['salary_from'], job['salary_to'], job['requirement'], job['responsibility'], job['experience'],
                 job['date'])
            )
        conn.commit()
        conn.close()
