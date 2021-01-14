"""Реализуем функцию расчета заработной платы сотрудника"""


def zarplat():

    name_person = input('Введите сотрудника: ')
    try:
        per_virab = float(input('Введите выработку в часах: '))
        hourly_rate = float(input('Введите часовую ставку сотрудника: '))
        pro_bonus = float(input('Введите процент премии: '))
        pers_zarplat = str((per_virab*hourly_rate)+(per_virab*hourly_rate*pro_bonus/100))
        print('Сотруднику - ' + name_person + ' начислено ' + str(pers_zarplat) + ' у.е')
    except ValueError:
        return print('Введенные не числовые данные!!!')


#zarplat()

#name_person = name_person
#per_virab = per_virab
#hourly_rate = float(hourly_rate)
#pro_bonus = pro_bonus
#pers_zarplat = str((per_virab*hourly_rate)+(per_virab*hourly_rate*pro_bonus/100))


