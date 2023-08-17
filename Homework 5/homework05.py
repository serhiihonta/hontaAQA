"""
Напишіть програму на Python для знаходження перетину двох заданих масивів за допомогою лямбда.

Напишіть програму на Python, щоб перевірити, чи є заданий рядок числом, за допомогою лямбда

Напишіть програму на Python, щоб знайти список із максимальною та мінімальною довжиною за допомогою лямбда.
"""

"""Task 1"""

array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]

intersection = list(filter(lambda x: x in array1, array2))

print(f"Array intersection: {intersection}")

"""Task 2"""

is_digit = lambda x: all(char.isdigit() for char in x)

input_string = input("Input a string: ")

if is_digit(input_string):
    print("Entered string contains only digits.")
else:
    print("Entered string contains not only digits")

"""Task 3"""

text = input("Input a text: ")
words = text.split()

max_length = max(len(word) for word in words)
min_length = min(len(word) for word in words)

max_length_words = list(filter(lambda word: len(word) == max_length, words))
min_length_words = list(filter(lambda word: len(word) == min_length, words))

print("Max length words:", max_length_words)
print("Min length words:", min_length_words)



