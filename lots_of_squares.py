import turtle
import random
turtle.bgcolor('black')
turtle.colormode(255)
turtle.speed(0)

for i in range(300):
    turtle.pencolor(random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    turtle.fd(i+50)
    turtle.lt(91)


turtle.mainloop()
