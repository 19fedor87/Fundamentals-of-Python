# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных
# о пользователе одной строкой.

def my_info(**args):
    return args
print(my_info(
    name=input('Введите имя: '),
    surname=input('Введите фамилию: '),
    age=input('Введите возраст: '),
    city=input('Введите город: '),
    email=input('Введите email: '),
    phone=input('Введите телефон: '),
))

