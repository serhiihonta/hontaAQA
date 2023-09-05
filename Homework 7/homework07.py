"""
Всі задачі оформити як окремі ф-ції

1. Написати функцію, яка отримує у вигляді параметра ім'я файлу назви інтернет доменів (domains.txt) та повертає
їх у вигляді списку рядків (назви повертати без крапки).

2. Написати функцію, яка отримує у вигляді параметра ім'я файлу (names.txt) і повертає список усіх прізвищ з нього.
 Кожен рядок файлу містить номер, прізвище, країну. Файл створити власноруч і записати туди дані

3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) і повертає список словників виду {"date": date}
 у яких date - це дата з рядка (якщо є), Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]
"""

"""Task 1"""


def read_domains(filename):
    domains = []

    with open(filename, "r") as file:
        for line in file:
            domain = line.strip()
            domain = domain.replace(".", "")
            domains.append(domain)
    return domains


filename = "domains.txt"
# domain_list = read_domains(filename)
# print("Domain list:", domain_list)

"""Task 2"""


def get_last_names(file_name):
    last_names = []

    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            if len(parts) >= 2:
                last_name = parts[1]
                last_names.append(last_name)

    return last_names


file_name = 'names.txt'
last_names_list = get_last_names(file_name)
print(last_names_list)


"""Task 3"""


def extract_dates_from_file(file_name):
    result = []
    current_month = None

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.title() == line:
                current_month = line
            else:
                parts = line.split(' - ')
                if len(parts) == 2:
                    date = parts[0]
                    event = parts[1]
                    if current_month:
                        result.append({"date": date})

    return result


file_name = 'authors.txt'
dates_list = extract_dates_from_file(file_name)
print(dates_list)
