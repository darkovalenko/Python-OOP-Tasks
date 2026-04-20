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
            raise ValueError("Знаменник не може дорівнювати нулю.")
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

    __radd__ = __add__

    def __call__(self):
        return self._n / self._d

    def __getitem__(self, key):
        if key == "n":
            return self._n
        elif key == "d":
            return self._d
        raise KeyError("Ключ має бути 'n' або 'd'")

    def __setitem__(self, key, value):
        if key == "n":
            self._n = int(value)
        elif key == "d":
            self._d = int(value)
        else:
            raise KeyError("Ключ має бути 'n' або 'd'")
        self._reduce()

    def __str__(self):
        return f"{self._n}" if self._d == 1 else f"{self._n}/{self._d}"

    def __repr__(self):
        return f"Rational({self._n}, {self._d})"

class RationalList:
    def __init__(self):
        self._items = []
    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = Rational(value)

    def __len__(self):
        return len(self._items)

    def __add__(self, other):
        new_list = RationalList()
        new_list._items = self._items[:]

        if isinstance(other, RationalList):
            new_list._items.extend(other._items)
        elif isinstance(other, (int, str, Rational)):
            new_list._items.append(Rational(other))
        else:
            raise TypeError("Непідтримуваний тип операнда для додавання")
        return new_list

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self._items.extend(other._items)
        elif isinstance(other, (int, str, Rational)):
            self._items.append(Rational(other))
        else:
            raise TypeError("Непідтримуваний тип операнда для += ")
        return self

    def __iter__(self):
        sorted_items = sorted(
            self._items,
            key=lambda r: (r["d"], r["n"]),
            reverse=True
        )
        return iter(sorted_items)

    def __str__(self):
        return f"[{', '.join(str(r) for r in self._items)}]"


def process_data_files(filenames):
    for filename in filenames:
        print(f"\n{'=' * 40}")
        print(f"Обробка файлу: {filename}")
        print(f"{'=' * 40}")

        r_list = RationalList()
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    tokens = line.strip().split()
                    for token in tokens:
                        r_list += token

            if len(r_list) == 0:
                print("Файл порожній або не містить валідних чисел.")
                continue

            total_sum = Rational(0)
            for item in r_list._items:
                total_sum += item

            print("Послідовність (відсортована за спаданням знаменника та чисельника):")
            sorted_sequence = [str(item) for item in r_list]
            print("  " + "  ".join(sorted_sequence))

            print(f"\nСума всіх елементів послідовності: {total_sum}")

        except FileNotFoundError:
            print(f"Помилка: Файл '{filename}' не знайдено.")


if __name__ == "__main__":
    files = ["input01.txt", "input02.txt", "input03.txt"]
    process_data_files(files)