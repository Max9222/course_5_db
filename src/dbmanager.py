import psycopg2
from typing import Any

class DBManager:

    def __init__(self, database_name: str, table_name: str, params: dict):

        self.conn = psycopg2.connect(dbname=database_name, **params)
        self.cur = self.conn.cursor()
        self.table_name = table_name


    def get_companies_and_vacancies_count(self) -> list[(str, Any)]:
        """Получает список всех компаний и количество вакансий у каждой компании."""
        with self.conn:
            self.cur.execute(
                f"SELECT  employer_name, COUNT (*) FROM {self.table_name} GROUP BY employer_name;")
            data = self.cur.fetchall()
            return data


    def get_all_vacancies(self) -> list[(str, Any)]:
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию."""
        with self.conn:
            self.cur.execute(
                f"SELECT  id, employer_name, salary_from, salary_to, url name FROM {self.table_name};")
            data = self.cur.fetchall()
            return data


    def get_avg_salary(self) -> list[(str, Any)]:
        """Получает среднюю зарплату по вакансиям."""
        with self.conn:
            self.cur.execute(
                f"SELECT  ROUND(AVG(salary_from), 0) FROM {self.table_name};")
            data = self.cur.fetchall()
            return data


    def get_vacancies_with_higher_salary(self) -> list[(str, Any)]:
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        with self.conn:
            self.cur.execute(
                f"SELECT name FROM {self.table_name} WHERE salary_from > (SELECT AVG(salary_from) FROM {self.table_name});")
            data = self.cur.fetchall()
            return data


    def get_vacancies_with_keyword(self, word: str) -> list[(str, Any)]:
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python."""
        with self.conn:
            self.cur.execute(
                f"SELECT name FROM {self.table_name} WHERE name LIKE '%{word}%';")
            data = self.cur.fetchall()
            return data
