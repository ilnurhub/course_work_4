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
    Возвращает отфильтрованные по ключевым словам вакансии
    """
    list_of_filtered_vacancies = []
    for vacancy in vacancies:
        filter_word_count = 0
        for filter_word in filter_words:
            if filter_word.lower() in vacancy.vacancy_data['description/requirement'].lower():
                filter_word_count += 1
        if filter_word_count == len(filter_words):
            list_of_filtered_vacancies.append(vacancy)
    return list_of_filtered_vacancies


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
