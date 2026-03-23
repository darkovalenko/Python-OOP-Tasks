import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


# --- Етап 2: Класи конкретних фігур ---
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def _is_valid(self):
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)

    def get_perimeter(self):
        if not self._is_valid():
            return 0
        return self.a + self.b + self.c

    def get_area(self):
        if not self._is_valid():
            return 0

        p = self.get_perimeter() / 2
        value_under_root = p * (p - self.a) * (p - self.b) * (p - self.c)

        if value_under_root <= 0:
            return 0

        return math.sqrt(value_under_root)

    def __str__(self):
        return f"Трикутник (сторони: {self.a}, {self.b}, {self.c})"


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b

    def __str__(self):
        return f"Прямокутник (сторони: {self.a}, {self.b})"


class Trapeze(Shape):
    def __init__(self, a, b, c, d):
        self.a, self.b = a, b
        self.c, self.d = c, d

    def get_perimeter(self):
        return self.a + self.b + self.c + self.d

    def get_area(self):
        base_diff = abs(self.a - self.b)
        if base_diff == 0:
            return self.a * self.c

        val = (base_diff ** 2 + self.c ** 2 - self.d ** 2) / (2 * base_diff)
        height = math.sqrt(abs(self.c ** 2 - val ** 2))
        return ((self.a + self.b) / 2) * height

    def __str__(self):
        return f"Трапеція (основи: {self.a}, {self.b}, бічні: {self.c}, {self.d})"


class Parallelogram(Shape):
    def __init__(self, a, b, h):
        self.a, self.b = a, b
        self.h = h

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.h

    def __str__(self):
        return f"Паралелограм (сторони: {self.a}, {self.b}, висота: {self.h})"


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def get_perimeter(self):
        return 2 * math.pi * self.r

    def get_area(self):
        return math.pi * (self.r ** 2)

    def __str__(self):
        return f"Круг (радіус: {self.r})"



def load_shapes_from_file(filename):
    shapes_list = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split()
                if not parts:
                    continue

                name = parts[0]
                params = [float(x) for x in parts[1:]]

                if name == "Triangle":
                    shapes_list.append(Triangle(*params))
                elif name == "Rectangle":
                    shapes_list.append(Rectangle(*params))
                elif name == "Trapeze":
                    shapes_list.append(Trapeze(*params))
                elif name == "Parallelogram":
                    shapes_list.append(Parallelogram(*params))
                elif name == "Circle":
                    shapes_list.append(Circle(*params))
                else:
                    print(f"Невідома фігура у файлі {filename}: {name}")

    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено у папці з проєктом.")
        return None
    except Exception as e:
        print(f"Помилка при читанні рядка '{line.strip()}' з файлу {filename}: {e}")
        return None

    return shapes_list


def main():
    files_to_process = ["input01.txt", "input02.txt", "input03.txt"]

    for filename in files_to_process:
        print(f"\n{'=' * 10} Аналіз файлу: {filename} {'=' * 10}")

        shapes = load_shapes_from_file(filename)

        if not shapes:
            print(f"Не вдалося обробити фігури з файлу {filename}. Пропускаємо...")
            continue

        max_area_shape = shapes[0]
        max_perimeter_shape = shapes[0]

        for shape in shapes:
            if shape.get_area() > max_area_shape.get_area():
                max_area_shape = shape


            if shape.get_perimeter() > max_perimeter_shape.get_perimeter():
                max_perimeter_shape = shape


        print(f" Найбільша площа:")
        print(f"   Фігура: {max_area_shape}")
        print(f"   Значення: {max_area_shape.get_area():.2f}")

        print(f" Найбільший периметр:")
        print(f"   Фігура: {max_perimeter_shape}")
        print(f"   Значення: {max_perimeter_shape.get_perimeter():.2f}")
        print("-" * 40)


if __name__ == "__main__":
    main()
