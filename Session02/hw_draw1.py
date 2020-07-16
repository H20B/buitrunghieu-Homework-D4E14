from turtle import *
speed = -1
for num in range(3, 7):
    for i in range(num):
        if num % 2 == 1:
            color('blue')
        else:
            color('red')
        forward(100)
        left(360/num)
mainloop()
