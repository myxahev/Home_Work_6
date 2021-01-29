''' Реализуйте базовый класс Car.

у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат. '''

class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'The {self.name} car.'

    def stop(self):
        return f'\nThe {self.name} has stopped.'

    def turn(self, direction):
        return f'\nThe {self.name} turned {direction}'

    def show_speed(self):
        return f'\nYour speed is {self.speed}'

class TownCar(Car):
    def show_speed(self):

        if self.speed > 60:
            return f'\nExcess of speed, your speed {self.speed}'
        else:
            super().show_speed()

class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):

        if self.speed < 40:
            super().show_speed()
        else:
            return f'\nExcess of speed, your speed {self.speed}'

class PoliceCar(Car):
    pass

town = TownCar('Lada Priora', 70, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('BMW', 170, 'black', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('KAMAZ', 30, 'orange', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('Kia', 100, 'yellow', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('right'), police.stop())