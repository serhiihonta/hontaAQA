import pytest

from Homework18.code_for_testing import Human


@pytest.mark.xfail(reason='failed due to known bug')
def test_change_hair_color():
    human = Human('Abelard', 62, 'grey')
    human.change_colour('pink')
    assert human.color == 'pink'


@pytest.mark.smoke
def test_age_growth(human):
    human.grow()
    assert human.age == 63


@pytest.mark.parametrize(
    "color,expected", [('black', 'black'), ('white', 'white')], ids=['change to black', 'change to white']
)
def test_change_hair_color2(human, color, expected):
    human.change_colour(color)
    assert human.color == expected


def test_check_raise_for_exeption(human):
    with pytest.raises(Exception):
        human.change_colour('red')
