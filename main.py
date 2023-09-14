from src.api_hh import ApiHH
from src.config import config
from src.utils import create_database, save_data_to_database
from src.dbmanager import DBManager

def main():

    employer_id = [
        '3428160', '4872201', '10091282', '999442',
        '9895883', '865', '5178281', '1362151',
        '5992859', '4576177'
    ]       # Id 10 работодателй

    params = config()

    hh = ApiHH(employer_id)
    vac_hh = hh.get_vacancies()
    #print(vac_hh)
    list_hh = hh.get_formatted(vac_hh)  # подгоняем под удобрый формат
    #print(list_hh)

    create_database('hh', params)   # Создаем таблицу

    save_data_to_database(list_hh, 'hh', params)  # Заполняем таблицу


if __name__ == '__main__':
    main()
