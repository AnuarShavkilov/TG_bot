
colors = ['коричневый', 'красный', 'оранжевый', 'желтый', 'зеленый',
          'голубой', 'фиолетовый', 'серый', 'белый', 'черный',
          'золотистый', 'серебристый']

def ring_count(resistor):
    global n, first, second, third, fourth, last
    n = resistor[0]
    first = resistor[1]
    second = resistor[2]
    # if n == 5:
    third = resistor[3]
    fourth = resistor[4]
    last = resistor[5]
    # elif n == 4:
    #     fourth = resistor[3]
    #     last = resistor[4]

    resultate = calcul()
    return resultate

def first_ring():
    count_fir = 0
    first_ring = first
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

    return(count_fir)

def second_ring():
    count_sec = 0
    second_ring = second
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

    return(count_sec)

def third_ring():
    third_ring = third
    count_thr = 0
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
    
    return(count_thr)

def fourth_ring(result_res):
    mult = 0
    fourth_ring = fourth
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

    return(mult)


def last_ring():
    proc = 0
    last_ring = last
    if last_ring.lower() == colors[10]:
        proc = 5
    elif last_ring.lower() == colors[11]:
        proc = 10

    return(proc)

def calcul():
    # if n == 5:
    result_res = str(first_ring()) + str(second_ring()) + str(third_ring())
    # elif n == 4:
    #     result_res = str(first_ring()) + str(second_ring())

    if 1000 < fourth_ring(result_res) < 1000000:
        kom = fourth_ring(result_res)/1000
        result_calcul = (f'Номинальное сопротивление = {kom} кОм\nТочность = {last_ring()} %')
    elif fourth_ring(result_res) > 1000000:
        mom = fourth_ring(result_res)/1000000
        result_calcul = (f'Номинальное сопротивление = {mom} МОм\nТочность = {last_ring()} %')
    else:
        result_calcul = (f'Номинальное сопротивление = {fourth_ring(result_res)} Ом\nТочность = {last_ring()} %')
    return result_calcul