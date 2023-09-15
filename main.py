from src.api_hh import ApiHH
from src.config import config
from src.utils import create_database, save_data_to_database
from src.dbmanager import DBManager

def main():

    employer_id = [
        '3428160', '4872201', '10091282', '999442',
        '9895883', '865', '5178281', '1362151',
        '5992859', '4576177'
    ]       # Id 10 работодателей

    params = config()

    db = 'hh'   # Название Базы Данных
    table_name = 'hh'   # Название таблицы

    hh = ApiHH(employer_id)
    vac_hh = hh.get_vacancies()
    #print(vac_hh)
    list_hh = hh.get_formatted(vac_hh)  # подгоняем под удобный формат
    #print(list_hh)

    create_database(db, params)   # Создаем таблицу

    save_data_to_database(list_hh, db, params)  # Заполняем таблицу

    dbmanager = DBManager(db, table_name, params)

    list_1 = dbmanager.get_companies_and_vacancies_count()
    print('Cписок всех компаний и количество вакансий у каждой компании')
    print(list_1)
    print()

    print('Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.')
    list_2 = dbmanager.get_all_vacancies()
    print(list_2)
    print()

    print('Получает среднюю зарплату по вакансиям')
    list_3 = dbmanager.get_avg_salary()
    print(list_3)
    print()

    print('Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям')
    list_4 = dbmanager.get_vacancies_with_higher_salary()
    print(list_4)
    print()

    print('Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python')
    list_5 = dbmanager.get_vacancies_with_keyword('python')
    print(list_5)

if __name__ == '__main__':
    main()
