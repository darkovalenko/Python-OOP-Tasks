import turtle
import random



class Stem:
    def __init__(self, length=150, color="#1D5C1E"):
        self.length = length
        self.color = color

    def draw(self, t):
        t.color(self.color)
        t.pensize(5)
        t.setheading(90)
        t.forward(self.length)


class Leaf:
    def __init__(self, color="#2B832B"):
        self.color = color

    def draw(self, t, side="right"):
        t.color(self.color)
        t.fillcolor(self.color)
        t.pensize(1)

        angle = 350 if side == "right" else 160
        t.setheading(angle)

        t.begin_fill()
        size = 50
        arc_extent = 90
        t.circle(size, arc_extent)
        t.left(180 - arc_extent)
        t.circle(size, arc_extent)
        t.end_fill()


class Petal:
    def __init__(self, main_color="red", shade_color="darkred"):
        self.main_color = main_color
        self.shade_color = shade_color

    def draw(self, t):
        t.pensize(1)
        t.color(self.shade_color, self.main_color)
        t.begin_fill()
        extent = 80
        size = 60
        t.circle(size, extent)
        t.left(180 - extent)
        t.circle(size, extent)
        t.end_fill()


class Flower:
    def __init__(self, x, y, petal_color, stem_length=150):
        self.x = x
        self.y = y

        self.stem = Stem(length=stem_length)
        self.leaf = Leaf()

        if petal_color == "red":
            self.petal = Petal("red", "#8B0000")
        elif petal_color == "purple":
            self.petal = Petal("#9932CC", "#4B0082")
        elif petal_color == "orange":
            self.petal = Petal("#FF8C00", "#FF4500")
        elif petal_color == "pink":
            self.petal = Petal("#FF69B4", "#C71585")
        else:
            self.petal = Petal("white", "lightgray")

    def draw(self, t):
        head_x, head_y = 0, 0

        t.penup()
        t.goto(self.x, self.y)
        t.pendown()

        self.stem.draw(t)

        head_x, head_y = t.pos()

        leaf_height = self.stem.length / 2
        t.penup()
        t.goto(self.x, self.y + leaf_height)
        t.pendown()
        self.leaf.draw(t, side="right")

        t.penup()
        t.goto(self.x, self.y + leaf_height - 20)
        t.pendown()
        self.leaf.draw(t, side="left")

        num_petals = 12
        petal_angle = 360 / num_petals


        for i in range(num_petals):
            t.penup()
            t.goto(head_x, head_y)
            t.pendown()

            t.setheading(90 + i * petal_angle - (180 - 80) / 2 + 20)

            self.petal.draw(t)

        t.penup()

        center_radius = 16
        t.goto(head_x, head_y - center_radius)
        t.setheading(0)
        t.pendown()
        t.color("#FFD700", "#FFD700")
        t.begin_fill()
        t.circle(center_radius)
        t.end_fill()


def main():
    screen = turtle.Screen()
    screen.bgcolor("#A1DAFF")
    screen.title("Гарний букет з правильними листками та серединками")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()

    colors = ["red", "purple", "orange", "pink", "white"]
    positions = [
        (-180, -100),
        (-80, -140),
        (10, -110),
        (100, -150),
        (190, -90)
    ]

    # Створення та малювання букета
    for i in range(len(positions)):
        flower = Flower(
            x=positions[i][0],
            y=positions[i][1],
            petal_color=colors[i],
            stem_length=random.randint(130, 170)  # Трохи різна довжина стебел
        )
        flower.draw(pen)

    screen.exitonclick()


if __name__ == "__main__":
    main()