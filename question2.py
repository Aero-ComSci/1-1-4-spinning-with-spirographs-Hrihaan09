import turtle
screen = turtle.Screen()
def draw_objects(num_objects):

    screen.setup(width=800, height=400)  
    screen.tracer(0)

    obj_turtle = turtle.Turtle()
    obj_turtle.hideturtle()
    obj_turtle.penup() 


    margin = 50 
    available_width = 800 - 2 * margin
    spacing = available_width / (num_objects + 1)


    for i in range(num_objects):
        obj_turtle.penup()
        x = margin + (i + 1) * spacing
        y = 0  
        obj_turtle.goto(x, y)
        for i in range(4):
            obj_turtle.pendown()
            obj_turtle.forward(100)
            obj_turtle.right(90)

    screen.update() 
    turtle.done()

def main():
    num_objects = int(screen.textinput("Enter the number of objects", "(1-5): "))
    
    if 1 <= num_objects <= 5:
        draw_objects(num_objects)
    else:
        print("Number of objects must be between 1 and 5.")

if __name__ == "__main__":
    main()
