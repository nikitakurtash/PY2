class Computer:
    """
    Базовый класс компьютера(бренд, модель)
    """
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Компьютер: {self.brand} {self.model}"

    def __repr__(self):
        return f"Computer('{self.brand}', '{self.model}')"

class Processor(Computer):
    """
    Дочерний класс процессора, наследует свойства компьютера(кол-во ядер)
    """
    def __init__(self, brand: str, model: str, cores: int):
        super().__init__(brand, model)
        self.cores = cores

    def __str__(self):
        return f"Процессор: {self.brand} {self.model}, Ядер: {self.cores}"

    def __repr__(self):
        return f"Processor('{self.brand}', '{self.model}', '{self.cores}')"

class GraphicsCard(Computer):
    """
    Дочерний класс видеокарты, наследует свойства компьютера(кол-во памяти)
    """
    def __init__(self, brand: str, model: str, memory: int):
        super().__init__(brand, model)
        self.memory = memory

    def __str__(self):
        return f"Видеокарта: {self.brand} {self.model}, Память: {self.memory}GB"

    def __repr__(self):
        return f"Videocard('{self.brand}', '{self.model}', '{self.memory}')"

class Weather:
    """
    Базовый класс погоды(температура)
    """
    def __init__(self, temperature: int):
        self.temperature = temperature

    def __str__(self):
        return f"Температура: {self.temperature}°C"

    def __repr__(self):
        return f"Weather({self.temperature})"

class Rain(Weather):
    """
    Дочерний класс дождя, наследует свойства погоды (интенсивность)
    """
    def __init__(self, temperature: int, intensity: str):
        super().__init__(temperature)
        self.intensity = intensity

    def __str__(self):
        return f"Дождь: Температура {self.temperature}°C, Интенсивность: {self.intensity}"

    def __repr__(self):
        return f"Rain('{self.temperature}', '{self.intensity}')"

class Snow(Weather):
    """
    Дочерний класс снега, наследует свойства погоды (размер снежинок)
    """
    def __init__(self, temperature: int, flake_size: str):
        super().__init__(temperature)
        self.flake_size = flake_size

    def __str__(self):
        return f"Снег: Температура {self.temperature}°C, Размер снежинок: {self.flake_size}"

    def __repr__(self):
        return f"Snow('{self.temperature}', '{self.flake_size}')"

class YouTube:
    """
    Базовый класс Ютуба(номер видео)
    """
    def __init__(self, video_id: str):
        self.video_id = video_id

    def __str__(self):
        return f"Видео ID: {self.video_id}"

    def __repr__(self):
        return f"YouTube('{self.video_id}')"

class Upload(YouTube):
    """
    Класс для загрузки видео на Ютуб(путь к видео)
    """
    def __init__(self, video_id: str, file_path: str):
        super().__init__(video_id)
        self.file_path = file_path

    def __str__(self):
        return f"Загрузка: Видео ID {self.video_id}, Путь файла: {self.file_path}"

    def __repr__(self):
        return f"Upload('{self.video_id}', '{self.file_path}')"

class View(YouTube):
    """
    Класс для просмотра видео на Ютуб(кол-во просмотров)
    """
    def __init__(self, video_id: str, views: int):
        super().__init__(video_id)
        self.views = views

    def __str__(self):
        return f"Просмотр: Видео ID {self.video_id}, Просмотры: {self.views}"

    def __repr__(self):
        return f"Views('{self.video_id}', '{self.views}')"

