import turtle

def draw_sq():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(20)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.speed(20)

    i=1
    while i < 73:
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.right(5)

        angie.circle(100)
        angie.right(5)
        i += 1

    window.exitonclick()
    

draw_sq()
