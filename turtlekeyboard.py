import turtle

def move_up():
    turtle.forward(50)

def move_down():
    turtle.right(180)
    turtle.forward(50)

def move_left():
    turtle.left(90)
    turtle.forward(50)

def move_right():
    turtle.right(90)
    turtle.forward(50)

def restart():
    turtle.reset()


while(True):

    turtle.shape('turtle')
    
    turtle.listen()
    turtle.stamp()

    turtle.onkey(move_up, 'w')
    turtle.onkey(move_down, 's')
    turtle.onkey(move_left, 'a')
    turtle.onkey(move_right, 'd')

    turtle.onkey(restart,'Escape')

