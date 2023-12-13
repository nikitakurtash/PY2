import doctest


class Phone:
    def __init__(self, model: str, battery_capacity: int):
        """
        Инициализация телефона с моделью и емкостью батареи

        :param model: Модель телефона
        :param battery_capacity: Емкость батареи в мАч

        Пример:
        >>> phone = Phone('Pineapplephone 15 Pro', 3000)
        """
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not isinstance(battery_capacity, int) or battery_capacity <= 0:
            raise ValueError("Емкость батареи должна быть положительным целым числом")
        self.model = model
        self.battery_capacity = battery_capacity
        self.current_charge = battery_capacity

    def make_call(self, duration: int) -> None:
        """
        Совершение звонка

        :param duration: Продолжительность звонка в минутах
        :raise ValueError: Продолжительность звонка - целое число больше нуля

        Пример:
        >>> phone = Phone('Pineapplephone 15 Pro', 3000)
        >>> phone.make_call(10)
        """
        ...

    def charge_phone(self, charge_amount: int) -> None:
        """
        Зарядка телефона

        :param charge_amount: Количество мАч для зарядки
        :raise ValueError: Если количество мАч для зарядки отрицательно или больше емкости батареи

        Примеры:
        >>> phone = Phone('Pineapplephone 15 Pro', 3000)
        >>> phone.charge_phone(500)
        """
        ...

    def check_battery_status(self) -> int:
        """
        Проверка текущего уровня заряда батареи.

        :return: Текущий уровень заряда батареи в процентах

        Примеры:
        >>> phone = Phone('Pineapplephone 15 Pro', 3000)
        >>> phone.check_battery_status()
        100.0
        """
        return (self.current_charge / self.battery_capacity) * 100


if __name__ == "__main__":
    doctest.testmod()