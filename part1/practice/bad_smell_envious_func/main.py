
class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def calculate(self):
        return self.y * self.x * self.z


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube):
        return cube.calculate
