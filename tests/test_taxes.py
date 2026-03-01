import pytest
from src.taxes import calculate_taxes
from src.taxes import calculate_tax

@pytest.fixture
def prices():
    return [100, 200, 300]

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

@pytest.mark.parametrize("price, tax_rate, expected", [
        (100,10,110),
        (50,5,52.5)])
def test_calculate_tax_parametrize_1(price, tax_rate, expected):
    assert calculate_tax(price, tax_rate) == expected

def test_calculate_tax_invalid_price():
    with pytest.raises(ValueError, match='Неверная цена'):
        calculate_tax(-1, 10)

def test_calculate_tax_negative_tax():
    with pytest.raises(ValueError, match='Неверный налоговый процент'):
       calculate_tax(100, -10)

def test_calculate_tax_negative_tax_100():
    with pytest.raises(ValueError, match='Неверный налоговый процент'):
       calculate_tax(100, 110)

@pytest.mark.parametrize("price, tax_rate, discount, expected", [
        (100, 10, 0, 110.0),
        (100, 10, 10, 99.0),
        (100, 10, 100, 0.0),])
def test_calculate_tax_parametrize_2(price, tax_rate, discount, expected):
    assert calculate_tax(price, tax_rate, discount=discount) == expected

def test_calculate_tax_no_discount():
    assert calculate_tax(100, 10) == 110

@pytest.mark.parametrize("round_val, expected", [
        (0, 99),
        (1, 99.4),
        (2, 99.42),
        (3, 99.425)])
def test_calculate_tax_parametrize_3(round_val, expected):
    assert calculate_tax(100, 2.5, discount=3, round_val=round_val) == expected

@pytest.mark.parametrize("price, tax_rate, discount, round_val", [
    ('100', 10, 0, 1),
    (100, '10', 10, 1),
    (100, 10, '100', 1),
    (100, 10, 100, '1')])
def test_calculate_tax_parametrize_4(price, tax_rate, discount, round_val):
    with pytest.raises(TypeError):
        calculate_tax(price, tax_rate, discount=discount, round_val=round_val)

def test_calculate_tax_kwargs():
    with pytest.raises(TypeError):
        calculate_tax(100, 2, 3, 1)