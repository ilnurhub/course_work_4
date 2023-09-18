from abstract_classes import APIManager


class HeadHunterAPI(APIManager):
    """
    Класс для работы с сайтом https://hh.ru/
    """

    def get_vacancies(self, keyword: str) -> dict:
        pass

    def format_data(self):
        pass
