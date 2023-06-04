import turtle
color = ["blue","magenta","red"]
count = 0
def sierpinski(length, level):
    global color, count, depth
    
    if level == 0:
        turtle.pencolor(color[int(count//3**(temp-depth-1))])
        
        for i in range(3):
            turtle.forward(length)
            turtle.left(120)
        
        count+=1
        if int(count//3**(temp-depth-1))>=3:
            count = 0
        
    else:
        sierpinski(length/2, level-1)
        turtle.penup()
        turtle.forward(length/2)
        turtle.pendown()
        sierpinski(length/2, level-1)
        turtle.penup()
        turtle.backward(length/2)
        turtle.left(60)
        turtle.forward(length/2)
        turtle.right(60)
        turtle.pendown()
        sierpinski(length/2, level-1)
        turtle.penup()
        turtle.left(60)
        turtle.backward(length/2)
        turtle.right(60)
        turtle.pendown()
turtle.speed(0)
depth = 0
temp = 4
sierpinski(200, 4)
turtle.Screen().exitonclick()