import turtle

# Create turtle object
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)   # move forward by 100 units
    t.right(90)      # turn right by 90 degrees

turtle.done()
