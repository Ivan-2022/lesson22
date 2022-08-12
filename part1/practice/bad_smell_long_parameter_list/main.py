# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    """
    Класс для управления перемещением unita
    """
    def __init__(self):
        pass

    def get_speed(self):
        """
        Получение скорости
        """
        if self.state == 'is_fly' and self.state == 'crawl':
            raise ValueError('Рожденный ползать летать не должен!')
        elif self.state == 'is_fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5

    def move(self, direction):
        """
        Cмещение по полю
        """
        speed = self.get_speed()

        if direction == 'UP':
            self.field.set_unit(x=self.new_x, y=self.new_y + speed, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(x=self.new_x, y=self.new_y - speed, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(x=self.new_x - speed, y=self.new_y, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(x=self.new_x + speed, y=self.new_y, unit=self)

