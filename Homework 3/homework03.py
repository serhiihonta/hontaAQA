"""
Написати програму, для введення та перегляду нотаток. Програма пропонує користувачу вводити ключові слова, та опрацьовує їх.
Перелік ключових слів:

    add - додати нотатку. Користувач вводить текст нотатки, який зберігається у програмі та є дійсним до її завершення
    earliest - виводить збережені нотатки у хронологічному порядку - від найстарішої до найновішої
    latest - виводить збережені нотатки у хронологічному порядку - від найновішої до найстарішої
    longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
    shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої
    Exit - вихід


Приклад:

> add  > Введіть нотатку: this is note
> add  > Введіть нотатку: this is notissimo
> add  > Введіть нотатку: note
> add > Введіть нотатку: this is a huge long, insanely long note
> add > Введіть нотатку: well, anyways
> earliest > Від найновішої до найпізнішої:
> this is note > this is notissimo > note > this is a huge long, insanely long note > well, anyways
> latest > Від найпізнішої до найновішої:
> well, anyways > this is a huge long, insanely long note > note > this is notissimo > this is note
> longest > Від найдовшої до найкоротшоЇ:
> this is a huge long, insanely long note > this is notissimo> well, anyways > this is note > note
> shortest > Від найкоротшої до найдовшої:
> note > this is note > well, anyways > this is notissimo > this is a huge long, insanely long note
"""

notes = []

while True:
    print("""
    Select an action:
    add -- add a note;
    earliest -- show notes from oldest to newest;
    latest -- show notes from newest to oldest;
    longest -- show notes fron longest to shortest;
    shortest -- show notes from shortest to longest;
    exit -- exit
    """)

    action = input("Input an action: ")

    if action == 'add':
        newNote = input("Enter a note: ")
        notes.append(newNote)

    elif action == 'earliest':
        for note in notes:
            print(note)

    elif action == 'newest':
        for note in reversed(notes):
            print(note)

    elif action == 'longest':
        sortedNotes = sorted(notes, key=len, reverse=True)
        for note in sortedNotes:
            print(note)

    elif action == 'shortest':
        sortedNotes = sorted(notes, key=len)
        for note in sortedNotes:
            print(note)

    elif action == 'exit':
        break

    else:
        print("Wrong option, select once more.")