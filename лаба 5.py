import math
import re


class Rational:
    def __init__(self, *args):
        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, Rational):
                self._n = arg._n
                self._d = arg._d
            elif isinstance(arg, str):
                if '/' in arg:
                    n_str, d_str = arg.split('/')
                    self._n = int(n_str)
                    self._d = int(d_str)
                else:
                    self._n = int(arg)
                    self._d = 1
            elif isinstance(arg, int):
                self._n = arg
                self._d = 1
            else:
                raise TypeError("Непідтримуваний тип аргументу для Rational")
        elif len(args) == 2:
            self._n = int(args[0])
            self._d = int(args[1])
        else:
            raise TypeError("Невірна кількість аргументів")

        self._reduce()

    def _reduce(self):
        if self._d == 0:
            raise ValueError("Помилка: Знаменник не може дорівнювати нулю.")

        g = math.gcd(self._n, self._d)
        self._n //= g
        self._d //= g

        if self._d < 0:
            self._n = -self._n
            self._d = -self._d

    def _get_other(self, other):
        if isinstance(other, int):
            return Rational(other)
        elif isinstance(other, Rational):
            return other
        return NotImplemented


    def __add__(self, other):
        other = self._get_other(other)
        if other is NotImplemented: return NotImplemented
        return Rational(self._n * other._d + other._n * self._d, self._d * other._d)

    def __sub__(self, other):
        other = self._get_other(other)
        if other is NotImplemented: return NotImplemented
        return Rational(self._n * other._d - other._n * self._d, self._d * other._d)

    def __mul__(self, other):
        other = self._get_other(other)
        if other is NotImplemented: return NotImplemented
        return Rational(self._n * other._n, self._d * other._d)

    def __truediv__(self, other):
        other = self._get_other(other)
        if other is NotImplemented: return NotImplemented
        if other._n == 0:
            raise ZeroDivisionError("Помилка: Ділення на нуль.")
        return Rational(self._n * other._d, self._d * other._n)

    __radd__ = __add__
    __rmul__ = __mul__

    def __rsub__(self, other):
        other = self._get_other(other)
        return other.__sub__(self)

    def __rtruediv__(self, other):
        other = self._get_other(other)
        return other.__truediv__(self)

    def __call__(self):
        return self._n / self._d

    def __getitem__(self, key):
        if key == "n":
            return self._n
        elif key == "d":
            return self._d
        raise KeyError("Ключ має бути 'n' (чисельник) або 'd' (знаменник)")

    def __setitem__(self, key, value):
        if key == "n":
            self._n = int(value)
        elif key == "d":
            self._d = int(value)
        else:
            raise KeyError("Ключ має бути 'n' (чисельник) або 'd' (знаменник)")
        self._reduce()

    def __str__(self):
        if self._d == 1:
            return str(self._n)
        return f"{self._n}/{self._d}"

    def __repr__(self):
        return f"Rational({self._n}, {self._d})"


def evaluate_expressions(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                expr = line.strip()
                if not expr:
                    continue

                rational_expr = re.sub(r'\b(\d+)\b', r'Rational(\1)', expr)

                try:
                    result = eval(rational_expr)
                    print(f"Рядок {line_num}: {expr}")
                    print(f"Результат (дріб): {result}")
                    print(f"Результат (десятковий): {result()}\n")
                except Exception as e:
                    print(f"Рядок {line_num}: Помилка обчислення виразу '{expr}' -> {e}\n")

    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено. Переконайтеся, що він лежить у тій самій папці.")


if __name__ == "__main__":
    evaluate_expressions("input01.txt")