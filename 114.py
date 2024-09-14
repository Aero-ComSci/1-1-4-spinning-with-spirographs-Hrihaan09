import turtle
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("Concentric Squares")
t = turtle.Turtle()
t.speed(0) 
def draw_concentric_squares(t, num_squares, initial_size, increment):
    for i in range(num_squares):
        size = initial_size + i * increment
        t.pensize(4)
        t.penup()
        t.goto(-size / 2, size / 2)  # Center the square
        t.pendown()
        t.color((i / num_squares, 0.1,0.5))  # HSV to RGB
        for z in range(4):
            t.pensize(4)
            t.forward(size)
            t.right(90)
def main():
    num_squares = 20
    initial_size = 50
    increment = 30
    draw_concentric_squares(t, num_squares, initial_size, increment)
    turtle.done()
if __name__ == "__main__":
    main()
