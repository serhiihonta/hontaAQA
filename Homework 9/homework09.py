"""
    1. Створіть класс з описом будь-якої тварини. Додайте 1 static method, 3 звичайних методи
    2. Створіть класс з описом будь-якої компанії чи організації. Додайте 1 classmethod, 3 звичайних методи
    3. Створіть декоратор, який виводить в консоль ім'я функції, яку було ввикликано. Наприклад, створіть
     пару функцій для аріфметичних операцій додавання і множення. При виклику цих функцій має повертатись результат
    операції і виводиться в консоль ім'я функції, яку було ввикликано.
    4. Створіть за допомогою list comprehension список, в якому буде 100 елементів, і кожен із яких буде в границях від
     1 до 10(для цього можна скористатись функцією randint із модуля random).
     Порахуйте кількість кожного елемента і виведіть в консоль
"""
import random

"""Task 1"""


class Kapibara:
    def __init__(self, weight, mood):
        self.weight = weight
        self.mood = mood

    @staticmethod
    def summary():
        return 'Kapibara is a friendly animal'

    def get_weight(self):
        return print(self.weight)

    def get_mood(self):
        return print(self.mood)

    def change_mood(self, state):
        if state == 0:
            self.mood = 'Happy'
        elif state == 1:
            self.mood = 'Angry'
        else:
            self.mood = 'Sleep'


john = Kapibara('medium', 'happy')

print(john.summary())
john.get_weight()
john.change_mood('wd')
john.get_mood()

"""Task 2"""


class Companyname:
    domain = 'agricultural'

    def __init__(self, name, workers, location):
        self.name = name
        self.workers = workers
        self.location = location

    @classmethod
    def change_domain(cls, new_domain):
        cls.domain = new_domain

    def get_name(self):
        return self.name

    def hire(self, add_workers):
        self.workers += add_workers
        return print(f"{add_workers} were hired. Total {self.workers} workers.")

    def fire(self, fire_workers):
        self.workers -= fire_workers
        return print(f"{fire_workers} were fired. Total {self.workers} workers.")

    def company_size(self):
        if self.workers < 50:
            print(f"{self.name} is a small company.")
        elif 51 <= self.workers < 100:
            print(f"{self.name} is a medium company.")
        else:
            print(f"{self.name} is big company.")


Companyname.change_domain('sales')
print(Companyname.domain)
company1 = Companyname('Amazing company', 70, 'Ukraine')

company1.fire(30)
company1.company_size()
company1.hire(50)
company1.company_size()


"""Task 3"""


def func_name(func):
    def inner(*args, **kwargs):
        print(f"The \"{func.__name__}\" function was called!")
        return func(*args, **kwargs)

    return inner


@func_name
def plus(a, b):
    return a + b


print(plus(2, 5))


"""Task 4"""


random_numbers = [random.randint(1, 10) for _ in range(100)]

counts = {number: random_numbers.count(number) for number in range(1, 11)}

for number, count in counts.items():
    print(f"{number} was generated {count} times")