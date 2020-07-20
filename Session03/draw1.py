from turtle import *
speed(-1)
for i in range(3,8):
    for j in range(i):
        if i % 5 == 3:
            color('red')
        elif i % 5 == 4:
            color('blue')
        elif i % 5 == 0:
            color('brown')  
        elif i % 5 == 1:
            color('yellow')  
        elif i % 5 == 2:
            color('grey')
        forward(100)
        left(360/i)   
mainloop()                     
