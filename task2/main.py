import turtle

def draw_koch_segment(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)
        t.right(120)
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)

def draw_koch_snowflake(t, length, level):
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)

def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("white")
    t.speed(0)

    level = int(input("Enter the recursion level: "))
    
    length = 300
    
    t.penup()
    t.goto(-length/2, length/3)
    t.pendown()

    draw_koch_snowflake(t, length, level)

    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()