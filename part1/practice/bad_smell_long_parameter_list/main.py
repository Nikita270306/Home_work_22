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

    def __init__(self, fields, x_coord, y_coord, state, speed):
        self.fields = fields
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.state = state
        self.speed = speed

    def move(self, direction):
        speed = self.get_speed()

        if direction == 'UP':
            self.fields.set_units(y=self.y_coord + speed, x=self.x_coord)
        elif direction == 'DOWN':
            self.fields.set_units(y=self.y_coord - speed, x=self.x_coord)
        elif direction == 'LEFT':
            self.fields.set_units(y=self.y_coord, x=self.x_coord - speed)
        elif direction == 'RIGHT':
            self.fields.set_units(y=self.y_coord, x=self.x_coord + speed)

    def get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        if self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Эх тебя разнесло)')



