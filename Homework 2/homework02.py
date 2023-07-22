"""Задача 1. В змінній minute лежит число от 0 до 59, згенероване випадковим чином.
Визначте в якій четверті години попадає це число (в першій, другій, третій чи четвертій).


Задача 2. В змінній birth_month запишіть номер місяця вашого народження (дані введіть з консолі).
В залежності від введених даних виведіть характеристику для відповідної пори року:

Зима - За вікном падав сніг.

Весна - Все довкола розцвітало.

Літо - Діти насолоджувались літніми канікулами.

Осінь - Все довкола загоралось яскравими фарбами.

Задача 3. За введеними координатами з'ясувати, до якої координатної чверті належить точка.
( Координати ввести з консолі, варто зауважити, що це можуть бути не лише цілі числа.
Опрацювати варіант, коли точка- початок координат або лежить на осі )
Намалюйте блок-схему до даної задачі і прикріпіть зображення до домашнього завдання."""

"""Task 1"""
import random

minute = random.randint(0, 60)
if minute < 15:
    print("First quarter")
elif 15 < minute < 30:
    print("Second quarter")
elif 30 < minute < 45:
    print("Third quarter")
else:
    print("Fourth quarter")
print(minute)

"""Task 2"""

birthMonth = input("> ")

winter = ["december", "january", "february"]
spring = ["march", "april", "may"]
fall = ["september", "october", "november"]
summer = ["june", "july", "august"]
if birthMonth.lower() in winter:
    print("Зима - За вікном падав сніг")
elif birthMonth.lower() in spring:
    print("Весна - Все довкола розцвітало.")
elif birthMonth.lower() in summer:
    print("Літо - Діти насолоджувались літніми канікулами")
elif birthMonth.lower() in fall:
    print("Осінь - Все довкола загоралось яскравими фарбами.")
else:
    print("Please, enter your birth month.")

"""Task 3"""

x = float(input("Enter the coordinate X: "))
y = float(input("Enter the coordinate Y: "))
if x == 0 and y == 0:
    print("The origin")
elif x == 0:
    print("The point lies on the Y axis")
elif y == 0:
    print("The point lies on the X axis")
elif x > 0 and y > 0:
    print("The point belongs to the first coordinate quarter")
elif x < 0 and y > 0:
    print("The point belongs to the second coordinate quarter")
elif x < 0 and y < 0:
    print("The point belongs to the third coordinate quarter")
else:
    print("The point belongs to the fourth coordinate quarter")