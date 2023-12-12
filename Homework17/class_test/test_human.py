from Homework17.pytest_exp import Human


class TestHuman:
    def setup(self):
        print('setup_ttt')
    def test_check_age(self):
        human = Human('Alf', 12, 'red')
        human.grow()
        assert human.age == 13

    def test_hair_color_change(self):
        human = Human('Alf', 12, 'red')
        human.change_colour('black')
        assert human.color == 'black'

    def teardown(self):
        print('trdwn')
