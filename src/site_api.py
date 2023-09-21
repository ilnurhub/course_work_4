from abstract_classes import APIManager
import requests
from config import SJ_API_KEY


class HeadHunterAPI(APIManager):
    """
    Класс для работы с сайтом https://hh.ru/
    """

    def __init__(self):
        self.unformatted_data = []
        self.formatted_data = []

    def get_vacancies(self, keyword: str) -> list:
        page = 0
        while page < 5:
            params = {
                'text': f'name:{keyword}',  # Текст фильтра. В имени должно быть  ключевое слово
                'page': page,  # Номер страницы
                'per_page': 100  # Кол-во вакансий на 1 странице
            }
            responce = requests.get('https://api.hh.ru/vacancies', params=params)
            if responce.status_code == 400:
                break
            data = responce.json()['items']
            self.unformatted_data.extend(data)
            page += 1
        result = self.format_data()
        return result

    def format_data(self):
        for item in self.unformatted_data:
            if item['salary'] is None:
                salary_min = 0
                salary_max = 0
            else:
                salary_min = item['salary']['from'] if item['salary']['from'] is not None else 0
                salary_max = item['salary']['to'] if item['salary']['to'] is not None else 0
            formatted_item = {
                'name': item['name'],
                'url': item['alternate_url'],
                'salary_min': salary_min,
                'salary_max': salary_max,
                'requirement': item['snippet']['requirement']
            }
            self.formatted_data.append(formatted_item)
        return self.formatted_data


class SuperJobAPI(APIManager):
    """
    Класс для работы с сайтом https://www.superjob.ru/
    """
    def __init__(self):
        self.unformatted_data = []
        self.formatted_data = []

    def get_vacancies(self, keyword: str) -> list:
        header = {
            'X-Api-App-Id': SJ_API_KEY}
        page = 0
        while page < 5:
            params = {
                'page': page,
                'count': 100
            }
            responce = requests.get(
                f'https://api.superjob.ru/2.0/vacancies/?keywords%5B0%5D%5Bkeys%5D=&keywords%5B1%5D%5Bsrws%5D=1&'
                f'keywords%5B1%5D%5Bskwc%5D=and&keywords%5B1%5D%5Bkeys%5D={keyword}',
                params=params, headers=header)
            data = responce.json()['objects']
            self.unformatted_data.extend(data)
            page += 1
        result = self.format_data()
        return result

    def format_data(self):
        for item in self.unformatted_data:
            formatted_item = {
                'name': item['profession'],
                'url': item['link'],
                'salary_min': item['payment_from'],
                'salary_max': item['payment_to'],
                'requirement': item['vacancyRichText']
            }
            self.formatted_data.append(formatted_item)
        return self.formatted_data
