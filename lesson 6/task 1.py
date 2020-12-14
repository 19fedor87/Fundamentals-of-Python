# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и
# метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.


import time
class TrafficLight:
    def __init__(self, _color):
        self._color = ['красный', 'желтый', 'зеленый']

    def running(self):
        from itertools import cycle
        for self._color in cycle(self._color):
            print('красный')
            time.sleep(7)
            print('желтый')
            time.sleep(2)
            print('зеленый')
            time.sleep(5)

my_running = TrafficLight('')
my_running.running()