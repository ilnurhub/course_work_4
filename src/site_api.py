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
        for vacancy in self.vacancies_list:
            if vacancy['salary'] is None:
                salary_min = 0
                salary_max = 0
            else:
                salary_min = vacancy['salary']['from'] if vacancy['salary']['from'] is not None else 0
                salary_max = vacancy['salary']['to'] if vacancy['salary']['from'] is not None else 0
            formatted_vacancy = {
                'name': vacancy['name'],
                'url': vacancy['alternate_url'],
                'salary_min': salary_min,
                'salary_max': salary_max,
                'requirement': vacancy['snippet']['requirement']
            }
            self.formatted_vacancies.append(formatted_vacancy)
        return self.formatted_vacancies


class SuperJobAPI(APIManager):
    """
    Класс для работы с сайтом https://www.superjob.ru/
    """

    def get_vacancies(self, keyword: str) -> dict:
        pass

    def format_data(self):
        pass
