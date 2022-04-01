from time import sleep
from itertools import cycle

class TrafficLight:

    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2), ('Green', 7))

    def running(self):
        for color, sec in cycle(self.__color):
            print(color, '(wait {} sec)'.format(sec))
            sleep(sec)

traffic_light = TrafficLight()
traffic_light.running()


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass


my_road = Road(20, 5000)
print(my_road.calc_mass(), 'т')



class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return round(self._income_wage + self._income_bonus, 2)


pos = Position('Ivan', 'Ivanov', 'Driver', {"wage": 20000, "bonus": 5000})
print(pos.get_full_name())
print(pos.get_total_income())



class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} поехала'.format(self.name))

    def stop(self):
        print('{} остановилась'.format(self.name))

    def turn(self, direction):
        print('{} повернула на {}'.format(self.name, direction))

    def show_speed(self):
        print('Текущая скорость:', self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости на', self.speed - 60)
        print('Текущая скорость:', self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости на', self.speed - 40)
        print('Текущая скорость:', self.speed)


class PoliceCar(Car):
    pass


sport_car = SportCar(200, 'Красная', 'Спортивная машина', False)
town_car = TownCar(100, 'Черная', 'Городская машина', False)
work_car = WorkCar(90, 'Желтая', 'Рабочая машина', False)
police_car = PoliceCar(150, 'Синяя', 'Полицейская машина', True)

sport_car.show_speed()
town_car.show_speed()
town_car.turn('лево')
work_car.show_speed()
police_car.show_speed()
police_car.stop()




class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Ручка рисует')


class Pencil(Stationery):
    def draw(self):
        super(Pencil, self).draw()
        print('Карандаш рисует')


class Handle(Stationery):
    def draw(self):
        print('Маркер рисует')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()