class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, vacancy_data: dict):
        self.vacancy_data = self.validate_data(vacancy_data)

    def validate_data(self, vacancy_data: dict):
        """
        Валидирует данные вакансии
        """
        if not isinstance(vacancy_data['name'], str):
            vacancy_data['name'] = '-'
        if not isinstance(vacancy_data['url'], str):
            vacancy_data['url'] = '-'
        if not isinstance(vacancy_data['salary_min'], int):
            vacancy_data['salary_min'] = 0
        if not isinstance(vacancy_data['salary_max'], int):
            vacancy_data['salary_max'] = 0
        if not isinstance(vacancy_data['description/requirement'], str):
            vacancy_data['description/requirement'] = '-'
        return vacancy_data

    def calculate_average_salary(self, salary_min: int, salary_max: int) -> int:
        """
        Вычисляет среднюю зарплату
        """
        return (salary_min + salary_max) // 2
