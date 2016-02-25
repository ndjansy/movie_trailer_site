import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    count = 0
    while count < 5:
        brad.forward(100)
        brad.right(90)
        count += 1
    

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    salma = turtle.Turtle()
    salma.shape("triangle")
    salma.color("green")
    salma.speed(3)

    count = 0
    while count < 4:
        salma.forward(100)
        salma.left(120)
        count += 1
    
    
    window.exitonclick()


draw_square()    
