import turtle
import time


class Figure:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.is_visible = False

    def set_color(self, color):
        self.color = color

    def _draw_shape(self, t, draw_color):
        pass

    def draw(self, t):
        if not self.is_visible:
            self._draw_shape(t, self.color)
            self.is_visible = True

    def hide(self, t, bg_color):
        if self.is_visible:
            self._draw_shape(t, bg_color)
            self.is_visible = False

    def move(self, t, new_x, new_y, bg_color):
        was_visible = self.is_visible
        if was_visible:
            self.hide(t, bg_color)

        self.x = new_x
        self.y = new_y

        if was_visible:
            self.draw(t)

class Stem:
    def __init__(self, length=100):
        self.length = length

    def draw(self, t, color):
        t.color(color)
        t.pensize(5)
        t.setheading(90)
        t.forward(self.length)


class Leaf:
    def draw(self, t, color, side="right"):
        t.color(color)
        t.fillcolor(color)
        t.pensize(1)
        angle = 20 if side == "right" else 160
        t.setheading(angle)
        t.begin_fill()
        t.circle(30, 90)
        t.left(90)
        t.circle(30, 90)
        t.end_fill()


class Petal:
    def draw(self, t, color):
        t.color(color)
        t.fillcolor(color)
        t.pensize(1)
        t.begin_fill()
        t.circle(40, 80)
        t.left(100)
        t.circle(40, 80)
        t.end_fill()

class Flower(Figure):
    def __init__(self, x, y, petal_color):
        super().__init__(x, y, petal_color)

        self.stem = Stem(length=100)
        self.leaf = Leaf()
        self.petal = Petal()

        self.stem_color = "#2B832B"
        self.center_color = "#FFD700"

    def _draw_shape(self, t, draw_color):

        is_hiding = (draw_color != self.color)

        c_stem = draw_color if is_hiding else self.stem_color
        c_petal = draw_color if is_hiding else self.color
        c_center = draw_color if is_hiding else self.center_color

        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        self.stem.draw(t, c_stem)

        head_x, head_y = t.pos()

        leaf_y = self.y + self.stem.length / 2
        t.penup()
        t.goto(self.x, leaf_y)
        t.pendown()
        self.leaf.draw(t, c_stem, side="right")

        t.penup()
        t.goto(self.x, leaf_y - 15)
        t.pendown()
        self.leaf.draw(t, c_stem, side="left")

        num_petals = 10
        for i in range(num_petals):
            t.penup()
            t.goto(head_x, head_y)
            t.pendown()
            t.setheading(90 + i * (360 / num_petals) + 10)
            self.petal.draw(t, c_petal)

        center_radius = 12
        t.penup()
        t.goto(head_x, head_y - center_radius)
        t.setheading(0)
        t.pendown()
        t.color(c_center)
        t.fillcolor(c_center)
        t.begin_fill()
        t.circle(center_radius)
        t.end_fill()


def main():
    screen = turtle.Screen()
    bg_color = "#A1DAFF"
    screen.bgcolor(bg_color)
    screen.title("Переміщення квітки (Спадкування + Композиція)")

    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()

    flower = Flower(x=-200, y=-100, petal_color="red")

    flower.draw(pen)
    screen.update()
    time.sleep(1)
    for _ in range(60):
        # Нові координати
        new_x = flower.x + 5
        new_y = flower.y + 2

        flower.move(pen, new_x, new_y, bg_color)

        screen.update()
        time.sleep(0.03)

    screen.exitonclick()


if __name__ == "__main__":
    main()