"""
Напишіть програму яка перевіряє чи стрічка містить лише великі і малі літери, числа та нижнє підкреслення.

Напишіть програму, що видаляє область дужок в стрічці

["example (.com)", "github (.com)", "stackoverflow (.com)"] ->

example

github

stackoverflow

Напишіть програму, що. вставляє пробіл перед великою літерою
"""

"""Task 1"""


def check_string(x):
    valid_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")

    for char in x:
        if char not in valid_characters:
            return False
    return True


input_string = input("Enter chars:")
if check_string(input_string):
    print('Chars are valid!')
else:
    print('Non valid chars!')


"""Task 2"""


def remove_parentheses(x):
    result = ""
    temporary = []

    for char in x:
        if char == '(':
            temporary.append('(')
        elif char == ')':
            if temporary:
                temporary.pop()
            else:
                result += char
        else:
            if not temporary:
                result += char

    return result


input_string = input("Enter a string with parentheses: ")
modified_string = remove_parentheses(input_string)
print("Result:", modified_string)


"""Task 3"""


def insert_space(x):
    result = ""
    for char in x:
        if char.isupper():
            result += " " + char
        else:
            result += char
    return result


input_string = input("Enter a string: ")
modified_string = insert_space(input_string)
print("Result:", modified_string)
