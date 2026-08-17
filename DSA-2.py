

import turtle
import random

random.seed()  


stack_depth = 0
max_depth_seen = 0
calls_made = 0


def draw_branch(t, length, depth, max_depth):
    """Recursive function = the 'algorithm' being simulated.

    Each call is a stack frame holding: length, depth, and turtle heading.
    """
    global stack_depth, max_depth_seen, calls_made

    stack_depth += 1                      
    max_depth_seen = max(max_depth_seen, stack_depth)
    calls_made += 1

    if depth == 0 or length < 4:
        stack_depth -= 1               
        return

    
    hue_t = depth / max_depth
    t.pencolor(
        0.15 + 0.1 * hue_t,
        0.35 + 0.5 * (1 - hue_t),
        0.55 + 0.4 * hue_t,
    )
    t.pensize(max(1, depth * 0.6))

    t.forward(length)

    
    right_angle = random.uniform(15, 45)
    left_angle = random.uniform(15, 45)
    shrink = random.uniform(0.68, 0.82)

    t.right(right_angle)
    draw_branch(t, length * shrink, depth - 1, max_depth)  

    t.left(right_angle + left_angle)
    draw_branch(t, length * shrink, depth - 1, max_depth)  

    t.right(left_angle)
    t.backward(length)                     

    stack_depth -= 1                       


def draw_petals_at_tips(t, length, depth, max_depth):
    """A second recursive pass: draw a little flower burst at each leaf,
    just to make it look more like a flower and less like a bare tree."""
    if depth == 0 or length < 4:
        t.pencolor(0.95, 0.55, 0.65)
        for _ in range(6):
            t.forward(6)
            t.backward(6)
            t.left(60)
        return

    right_angle = random.uniform(15, 45)
    left_angle = random.uniform(15, 45)
    shrink = random.uniform(0.68, 0.82)

    t.forward(length)
    t.right(right_angle)
    draw_petals_at_tips(t, length * shrink, depth - 1, max_depth)
    t.left(right_angle + left_angle)
    draw_petals_at_tips(t, length * shrink, depth - 1, max_depth)
    t.right(left_angle)
    t.backward(length)


def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("#0B1120")
    screen.title("Recursion Tree / Flower — DSA Turtle Sim")
    screen.tracer(0, 0)  

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.left(90)           
    t.penup()
    t.goto(0, -350)
    t.pendown()

    max_depth = 10
    draw_branch(t, 180, max_depth, max_depth)

    screen.update()

    print(f"Recursive calls made: {calls_made}")
    print(f"Max call-stack depth reached: {max_depth_seen}")

    canvas = screen.getcanvas()
    canvas.postscript(file="tree.eps")

    screen.bye()


if __name__ == "__main__":
    main()