"""
Опишіть класс будь-якого транспортного засобу. Скористайтесь двома рівнями наслідування і абстракцією за допомогою ABC
(використання ABC не рахується за рівень наслідування)
"""
from abc import ABC, abstractmethod


class RidingAnimals(ABC):
    def __init__(self, food, maxspeed, maxlift):
        self.food = food
        self.maxspeed = maxspeed
        self.maxlift = maxlift

    @abstractmethod
    def feeding(self):
        pass


class Reptiles(RidingAnimals):
    feed = 'meat'

    def __init__(self, food, maxspeed, maxlift):
        super().__init__(food, maxspeed, maxlift)

    def feeding(self):
        if self.food == 'meat':
            print(f"The riding animal is fed and can move with {self.maxspeed} and lift {self.maxlift} weight.")
        else:
            print(f"Feed your transport with {Reptiles.feed}!")


class Horses(RidingAnimals):
    feed = 'grass'

    def __init__(self, food, maxspeed, maxlift):
        super().__init__(food, maxspeed, maxlift)

    def feeding(self):
        if self.food == 'grass':
            print(f"The riding animal is fed and can move with {self.maxspeed} and lift {self.maxlift} weight.")
        else:
            print(f"Feed your transport with {Horses.feed}!")


class Serpent(Reptiles):
    def __init__(self, food, maxspeed, maxlift):
        super().__init__(food, maxspeed, maxlift)


class Unicorn(Horses):
    def __init__(self, food, maxspeed, maxlift):
        super().__init__(food, maxspeed, maxlift)


snake = Serpent('meatй', 32, 10)
unicorn = Unicorn('grass', 44, 40)
print(snake.feed)
snake.feeding()
print(unicorn.feed)
unicorn.feeding()
