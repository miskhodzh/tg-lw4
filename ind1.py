#  Дано натуральное число . Вывести на экран фразу Мне n лет , учитывая, что при
# некоторых значениях n слово «лет» надо заменить на слово «год» или «года»

n = input('Введите число >>> ')

if int(n[-1]) == 1 and int(n) != 11:
    end = 'год'
elif int(n) > 1 and int(n) <= 4:
    end = 'года'
elif int(n) >= 5:
    end = 'лет'

print('Мне', n, end)