import datetime

class Traffic_light:

    numbers_someone_called_height = []
    def __init__(self):
        self.__color = 'Green'

    def __str__(self):
        return f'I\'m traff lisht and curr state is {self.__color}'

    def __repr__(self):
        return 'Traffic_light()'

    def __getattr__(self, item):
        return f'this is not {item} you are looking for'
    def __getattribute__(self, item):
        if item.startswith('height'):
            Traffic_light.numbers_someone_called_height.append(datetime.datetime.now())
        return super().__getattribute__(item)

traffic_light_1 = Traffic_light()
print(traffic_light_1)
#traffic_light_2 = eval(repr(traffic_light_1))
#print(traffic_light_2)
print(traffic_light_1.height)

class Horse:

    def __init__(self):
        self.speed = 5
        self.age = 4


    def __add__(self, other):
        print(type(other))
        #if other.__class__.__name__.startswith('Horse'):
        if type(other) == Horse:
            return Horse()
        else:
            return Mul(other.strength, self.speed)

    #def __radd__(self, other):
    #    return Mul(other.strength, self.speed)

    def __del__(self):
        print("deleted")
class Donkey:

    def __init__(self):
        self.strength = 10
        self.age = 5

class Mul:
    def __init__(self, strength, speed):
        self.strength = strength
        self.speed = speed

    def __str__(self):
        return f'{self.__class__.__name__}\n{self.speed}\n{self.strength}'

horse = Horse()
donkey = Donkey()
mul = horse + donkey
print(mul)
del horse
horse2 += donkey
print(horse2)