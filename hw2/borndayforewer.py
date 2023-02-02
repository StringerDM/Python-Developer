# 13.Написать или модернизировать программу (МОДУЛЬ 3) используя условные операторы и цикл while:

year = 1799
day = 6

birth_year, birth_day = 0, 0

while birth_year != year:
    birth_year = int(input('Введите год рождения А.С Пушкина: '))

while birth_day != 6:
    birth_day = int(input('Введите день рождения А.С Пушкина: '))

print('Верно')
