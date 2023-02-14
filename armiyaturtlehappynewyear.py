import turtle
t = turtle.Turtle()
t.shape('turtle')
t.left(90)
turtle.colormode(255)
t.color(0,100,0)

t.up()
k = 0
for i in range(1, 15):
    y = 30*i
    for j in range(i-k):
        x = 30*j
        t.goto(x,-y+280)
        t.stamp()
        t.goto(-x,-y+280)
        t.stamp()
    if i % 4 == 0:
        x = 30*(j+1)
        k += 2

t.color(50,0,0)
for i in range(15,18):
    y = 30*i
    for j in range(3):
        x = 30*j
        t.goto(x,-y+280)
        t.stamp()
        t.goto(-x,-y+280)
        t.stamp()
turtle.exitonclick()