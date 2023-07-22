"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""
number = int(input('Введите целое число: '))
num = hex(number)
hex_alphabet = '0123456789abcdef'
DIVIDER = 16
number_hex = " "

while number > 0:
    number_hex = hex_alphabet[number % DIVIDER] + number_hex
    number //= DIVIDER

print(f'В шестнадцатиричной системе = 0x{number_hex}')
print(f'Проверка hex функцией: в шестнадцатиричной системе = {num}')
