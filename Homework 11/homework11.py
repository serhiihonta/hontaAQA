"""Опишіть об'єкти мистецтва для музею. скористайтесь всіма 5 принципами: абстракція, наслідування, поліморфізм, скриття,
 інкапсуляція. додайте property, setter. Створіть хоча-б по одному інстансу кожного класу і викличте методи"""

from abc import ABC


class ArtObject(ABC):
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value >= 0:
            self._value = new_value
        else:
            print("The value should be positive number.")

    def info(self):
        return f"{self.year}, {self.artist}: '{self.title}')"


class Painting(ArtObject):
    def __init__(self, title, artist, year, style):
        super().__init__(title, artist, year)
        self.style = style

    def info(self):
        return super().info() + f", {self.style} painting"


class Sculpture(ArtObject):
    def __init__(self, title, artist, year, material):
        super().__init__(title, artist, year)
        self.material = material

    def info(self):
        return super().info() + f", made of {self.material}"


class Photograph(ArtObject):
    def __init__(self, title, artist, year, camera):
        super().__init__(title, artist, year)
        self.camera = camera

    def info(self):
        return super().info() + f", {self.camera} camera."


sunflowers = Painting("Sunflowers", "Vincent van Gogh", 1888, "oil on wood")
david = Sculpture("David", "Michelangelo", 1504, "marble")
tankman = Photograph("Tank Man", "Jeff Widener", 1989, "Nikon FE2")

print(sunflowers.info())
print(david.info())
print(tankman.info())

sunflowers.value = 42000
print(f"Cost of'{sunflowers.title}': ${sunflowers.value}.")

david.value = -5000
