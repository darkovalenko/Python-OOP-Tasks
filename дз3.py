import math

class Figure:
    def dimention(self): return None
    def perimetr(self): return None
    def square(self): return None
    def squareSurface(self): return None
    def squareBase(self): return None
    def height(self): return None
    def volume(self): return None

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def dimention(self): return 2

    def perimetr(self): return self.a + self.b + self.c

    def square(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(max(0, p * (p - self.a) * (p - self.b) * (p - self.c)))

    def volume(self): return self.square()


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b
    def dimention(self): return 2
    def perimetr(self): return 2 * (self.a + self.b)
    def square(self): return self.a * self.b
    def volume(self): return self.square()


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a, self.b = a, b
        self.c, self.d = c, d

    def dimention(self): return 2
    def perimetr(self): return self.a + self.b + self.c + self.d
    def square(self):
        try:
            num = (self.a - self.b)**2 + self.c**2 - self.d**2
            den = 2 * (self.a - self.b)
            h_squared = self.c**2 - (num / den)**2
            if h_squared < 0:
                return 0

            return ((self.a + self.b) / 2) * math.sqrt(h_squared)

        except (ZeroDivisionError, ValueError):
            return 0

    def volume(self): return self.square()

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a, self.b = a, b
        self._h = h

    def dimention(self): return 2

    def perimetr(self): return 2 * (self.a + self.b)

    def square(self): return self.a * self._h

    def volume(self): return self.square()


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self): return 2
    def perimetr(self): return 2 * math.pi * self.r
    def square(self): return math.pi * (self.r ** 2)
    def volume(self): return self.square()

class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self): return 3
    def squareSurface(self): return 4 * math.pi * (self.r ** 2)
    def volume(self): return (4 / 3) * math.pi * (self.r ** 3)

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self._height = h

    def dimention(self): return 3
    def perimetr(self): return None
    def square(self): return None
    def squareBase(self): return super().square()
    def height(self): return self._height
    def volume(self): return (1 / 3) * self.squareBase() * self.height()


class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self._height = h

    def dimention(self): return 3
    def perimetr(self): return None
    def square(self): return None
    def squareBase(self): return super().square()
    def height(self): return self._height
    def volume(self): return (1 / 3) * self.squareBase() * self.height()

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self._height = c

    def dimention(self): return 3
    def perimetr(self): return None
    def square(self): return None
    def squareBase(self): return super().square()
    def height(self): return self._height
    def volume(self): return self.squareBase() * self.height()


class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self._height = h

    def dimention(self): return 3
    def perimetr(self): return None
    def square(self): return None
    def squareBase(self): return super().square()
    def height(self): return self._height
    def volume(self): return (1 / 3) * self.squareBase() * self.height()


class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self._height = h

    def dimention(self): return 3
    def perimetr(self): return None
    def square(self): return None
    def squareBase(self): return super().square()
    def height(self): return self._height
    def volume(self): return self.squareBase() * self.height()


def parse_figure(line):
    parts = line.strip().split()
    if not parts:
        return None

    name = parts[0]
    args = [float(x) for x in parts[1:]]

    classes = {
        "Triangle": Triangle,
        "Rectangle": Rectangle,
        "Trapeze": Trapeze,
        "Parallelogram": Parallelogram,
        "Circle": Circle,
        "Ball": Ball,
        "TriangularPyramid": TriangularPyramid,
        "QuadrangularPyramid": QuadrangularPyramid,
        "RectangularParallelepiped": RectangularParallelepiped,
        "Cone": Cone,
        "TriangularPrism": TriangularPrism
    }

    if name in classes:
        return classes[name](*args)
    return None


def find_max_figure(filename):
    max_fig = None
    max_measure = -1
    max_name = ""

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                fig = parse_figure(line)
                if fig:
                    measure = fig.volume()
                    if measure and measure > max_measure:
                        max_measure = measure
                        max_fig = fig
                        max_name = line.strip().split()[0]

        if max_fig:
            print(f"Файл {filename}: Найбільша міра у фігури {max_name} = {max_measure:.2f}")
        else:
            print(f"Файл {filename}: Фігури не знайдено.")

    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено. Переконайся, що він лежить у тій самій папці.")


if __name__ == "__main__":
    files = ["input01.txt", "input02.txt", "input03.txt"]
    for file in files:
        find_max_figure(file)