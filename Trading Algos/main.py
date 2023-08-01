import turtle

def draw_canvas():
    # Create a turtle object
    t = turtle.Turtle()

    # Set the speed of the turtle (1 to 10, 1 being the slowest)
    t.speed(1)

    # Draw a square
    for _ in range(4):
        t.forward(100)  # Move the turtle forward by 100 units
        t.left(90)      # Turn the turtle left by 90 degrees

    # Draw a circle
    t.penup()         # Lift the pen up (don't draw while moving)
    t.goto(150, 0)    # Move the turtle to the right
    t.pendown()       # Put the pen down (start drawing again)
    t.circle(50)      # Draw a circle with a radius of 50 units

    # Draw a triangle
    t.penup()
    t.goto(-150, -100)
    t.pendown()
    for _ in range(3):
        t.forward(100)
        t.left(120)

    # Close the canvas when clicked
    turtle.done()

if __name__ == "__main__":
    draw_canvas()
