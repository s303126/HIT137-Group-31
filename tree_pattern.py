
import turtle

def draw_branch(t, branch_length, left_angle, right_angle, reduction_factor, depth):
    if depth == 0:
        return

    
    t.forward(branch_length)
    
    
    t.left(left_angle)
    draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, reduction_factor, depth - 1)
    t.right(left_angle) 

    
    t.right(right_angle)
    draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, reduction_factor, depth - 1)
    t.left(right_angle)
    
    t.backward(branch_length)

def main():
    
    left_angle = (40)
    right_angle = (40)
    branch_length = (100)
    depth = (5)
    reduction_factor = 0.6

    
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90) 
    t.up()
    t.goto(0, -300) 
    t.down()

    
    draw_branch(t, branch_length, left_angle, right_angle, reduction_factor, depth)

    
    screen.mainloop()

if __name__ == "__main__":
    main()
