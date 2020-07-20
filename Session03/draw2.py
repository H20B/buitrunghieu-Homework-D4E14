from turtle import *
speed(-1)
list = ['red', 'blue', 'brown','yellow', 'grey']
def draw():
    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
def fill_color() :
    fillcolor(color)
    begin_fill()
    draw()
    end_fill()
for j in range(5):
    color = list[j]
    fill_color()
    forward(50)    


mainloop()    