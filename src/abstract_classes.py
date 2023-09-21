from abc import ABC, abstractmethod


class APIManager(ABC):
    """
    Класс для работы с API сайтов
    """

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list:
        """
        Получает вакансии
        """
        pass

    @abstractmethod
    def format_data(self):
        """
        Приводит пришедшие по API данные к единому формату:
        {'name': 'название вакансии',
        'url': 'ссылка на вакансию',
        'salary_min': 'минимальная зарплата',
        'salary_max': 'максимальная зарплата',
        'description/requirement': 'описание или требования'}
        """
        pass


class FileManager(ABC):
    """
    Класс для работы с файлами
    """

    @abstractmethod
    def write(self, data):
        """
        Запись в файл
        """
        pass

    def read(self):
        """
        Чтение из файла
        """
        pass

    def delete(self):
        """
        Удаление данных
        """
        pass
