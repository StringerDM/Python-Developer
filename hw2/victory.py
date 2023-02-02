birth_year_Einstein = 1879
birth_year_Tolstoy = 1828
birth_year_Yesenin = 1895
birth_year_Stalin = 1878
birth_year_Plank = 1858

total_answers = 5
repeat = 'да'

while repeat == 'да':
    right_answers = 0

    # 1879
    birth_year = int(input('Введите год рождения Альберта Эйнштейна: '))
    if birth_year == birth_year_Einstein:
        right_answers += 1

    # 1828
    birth_year = int(input('Введите год рождения Л.Н. Толстова: '))
    if birth_year == birth_year_Tolstoy:
        right_answers += 1

    # 1895
    birth_year = int(input('Введите год рождения С.А. Есенина: '))
    if birth_year == birth_year_Yesenin:
        right_answers += 1

    # 1878
    birth_year = int(input('Введите год рождения И.В. Сталина: '))
    if birth_year == birth_year_Stalin:
        right_answers += 1

    # 1858
    birth_year = int(input('Введите год рождения Макса Планка: '))
    if birth_year == birth_year_Plank:
        right_answers += 1

    wrong_answers = total_answers - right_answers

    print('количество правильных ответов:', right_answers)
    print('количество ошибок:', wrong_answers)
    print('процент правильных ответов:',  right_answers * 100 / total_answers, '%')
    print('процент неправильных ответов:',  wrong_answers * 100 / total_answers, '%')

    repeat = input('хотите начать игру сначала? да/нет: ')
