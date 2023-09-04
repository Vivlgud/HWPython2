import argparse
from task15_1 import Matrix


def convert_format(input):
    '''Преобразования входных данных в терминале в матрицу'''
    if len(input) == 1:
        j = 0
    else:
        j = 1
    m_1 = []
    m_2 = []
    input[j].append(' ')
    for i in input[j]:
        if i == ' ':
            m_2.append(list(m_1))
            m_1.clear()
        else:
            m_1.append(float(i))
    return m_2

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Получаем операцию над двумя матрицами")
    parser.add_argument('-m_1', type=list, action='append',
                        default=[['1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1', '1']])
    parser.add_argument('-m_2', type=list, action='append',
                        default=[['1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1', '1']])
    parser.add_argument('-operation', type=str, default='+')

    args = parser.parse_args()

    m_1 = convert_format(args.m_1)
    m_2 = convert_format(args.m_2)

    if args.operation == '+':
        print(f'СЛОЖЕНИЕ: {m_1} {args.operation} {m_2} : ', (f'{Matrix(m_1) + Matrix(m_2)} '))
    elif args.operation == '=':
        print(f'РАВЕНСТВО: {m_1} {args.operation} {m_2} : ', (f'{Matrix(m_1) == Matrix(m_2)} '))
    else:
        print(f'Такая операция {args.operation} над матрицами не предусмотрена!')

    # примеры вызова  из командной строки:
    # python Sem15\task15_1_terminal.py
    # python Sem15\task15_1_terminal.py -m_1='111 222 333' -m_2='333 222 111'
    # python Sem15\task15_1_terminal.py -m_1='124 252 253' -m_2='124 252 253' -operation='='
