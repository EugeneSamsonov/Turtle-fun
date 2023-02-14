import random
import turtle
t = turtle.Turtle()
t.speed(0)
def draw_circle(c, r):
	t.fillcolor(c)
	t.begin_fill()
	t.circle(r)
	t.end_fill()

def draw_panda(x, y):
    # Уши 
    # 1
    t.penup()
    t.setpos(x-50, y+50)
    t.pendown()
    draw_circle('black', 20)

    # 2
    t.penup()
    t.setpos(x+50, y+50)
    t.pendown()
    draw_circle('black', 20)

    # Лицо
    t.penup()
    t.setpos(x, y)
    t.pendown()
    draw_circle('white', 50)

    #Глаза
    # 1 глаз
    t.penup()
    t.setpos(x-20, y+50)
    t.pendown()
    draw_circle('black', 10)

    # 2 глаз
    t.penup()
    t.setpos(x+20, y+50)
    t.pendown()
    draw_circle('black', 10)

    #Зрачки
    # 1
    t.penup()
    t.setpos(x-20, y+52)
    t.pendown()
    draw_circle('white', 5)

    # 2
    t.penup()
    t.setpos(x+20, y+52)
    t.pendown()
    draw_circle('white', 5)

    #Нос
    t.penup()
    t.setpos(x, y+35)
    t.pendown()
    draw_circle('black', 6)

    #Рот
    t.penup()
    t.setpos(x, y+35)
    t.pendown()
    t.rt(90)
    t.circle(6, 180)
    t.penup()
    t.setpos(x, y+35)
    t.pendown()
    t.lt(360)
    t.circle(6, -180)
    t.hideturtle()

for i in range(30):
    x = random.randrange(-turtle.window_width()//2, turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2, turtle.window_height()//2)

    draw_panda(x,y)
    t.penup()
    t.home()
    t.pendown()