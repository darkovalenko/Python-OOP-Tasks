import math

class RationalError(ZeroDivisionError):

    def __init__(self, message="Помилка: Знаменник раціонального числа не може дорівнювати нулю."):
        self.message = message
        super().__init__(self.message)


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
            raise RationalError()

        g = math.gcd(self._n, self._d)
        self._n //= g
        self._d //= g
        if self._d < 0:
            self._n = -self._n
            self._d = -self._d

    def __str__(self):
        if self._d == 1:
            return str(self._n)
        return f"{self._n}/{self._d}"

    def __repr__(self):
        return f"Rational({self._n}, {self._d})"


if __name__ == "__main__":
    r1 = Rational(5, 2)
    print(f"Успішно створено: {r1}")

    try:
        r2 = Rational(5, 0)
    except RationalError as e:
        print(f"Спіймано виключення: {type(e).__name__} -> {e}")

    try:
        r3 = Rational("10/0")
    except RationalError as e:
        print(f"Спіймано виключення: {type(e).__name__} -> {e}")

    try:
        r4 = Rational(1, 0)
    except ZeroDivisionError as e:
        print("Виключення успішно спіймано як ZeroDivisionError!")