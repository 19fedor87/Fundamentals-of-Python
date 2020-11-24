# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна,
# лето, осень). Напишите решения через list и через dict.

month = int(input('Введите номер месяца: '))
# year = ['Зима', 'Весна', 'Лето', 'Осень']             #list
year = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень'}   #dict
if 0 < month < 3:
        print(year[0])
elif 6 > month > 2:
        print(year[1])
elif 9 > month > 5:
        print(year[2])
elif 12 > month > 8:
        print(year[3])
elif month == 12:
        print(year[0])
elif month < 0:
        print('Неверное значение')
elif month > 12:
        print('Неверное значение')