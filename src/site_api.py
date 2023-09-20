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
        pass

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
