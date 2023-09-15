from abc import ABC, abstractmethod
import requests
from datetime import datetime

class APIJob(ABC):

    @abstractmethod
    def __init__(self, keyword: str) -> None:
        self.keyword = keyword


    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def get_formatted(self):
        pass

#############


class ApiHH(APIJob):
    """ Класс для работы с конкретной платформой HeadHunter"""
    url = 'https://api.hh.ru/vacancies'
    def __init__(self, employer_id):
        self.employer_id = employer_id

        self.params = { # Справочник для параметров GET-запроса
            #'text': f'NAME:{self.keyword}',  # Текст фильтра.
            'employer_id': employer_id,  # Поиск по ID работодателей из списка
            'area': 1,  # Поиск осуществляется по вакансиям города
            'page': 0,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        self.vacancies = []


    def get_vacancies(self):
        """ Метод выполняющий запрос"""
        req = requests.get(self.url, self.params)  # Посылаем запрос к API
        data = req.json()

        return data.get('items', [])

    def get_formatted(self, data):
        """ Получение стандартного списка"""

        for i in data:
            dict_hh = {
                'employer_name': i['employer']['name'],
                'id': i['id'],  # id вакансии
                'name': i['name'],  # Название вакансии
                'url': i['url'],  # Ссылка на вакансию
                'salary_from': i['salary']['from'] if i['salary']  else 0,  # Зарплата от
                'salary_to': i['salary']['to'] if i['salary'] else 0,  # Зарплата до
                'requirement': i['snippet']['requirement'],  # Требования
                'responsibility': i['snippet']['responsibility'],  # Обязанности
                'experience': i['experience']['name'],  # Опыт
                'date': datetime.strptime(i['published_at'], '%Y-%m-%dT%H:%M:%S%z').strftime('%d %B %Y'),
            }
            self.vacancies.append(dict_hh)
        return self.vacancies
