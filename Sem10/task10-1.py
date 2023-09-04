"""
Доработаем задания 5-6.
- Создайте класс-фабрику.
- Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
- Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""


class Animal():
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1


class Fishes(Animal):

    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return self._size


class Birds(Animal):

    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return self._color


class Mammals(Animal):

    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return self._spec

class Fabric:

    def __init__(self, animal_class,  **kwargs):
        self.animal_class = animal_class
        for key, value in kwargs.items():
            if key == 'kind':
                self.kind = value
            if key == 'name':
                self.name = value
            if key == 'age':
                self.age = value
            if key == 'size':
                self.size = value
            if key == 'color':
                self.color = value
            if key == 'spec':
                self.spec = value


    def get_info_animal(self):
        if self.animal_class == 'fishes':
            return Fishes(self.kind, self.name, self.age, self.size)
        elif self.animal_class == 'birds':
            return Birds(self.kind, self.name, self.age, self.color)
        elif self.animal_class == 'mammals':
            return Mammals(self.kind, self.name, self.age, self.spec)
        else:
            return f'нет такого животного'


animal1 = Fabric(animal_class='fishes',kind='карась', name='Федя', age=1, size=15).get_info_animal()

print(f'Вид: {animal1.get_kind()}')
print(f'кличка: {animal1.get_name()}')
print(f'возраст: {animal1.get_age()} лет')
print(f'размер: {animal1.get_specific()} см.')
