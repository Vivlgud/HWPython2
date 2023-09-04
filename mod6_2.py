from random import randint


def check_pos(pos):
    beats = True
    for i in range(len(pos)):
        row, col = pos[i]
        for j in range(i + 1, len(pos)):
            row_2, col_2 = pos[j]
            if row == row_2 or col == col_2 or abs(row - row_2) == abs(col - col_2):
                beats = False
    return beats


def success_location():
    count = 4
    while count > 0:
        pos = list((i, randint(1, 9)) for i in range(1, 9))
        if check_pos(pos):
            print(*pos)
            count -= 1


if __name__ == "__main__":
    print("это шахматный модуль")
