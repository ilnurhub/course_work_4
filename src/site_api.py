from abstract_classes import APIManager
import requests


class HeadHunterAPI(APIManager):
    """
    Класс для работы с сайтом https://hh.ru/
    """

    def __init__(self):
        self.data_list = []
        self.formatted_data = []

    def get_vacancies(self, keyword: str) -> list:
        page = 0
        while page < 21:
            params = {
                'text': f'name:{keyword}',  # Текст фильтра. В имени должно быть  ключевое слово
                'page': page,  # Номер страницы
                'per_page': 100  # Кол-во вакансий на 1 странице
            }
            responce = requests.get('https://api.hh.ru/vacancies', params=params)
            if responce.status_code == 400:
                break
            data = responce.json()['items']
            self.data_list.extend(data)
            page += 1
        result = self.format_data()
        return result

    def format_data(self):
        for item in self.data_list:
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

    def get_vacancies(self, keyword: str) -> dict:
        pass

    def format_data(self):
        pass

