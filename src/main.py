from site_api import HeadHunterAPI, SuperJobAPI
from vacancy import Vacancy
from file_manager import JSONFileManager
from functions import choice, filter_vacancies, sort_vacancies, get_top_vacancies


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    user_choice = choice()
    while user_choice not in ('0', '1', '2'):
        print('Неверный ввод')
        user_choice = choice()

    if user_choice == '1':
        platform = HeadHunterAPI()
    elif user_choice == '2':
        platform = SuperJobAPI()
    else:
        print('Bye')
        return

    search_query = input("Введите поисковый запрос: ")
    list_of_data = platform.get_vacancies(search_query)

    if len(list_of_data) == 0:
        print('По вашему запросу ничего не найдено')
        return

    json_file = JSONFileManager()
    json_file.write(list_of_data)

    list_of_vacancy_data = json_file.read()
    list_of_vacancies = []

    for vacancy_data in list_of_vacancy_data:
        vacancy = Vacancy(vacancy_data)
        list_of_vacancies.append(vacancy)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите через пробел ключевые слова для фильтрации вакансий: ").split()
    print()

    filtered_vacancies = filter_vacancies(list_of_vacancies, filter_words)
    if len(filtered_vacancies) == 0:
        print('Нет вакансий, соответствующих заданным критериям.')
        return

    sorted_list_of_vacancies = sort_vacancies(filtered_vacancies)

    top_vacancies = get_top_vacancies(sorted_list_of_vacancies, top_n)

    for vacancy in top_vacancies:
        print(f"Название: {vacancy.vacancy_data['name']}")
        print(f"Ссылка на вакансию: {vacancy.vacancy_data['url']}")
        if vacancy.vacancy_data['salary_max'] != 0:
            if vacancy.vacancy_data['salary_min'] != 0:
                print(f"Зарплата: от {vacancy.vacancy_data['salary_min']} до {vacancy.vacancy_data['salary_max']}")
            else:
                print(f"Зарплата: до {vacancy.vacancy_data['salary_max']}")
        else:
            if vacancy.vacancy_data['salary_min'] != 0:
                print(f"Зарплата: от {vacancy.vacancy_data['salary_min']}")
            else:
                print(f"Зарплата: не указана")
        print(f"Описание: {vacancy.vacancy_data['description/requirement']}")
        print('---------------------------------------------')
    return


if __name__ == '__main__':
    user_interaction()
