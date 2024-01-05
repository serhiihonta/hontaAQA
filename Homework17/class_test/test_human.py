from Homework17.pytest_exp import Human


class TestHuman:

    def setup_class(self):
        print('setup for class')

    def setup(self):
        self.human = Human('Alf', 12, 'red')

    def test_check_age(self):
        self.human.grow()
        assert self.human.age == 13

    def test_hair_color_change(self):
        self.human.change_colour('black')
        assert self.human.color == 'black'

    def teardown_method(self):
        print('trdwn')

    def teardown_class(self):
        print('It\'s teardown class')
