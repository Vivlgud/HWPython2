"""Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака."""

print("Задача 3")

from operator import itemgetter

dictionary = {'фонарь': 1, 'одежда': 7, 'палатка': 4, 'спальный мешок': 3, 'рыболовные снасти': 9, \
              'продукты': 5, 'аптечка': 2}
max_weight = 15
weight = 0
capacity = 0

print(f"Список всех вещей и их вес: {dictionary}")
print(f"Список вещей, который поместится в рюкзак, максимально {max_weight} кг")

for things, value in dict(sorted(dictionary.items(), key=itemgetter(1))).items():
    weight += dictionary[things]
    if weight <= max_weight:
        print(things, ' = ', value)
        capacity += dictionary[things]

print("вес рукзака с вещами: ", capacity)
