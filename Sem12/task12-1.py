"""
- Создайте класс студента.
- Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
- Названия предметов должны загружаться из файла CSV при создании экземпляра.
 Другие предметы в экземпляре недопустимы.
 - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
- Также экземпляр должен сообщать средний балл по тестам для каждого предмета и
по оценкам всех предметов вместе взятых.
"""

from pathlib import Path
from functools import reduce
import csv


class Check:
    "Дескриптор проверки ФИО на первую заглавную букву и наличие только букв"

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.isalpha():
            raise TypeError(f'Значение {value} должно содержать только буквы')
        if not value.istitle():
            raise TypeError(f'Значение {value} должно начинаться с заглавной буквы')


class Student:
    name = Check()
    patronymic = Check()
    surname = Check()
    _lessonlist = None

    def __init__(self, name, patronymic, surname, lesson_file: Path):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.lessonlist = lesson_file

    @property
    def lessonlist(self):
        return self._lessonlist

    @lessonlist.setter
    def lessonlist(self, lesson_file: Path):
        self._lessonlist = {"lessonlist": {}}
        with open(lesson_file, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self._lessonlist["lessonlist"][row[0]] = {"assessments": [], "test_results": [], "average_test": None}
        self._lessonlist["middle_assessment"] = None
        self._lessonlist["middle_test"] = None

    def __call__(self, lesson, number, type_est="lesson"):
        if lesson not in self.lessonlist["lessonlist"].keys():
            raise AttributeError("Предмет не обнаружен")
        if type_est == "lesson":
            if number < 2 or number > 5:
                raise ValueError("Оценка предмета должна быть от 2 до 5")
            self.lessonlist["lessonlist"][lesson]["assessments"].append(number)
            self.lessonlist["middle_assessment"] = self.calculate_middle_estimate(self.lessonlist)
        elif type_est == "test":
            if number < 0 or number > 100:
                raise ValueError("Оценка теста должна быть от 0 до 100")
            self.lessonlist["lessonlist"][lesson]["test_results"].append(number)
            self.lessonlist["lessonlist"][lesson]["average_test"] = reduce(lambda x, y: x + y,
                                                                           self.lessonlist["lessonlist"][lesson][
                                                                               "test_results"]) / len(
                self.lessonlist["lessonlist"][lesson]["test_results"])
            self.lessonlist['middle_test'] = self.calculate_middle_test(self.lessonlist)

    @staticmethod
    def calculate_middle_estimate(lessonlist):
        """Средний бал предмета"""
        all_estimates = []
        [all_estimates.extend(lessonlist["lessonlist"][name]["assessments"]) for name in lessonlist["lessonlist"]]
        return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)

    @staticmethod
    def calculate_middle_test(lessonslist):
        """Средний бал теста"""
        all_estimates = []
        [all_estimates.extend(lessonslist["lessonlist"][name]["test_results"]) for name in lessonslist["lessonlist"]]
        return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)

    def __repr__(self):
        result = f'\nCтудент = {self.name} {self.patronymic} {self.surname}\n\nСредняя оценка по предметам = ' \
                 f'{self.lessonlist["middle_assessment"]}\n'
        result += "\nОценки по предметам:\n"
        for key, value in self.lessonlist["lessonlist"].items():
            result += f'{key} = {value["assessments"]}\n'
        result += "\nРезультаты тестов по предметам:\n"
        for key, value in self.lessonlist["lessonlist"].items():
            result += f'{key} = {value["test_results"]}, ср.бал = {value["average_test"]}\n'
        return result


stud1 = Student("Иван", "Иванович", "Иванов", Path('lessonlist.csv'))
stud1("алгебра", 2)
stud1("алгебра", 5)
stud1("алгебра", 60, "test")
stud1("алгебра", 85, "test")
stud1("физика", 3)
stud1("геометрия", 5)
stud1("геометрия", 4)
stud1("геометрия", 85, "test")
stud1("химия", 10, "test")
stud1("химия", 64, "test")
stud1("химия", 4)
stud1("физика", 5)

print(stud1)
