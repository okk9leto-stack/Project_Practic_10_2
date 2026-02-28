import pytest
from src.taxes import calculate_taxes

# @pytest.fixture # отправила в conftest.py
# def prices():
#     return [100, 200, 300]


def test_calculate_taxes_valid():
    assert calculate_taxes([100, 200], 10) == [110, 220]

@pytest.mark.parametrize("tax_rate, expected", [
        (0,[100,200,300]),
        (10,[110,220,330]),
        (20,[120,240,360])
        ])
def test_calculate_taxes_parametrize(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected


def test_calculate_taxes_zero_price():
    with pytest.raises(ValueError, match='Неверная цена'):
        calculate_taxes([0,-1], 10)

def test_calculate_taxes_negative_tax():
    with pytest.raises(ValueError, match='Неверный налоговый процент'):
        calculate_taxes([100], -10)

