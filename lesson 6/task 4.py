# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
# WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} ура, я еду'

    def stop(self):
        return f'{self.name} блин, светофор'

    def turn_right(self):
        return f'{self.name} смотрю прямо, кручу в право'

    def turn_left(self):
        return f'{self.name} смотрю прямо, кручу влево'

    def show_speed(self):
        return f'Текущая скорость {self.name} {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Еду в городе {self.name} {self.speed} км/ч')

        if self.speed > 40:
            return f'Слишком быстро для города {self.name} км/ч'
        else:
            return f'Разумная скорость в городе {self.name} '

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Еду по работе на {self.name} {self.speed} км/ч')

        if self.speed > 60:
            return f'Скорость {self.name} слишком быстро для рабочей машины'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полиции'
        else:
            return f'{self.name} не из полиции'


audi = SportCar(100, 'Red', 'Audi', False)
volkswagen = TownCar(30, 'White', 'Volkswagen', False)
lada = WorkCar(70, 'Rose', 'Lada', True)
mitsubishi = PoliceCar(110, 'Blue',  'Mitsubishi', True)
print(lada.turn_left())
print(f'{volkswagen.turn_right()}, {audi.stop()}')
print(f'{lada.go()} хорошая скорость {lada.show_speed()}')
print(f'{lada.name} цвет {lada.color}')
print(f'{audi.name} полицейская машина? {audi.is_police}')
print(f'{lada.name} полицейская машина? {lada.is_police}')
print(audi.show_speed())
print(volkswagen.show_speed())
print(mitsubishi.police())
print(mitsubishi.show_speed())






# class Car:
#     def __init__(self, speed, color, name, is_polise):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_polise = is_polise
#
#     def go(self):
#         print('Ура, я еду')
#
#     def stop(self):
#         print('Блин, светофор')
#
#     def turn(self):
#         print('На лево еду')
#
#     def show_speed(self):
#         print(100)
#
# class TownCar(Car):
#     print('Еду как все')
#
# class SportCar(Car):
#     print('Ухожу в точку')
#
# class WorkCar(Car):
#     print('Стою в пробке')
#
# class PoliceCar(Car):
#     print('Высматриваю нарушителей')
#
# cars = Car()
# cars.