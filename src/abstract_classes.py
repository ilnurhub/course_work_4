from abc import ABC, abstractmethod


class APIManager(ABC):
    """
    Класс для работы с API сайтов
    """

    @abstractmethod
    def get_vacancies(self, keyword: str) -> dict:
        """
        Получает вакансии
        """
        pass


class FileManager(ABC):
    """
    Класс для работы с файлами
    """
    pass
