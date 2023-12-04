import doctest


class Auditorium:
    def __init__(self, number: int, capacity: int):
        """
        Инициализация аудитории с номером и вместимостью

        :param number: Номер аудитории
        :param capacity: Вместимость аудитории (количество мест)

        Пример:
        >>> auditorium = Auditorium(101, 40)
        """
        if not isinstance(number, int) or number <= 0:
            raise ValueError("Номер аудитории должен быть положительным целым числом")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Вместимость должна быть положительным целым числом")
        self.number = number
        self.capacity = capacity

    def check_availability(self, required_seats: int) -> bool:
        """
        Проверка возможности разместить заданное количество человек в аудитории

        :param required_seats: Требуемое количество мест
        :return: Возможность размещения (True/False)

        Пример:
        >>> auditorium = Auditorium(101, 40)
        >>> auditorium.check_availability(30)
        True
        """
        ...

    def take_seats(self, seats: int) -> None:
        """
        Занять места в аудитории

        :param seats: Количество мест которые займет группа
        :raise ValueError: Людей которые пришли > кол-во мест в аудитории - ошибка

        Пример:
        >>> auditorium = Auditorium(101, 40)
        >>> auditorium.take_seats(30)
        """
        ...

if __name__ == "__main__":
    doctest.testmod()