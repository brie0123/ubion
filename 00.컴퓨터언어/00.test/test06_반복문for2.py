import turtle as t
'''
for x in range(3):
    t.forward(100)
    t.left(120)


for x in range(4):
    t.pencolor("green")
    t.forward(130)
    t.left(90)

for x in range(5):
    t.pencolor("grey")
    t.forward(150)
    t.left(72)'''

#반복문으로 원형 겹쳐그리

t.speed(10)
t.begin_fill
for x in range(10):
    t.begin_fill(DarkSeaGreen.5)
    t.pencolor("DarkSeaGreen")
    t.circle(100)
    t.left(360/10)
    t.end_fill(DarkSeaGreen.5)
    
