"""
    Реалізуйте біблиотеку з будь-яким функціоналом. Наприклад, створіть функції для арифметичних операцій і побудуйте каскад
    імпортів з декількох packagів. Має бути можливіcть імпортувати деякі функції з пакета, але не всі.
    Створіть обробку одного будь-якого exception, який не використався як приклад на занятті. Виведіть результат в консоль
    Реалізуйте функцію, яка додає або віднімає від заданої дати певну кількість днів. Приймає на вхід будь-яку дату
    та час (datetime), а також значення днів(int), і знак(True або False, які репрезентують + і -).
    Повертає datetime. В цій задачі скористайтесь datetime.timedelta
    Реалізуйте функцію, яка вираховує ваш точний вік(не обов'язково вказувати свої данні), вираховуючі різницю між
    наданим значеням і значенням datetime.now(). Приймає дату та час(datetime), повертає два значення: datetime і datetime.timestamp.
    В цій задачі скористайтесь для конвертації datetime.timestamp. Виведіть результат в консоль
"""

"""Task 1"""

from dir1 import umnozhit

print(umnozhit(10, 12))

"""Task 2"""


def reverse_string(string):
    if not string:
        return "Empty string!"
    reversed_str = string[::-1]
    return reversed_str


str = ""
result = reverse_string(str)
print(result)

"""Task 3"""

from datetime import datetime, timedelta


def change_date(input_date, days, add=True):
    if add:
        new_date = input_date + timedelta(days=days)
    else:
        new_date = input_date - timedelta(days=days)
    return new_date


input_date = datetime(2023, 9, 6)
days_to_change = 42
add_days = True

modified_date = change_date(input_date, days_to_change, add=add_days)
print(modified_date)

"""Task 4"""


def find_age(birthdate):
    current_datetime = datetime.now()
    age = current_datetime - birthdate
    age_timestamp = age.total_seconds()
    return age, age_timestamp

birthdate = datetime(1989, 12, 17)
age, age_timestamp = find_age(birthdate)

print(f"Current age: {age}")
print(f"Current age in timestamp: {age_timestamp}")
