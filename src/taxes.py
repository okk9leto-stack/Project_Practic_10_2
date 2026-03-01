def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError('Неверная цена')
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)

    return taxed_prices


def calculate_tax(
        price: float,
        tax_rate: float,
        *,
        discount: float = 0,
        round_val: int =2
        ) -> float:
    """Функция вычисляет стоимость 1 товарA с учётом налога."""

    for arg in [price, tax_rate, discount, round_val]:
        if not isinstance(arg, (float|int)):
            raise TypeError ('Неверный тип данных')

    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError('Неверный налоговый процент')

    if price <= 0:
        raise ValueError('Неверная цена')

    tax_price = price + price * tax_rate / 100
    new_price_discount = tax_price - tax_price * discount/100
    return round(new_price_discount, round_val)

