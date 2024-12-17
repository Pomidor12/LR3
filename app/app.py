import math

def square_area(side_length):
    return side_length ** 2

def pyramid_volume(base_area, height):
    return (1/3) * base_area * height

def pyramid_surface_area(base_area, perimeter, slant_height):
    lateral_area = (1/2) * perimeter * slant_height
    return base_area + lateral_area

def calculate_pyramid(side_length, height):
    base_area = square_area(side_length)
    perimeter = 4 * side_length
    slant_height = math.sqrt((side_length / 2) ** 2 + height ** 2)
    volume = pyramid_volume(base_area, height)
    surface_area = pyramid_surface_area(base_area, perimeter, slant_height)
    return volume, surface_area

if __name__ == "__main__":
    side_length = float(input("Введите длину стороны основания: "))
    height = float(input("Введите высоту пирамиды: "))
    volume, surface_area = calculate_pyramid(side_length, height)
    print(f"Объем пирамиды: {volume:.2f}")
    print(f"Площадь поверхности пирамиды: {surface_area:.2f}")

NO_VALUE = -1
developersInfo = '1st developer: Abaidullin Ruslan \n2nd developer: Abzalov Timur \n3rd developer: Baulybaev Dinar'
class Shape:
    def __init__(self, s=NO_VALUE, h=NO_VALUE):
        self.__s = s
        self.__h = h

    @staticmethod
    def about():
        print(developersInfo)

    def getSquare(self):
        print("some calculations")


Shape.about() 
