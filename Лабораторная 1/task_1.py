import doctest
class Automat:
    def __init__(self, product_type: str, capacity: int):
        """
        Инициализация автомата с типом товаров и емкостью

        :param product_type: Товары ('напитки', 'бутерброды')
        :param capacity: Емкость автомата

        Пример:
        >>> automat = Automat('напитки', 50)
        """
        if not isinstance(product_type, str):
            raise TypeError("Название товаров должно быть буквенным")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Емкость автомата - целое число больше нуля")
        self.product_type = product_type
        self.capacity = capacity

    def check_availability(self) -> bool:
        """
        Проверка наличия товаров в автомате

        :return: Есть ли товар в наличии (True/False)

        Пример:
        >>> automat = Automat('напитки', 50)
        >>> automat.check_availability()
        True
        """
        ...

    def purchase(self, quantity: int) -> None:
        """
        Покупка товара

        :param quantity: Кол-во для покупки
        :raise ValueError: Кол-во > остатка - оошибка

        Пример:
        >>> automat = Automat('напитки', 50)
        >>> automat.purchase(5)
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Количество должно быть положительным целым числом")
        if quantity > self.capacity:
            raise ValueError("В автомате недостаточно товара")
        ...


if __name__ == "__main__":
    doctest.testmod()