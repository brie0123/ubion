import turtle

wm = turtle.Screen()
t = turtle.Turtle()


#triangle
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)


#pentagon
t.color("green")
t.forward(100)
t.left(360/5)
t.forward(100)
t.left(360/5)
t.forward(100)
t.left(360/5)
t.forward(100)
t.left(72)
t.forward(100)


wm.mainloop()
