from abstract_classes import APIManager
import requests


class HeadHunterAPI(APIManager):
    """
    Класс для работы с сайтом https://hh.ru/
    """

    def __init__(self):
        self.vacancies_list = None
        self.formatted_vacancies = []

    def get_vacancies(self, keyword: str) -> list:
        params = {
            'text': f'name:{keyword}',  # Текст фильтра. В имени должно быть  ключевое слово
            'area': 1,  # Поиск ощуществляется по вакансиям города Москва
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        responce = requests.get('https://api.hh.ru/vacancies', params=params)
        vacancies = responce.json()
        self.vacancies_list = vacancies['items']
        result = self.format_data()
        return result

    def format_data(self):
        pass


class SuperJobAPI(APIManager):
    """
    Класс для работы с сайтом https://www.superjob.ru/
    """

    def get_vacancies(self, keyword: str) -> dict:
        pass

    def format_data(self):
        pass
