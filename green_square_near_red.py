import turtle
import random

# настройка экрана
wn = turtle.Screen()
wn.title("Find square")
wn.bgcolor("green")
wn.setup(width=600, height=600)

# функция позиции квадратов


def position_fig(t, x, y):
    t.hideturtle()
    t.penup()
    t.setposition(x, y)
    t.speed(0)

# рисуем квадрат


def draw_square(t, col, length_side):
    t.pendown()
    t.pencolor(col)
    t.fillcolor(col)
    t.begin_fill()
    for i in range(4):
        t.fd(length_side)
        t.rt(90)
    t.end_fill()


# создаем круг
cir = turtle.Turtle()
cir.penup()
cir.shape("circle")
cir.color("orange")

# функция вывода сообщения


def message(text, color):
    cir.hideturtle()
    cir.goto(0, 0)
    cir.color(color)
    sq.clear()
    print(moves)
    cir.write(text, font=("Arial", 12, "bold"))


# функция проверка на попадание
def check(moves, x, y):
    if cir.distance(red) < 40:
        message('Игра окончена! Поражение!\nСделано шагов: ' + str(moves), 'red')
    if cir.distance(green) < 40:
        message('Победа!\nСделано шагов: ' + str(moves), 'black')

# функции перемещения


def move_up():
    global moves
    y_1 = cir.ycor() + 10
    cir.sety(y_1)
    moves += 1
    check(moves, x, y)


def move_down():
    global moves
    y_1 = cir.ycor() - 10
    cir.sety(y_1)
    moves += 1
    check(moves, x, y)


def move_right():
    global moves
    x_1 = cir.xcor() + 10
    cir.setx(x_1)
    moves += 1
    check(moves, x, y)


def move_left():
    global moves
    x_1 = cir.xcor() - 10
    cir.setx(x_1)
    moves += 1
    check(moves, x, y)


# создание переменных
moves = 0
x = random.randrange(-500//2, 500//2)
y = random.randrange(-500//2, 500//2)
x_gr = random.randrange(0, 40)
y_gr = random.randrange(0, 40)


# создание квадратов на экране
sq = turtle.Turtle()
sq.hideturtle()
# position_fig(sq, x-20, y+70)
# draw_square(sq, 'red', 60)
# position_fig(sq, x-60, y+90)
# draw_square(sq, 'green', 40)

green = turtle.Turtle()
green.penup()
green.shapesize(1, 1)
green.shape('square')
green.color('green')
green.goto(x-x_gr, y-y_gr)

red = turtle.Turtle()
red.penup()
red.shapesize(3, 2)
red.shape('square')
red.color('red')
red.goto(x, y)


# создание связей с  клавишами
wn.listen()
wn.onkeypress(move_up, 'w')  # Up
wn.onkeypress(move_down, 's')  # Down
wn.onkeypress(move_right, 'd')  # Right
wn.onkeypress(move_left, 'a')  # Left

wn.mainloop()
