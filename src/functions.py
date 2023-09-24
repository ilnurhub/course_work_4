def choice():
    """
    Возвращает значение, выбранное пользователем
    """
    user_choice = input("""
Выберите цифру:
1 - поиск ваканский на HeadHunter
2 - поиск вакансий на SuperJob
0 - выход
""")
    return user_choice


def filter_vacancies(vacancies, filter_words):
    """
    Возраващает отфильтрованные по ключевым словам вакансии
    """
    pass


def sort_vacancies(vacancies):
    """
    Возвращает отсортированные вакансии
    """
    sorted_vacancies = sorted(vacancies, key=lambda x: x.average_salary, reverse=True)
    return sorted_vacancies


def get_top_vacancies(vacancies, top_n):
    """
    Возвращает заданное количество вакансий
    """
    pass
