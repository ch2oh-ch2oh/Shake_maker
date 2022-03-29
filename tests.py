import pytest
from pytest_mock import MockerFixture

import apps
from apps import Cocktails


@pytest.fixture(autouse=True)
def clean_cocktails():
    apps.cocktails = []


def test_read__correct_data(mocker: MockerFixture):
    test_file = """ Коктейль Пиранья
3
Водка – 37 мл (6 ч. л.)
ликер, коричневый – 25 мл (1,5 ст. л.)
Кола, сильно охлажденная – 25 мл (1,5 ст. л.)
Влейте спиртное в низкий стакан, заполненный большим количеством колотого льда. Хорошо размешайте. Затем добавьте колу.
Коктейль Оазис
3
Джин – 50 мл (3 ст. л.)
Ликер «Кюрасао» голубой – 12 мл (2 ч. л.)
Тоник – 100 мл
Влейте джин в стакан, наполовину заполненный колотым льдом. Добавьте Кюрасао, влейте тоник и перемешайте. Украсьте долькой лимона и веточкой мяты.
"""

    mocker.patch('builtins.open', mocker.mock_open(read_data=test_file))
    c=Cocktails()
    assert len(c.cocktails) == 2
    assert all([isinstance(r, Cocktails.Cocktail) for r in c.cocktails])


def test_read__empty_data(mocker: MockerFixture):
    test_file = """"""

    mocker.patch('builtins.open', mocker.mock_open(read_data=test_file))
    c=Cocktails()
    assert not c.cocktails


def test_get_receipts__empty_list(): ...


def test_get_receipts__list_with_one_ingredient(): ...


def test_get_receipts__list_with_another_ingredient(): ...


def test_get_receipts__list_with_multiple_ingredients(): ...


def test_get_receipts__list_with_incorrect_ingredient(): ...


def test_get_receipts__list_with_correct_and_incorrect_ingredient(): ...


def test_get_receipts__list_with_incorrect_ingredient_type(): ...


def test_get_receipts__int_instead_of_list(): ...


def test_get_receipts__list_with_all_ingredients(): ...


def test_get_random(): ...
