"""
Для всіх трьох задач скористайтесь написанням функцій. В межах розумного робіть функції невеликими за розміром і перевикористовуйте код.


1.Дано два списки чисел. Знайдіть всі числа, що зустрічаються як в першому, так і другому списках, і надрукуйте їх у порядку зростання.
2.Створіть словник із даними про студентів: ключі - імена студентів, значення - бали для кожного.
Програма повинна визначити середній бал і вивести імена студентів, чий бал вище середнього.
3.Створіть списки із значеннями для name, surname, location, наприклад name = ['Alex', 'John', 'Simba'].
напишіть програму, яка створює словники з даними випадкових людей на основі ваших списків, роздрукуйте результат.
для випадковості значень скористайтесь модулем random. приклад згенерованого словника:
{'name':'Liza', 'surname':'Djoconda', 'location':'Florence'}
"""

"""Task 1"""

firstList = [1, 2, 3, 4, 5]
secondList = [4, 5, 6, 7, 8, 1]


def finddistinct(a, b):
    """Find common elements in lists"""
    setone = set(a)
    settwo = set(b)
    common = sorted(setone.intersection(settwo))
    print(common)


finddistinct(firstList, secondList)

"""Task 2"""

students = {'Oksana': 15, 'Kolya': 22, 'Dima': 6, 'Natasha': 11}


def average(dict):
    """Find average"""
    total_sum = sum(dict.values())
    total_len = len(dict)
    average = total_sum / total_len
    return average


def above_average(dict, average):
    """Create a list above average values"""
    above_avg_students = []
    for name, score in dict.items():
        if score > average:
            above_avg_students.append((name, score))
    return above_avg_students


avg_score = average(students)
above_avg = above_average(students, avg_score)
print(f"The average score is {avg_score}. Students with score above average: {above_avg}")

"""Task 3"""

import random

name_list = ['Oksana', 'Kolya', 'Igor', 'Natasha']
surname_list = ['Nikolaev', 'Oksanova', 'Igorev', 'Natashich']
locations_list = ['Chernihiv', 'Nizhin', 'Priluky', 'Snovsk']


def create_random_people():
    """Create a random set of personal data from lists"""
    random_name = random.choice(name_list)
    random_surname = random.choice(surname_list)
    random_location = random.choice(locations_list)

    person = {'name': random_name, 'surname': random_surname, 'location': random_location}
    return person


number_people = 6

for i in range(number_people):
    random_people = create_random_people()
    print(random_people)