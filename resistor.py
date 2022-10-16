n = int(input('Введите кол-во колец\n'))
count_fir = 0
count_sec = 0
count_thr = 0
mult = 0
proc = 0
colors = ['коричневый', 'красный', 'оранжевый', 'желтый', 'зеленый',
          'голубой', 'фиолетовый', 'серый', 'белый', 'черный',
          'золотистый', 'серебристый']
if n == 4:
    first_ring = input('Выберите цвет первого кольца\n')
    if first_ring.lower() == colors[0]:
        count_fir += 1
    elif first_ring.lower() == colors[1]:
        count_fir += 2
    elif first_ring.lower() == colors[2]:
        count_fir += 3
    elif first_ring.lower() == colors[3]:
        count_fir += 4
    elif first_ring.lower() == colors[4]:
        count_fir += 5
    elif first_ring.lower() == colors[5]:
        count_fir += 6
    elif first_ring.lower() == colors[6]:
        count_fir += 7
    elif first_ring.lower() == colors[7]:
        count_fir += 8
    elif first_ring.lower() == colors[8]:
        count_fir += 9

    second_ring = input('Выберите цвет второго кольца\n')
    if second_ring.lower() == colors[0]:
        count_sec += 1
    elif second_ring.lower() == colors[1]:
        count_sec += 2
    elif second_ring.lower() == colors[2]:
        count_sec += 3
    elif second_ring.lower() == colors[3]:
        count_sec += 4
    elif second_ring.lower() == colors[4]:
        count_sec += 5
    elif second_ring.lower() == colors[5]:
        count_sec += 6
    elif second_ring.lower() == colors[6]:
        count_sec += 7
    elif second_ring.lower() == colors[7]:
        count_sec += 8
    elif second_ring.lower() == colors[8]:
        count_sec += 9

    result_res = str(count_fir) + str(count_sec)

    third_ring = input('Выберите цвет третьего кольца\n')
    if third_ring.lower() == colors[0]:
        mult = int(result_res) * 10
    elif third_ring.lower() == colors[1]:
        mult = int(result_res) * 100
    elif third_ring.lower() == colors[2]:
        mult = int(result_res) * 1000
    elif third_ring.lower() == colors[3]:
        mult = int(result_res) * 10000
    elif third_ring.lower() == colors[4]:
        mult = int(result_res) * 100000
    elif third_ring.lower() == colors[5]:
        mult = int(result_res) * 1000000
    elif third_ring.lower() == colors[6]:
        mult = int(result_res) * 10000000
    elif third_ring.lower() == colors[9]:
        mult = int(result_res) * 1
    elif third_ring.lower() == colors[10]:
        mult = float(result_res) / 10
    elif third_ring.lower() == colors[11]:
        mult = float(result_res) / 100

    fourth_ring = input('Выберите цвет четвертого кольца\n')
    if fourth_ring.lower() == colors[10]:
        proc = 5
    elif fourth_ring.lower() == colors[11]:
        proc = 10

    if 1000 < mult < 1000000:
        kom = mult/1000
        print(f'Номинальное сопротивление = {kom} кОм\nТочность = {proc} %')
    elif mult > 1000000:
        mom = mult/1000000
        print(f'Номинальное сопротивление = {mom} МОм\nТочность = {proc} %')
    else:
        print(f'Номинальное сопротивление = {mult} Ом\nТочность = {proc} %')

elif n == 5:
    first_ring = input('Выберите цвет первого кольца\n')
    if first_ring.lower() == colors[0]:
        count_fir += 1
    elif first_ring.lower() == colors[1]:
        count_fir += 2
    elif first_ring.lower() == colors[2]:
        count_fir += 3
    elif first_ring.lower() == colors[3]:
        count_fir += 4
    elif first_ring.lower() == colors[4]:
        count_fir += 5
    elif first_ring.lower() == colors[5]:
        count_fir += 6
    elif first_ring.lower() == colors[6]:
        count_fir += 7
    elif first_ring.lower() == colors[7]:
        count_fir += 8
    elif first_ring.lower() == colors[8]:
        count_fir += 9

    second_ring = input('Выберите цвет второго кольца\n')
    if second_ring.lower() == colors[0]:
        count_sec += 1
    elif second_ring.lower() == colors[1]:
        count_sec += 2
    elif second_ring.lower() == colors[2]:
        count_sec += 3
    elif second_ring.lower() == colors[3]:
        count_sec += 4
    elif second_ring.lower() == colors[4]:
        count_sec += 5
    elif second_ring.lower() == colors[5]:
        count_sec += 6
    elif second_ring.lower() == colors[6]:
        count_sec += 7
    elif second_ring.lower() == colors[7]:
        count_sec += 8
    elif second_ring.lower() == colors[8]:
        count_sec += 9

    third_ring = input('Выберите цвет третьего кольца\n')
    if third_ring.lower() == colors[0]:
        count_thr += 1
    elif third_ring.lower() == colors[1]:
        count_thr += 2
    elif third_ring.lower() == colors[2]:
        count_thr += 3
    elif third_ring.lower() == colors[3]:
        count_thr += 4
    elif third_ring.lower() == colors[4]:
        count_thr += 5
    elif third_ring.lower() == colors[5]:
        count_thr += 6
    elif third_ring.lower() == colors[6]:
        count_thr += 7
    elif third_ring.lower() == colors[7]:
        count_thr += 8
    elif third_ring.lower() == colors[8]:
        count_thr += 9

    result_res = str(count_fir) + str(count_sec) + str(count_thr)

    fourth_ring = input('Выберите цвет четвертого кольца\n')
    if fourth_ring.lower() == colors[0]:
        mult = int(result_res) * 10
    elif fourth_ring.lower() == colors[1]:
        mult = int(result_res) * 100
    elif fourth_ring.lower() == colors[2]:
        mult = int(result_res) * 1000
    elif fourth_ring.lower() == colors[3]:
        mult = int(result_res) * 10000
    elif fourth_ring.lower() == colors[4]:
        mult = int(result_res) * 100000
    elif fourth_ring.lower() == colors[5]:
        mult = int(result_res) * 1000000
    elif fourth_ring.lower() == colors[6]:
        mult = int(result_res) * 10000000
    elif fourth_ring.lower() == colors[9]:
        mult = int(result_res) * 1
    elif fourth_ring.lower() == colors[10]:
        mult = float(result_res) / 10
    elif fourth_ring.lower() == colors[11]:
        mult = float(result_res) / 100

    fifth_ring = input('Выберите цвет пятого кольца\n')
    if fifth_ring.lower() == colors[10]:
        proc = 5
    elif fifth_ring.lower() == colors[11]:
        proc = 10

    if 1000 < mult < 1000000:
        kom = mult / 1000
        print(f'Номинальное сопротивление = {kom} кОм\nТочность = {proc} %')
    elif mult > 1000000:
        mom = mult / 1000000
        print(f'Номинальное сопротивление = {mom} МОм\nТочность = {proc} %')
    else:
        print(f'Номинальное сопротивление = {mult} Ом\nТочность = {proc} %')
else:
    print('Кажется, Вы ввели неверное количество колец')
