"""
Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.

✔Начальная сумма равна нулю
✔Допустимые действия: пополнить, снять, выйти
✔Сумма пополнения и снятия кратны 50 у.е.
✔Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔Нельзя снять больше, чем на счёте
✔При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
✔Любое действие выводит сумму денег

"""

from datetime import date

amount_in_bank = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01


def add_bank(cash: float) -> None:
    """refilling bank"""
    global amount_in_bank
    global count
    amount_in_bank += cash
    count += 1
    if count % 3 == 0:
        amount_in_bank = amount_in_bank + percent_add * amount_in_bank
        print("начислены проценты в размере: ", percent_add * amount_in_bank)


def take_bank(cash: float) -> None:
    """cash advance"""
    global amount_in_bank
    global count
    amount_in_bank -= cash
    count += 1

    if cash * percent_take < 30:
        amount_in_bank -= 30
        print("списаны проценты за снятие: ", 30)
    elif cash * percent_take > 600:
        bank -= 600
        print("списаны проценты за снятие: ", 600)
    else:
        amount_in_bank -= cash * percent_take
        print("списаны проценты за снятие: ", cash * percent_take)

    if count % 3 == 0:
        bank = amount_in_bank + percent_add * amount_in_bank
        print("начислены проценты в размере: ", percent_add * amount_in_bank)


def exit_bank():
    """exit from bank"""
    print("Окончание операций\n")
    exit()


def check_bank() -> int:
    """checking correct adding"""
    while True:
        cash = int(input("Введите сумму опреации кратно 50\n"))
        if cash % 50 == 0:
            return cash


list_operation = []
while True:
    action = input("1 - пополнить баланс \n2 - снять деньги\n3 - история операций\n4 - выйти\n")

    if action == '1':
        cash = check_bank()
        add_bank(cash)
        if amount_in_bank > 5_000_000:
            amount_in_bank = amount_in_bank - amount_in_bank * percent_tax
            print("списан налог на богатство: ", amount_in_bank * percent_tax)
        print("Баланс = ", amount_in_bank)
        list_operation.append([str(date.today()), cash])

    elif action == '2':
        if amount_in_bank > 5_000_000:
            amount_in_bank = amount_in_bank - amount_in_bank * percent_tax
            print("списан налог на богатство: ", amount_in_bank * percent_tax)
        cash = check_bank()

        if cash < amount_in_bank:
            take_bank(cash)
            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("Недостаточно средств на счете\n")

        if amount_in_bank > 5_000_000:
            amount_in_bankk = amount_in_bank - amount_in_bank * percent_tax
            print("списан налог на богатство: ", amount_in_bank * percent_tax)
        print("Баланс = ", amount_in_bank)

    elif action == '3':
        print(list_operation)

    elif action == '4':
        exit_bank()
