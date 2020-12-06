# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать
# формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, length, width, weight, height):
        self._length = length
        self._width = width
        self.weight = weight
        self.height = height

    def mass_of_aspalt(self):
        mass_of_aspalt = self._length * self._width * self.weight * self.height
        print(f'Для покрытия дорожного полотна неободимо {round(mass_of_aspalt)} т. массы асфальта')


my_aspalt = Road(20, 5000, 25, 5)
my_aspalt.mass_of_aspalt()