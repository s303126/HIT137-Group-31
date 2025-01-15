import turtle

# Recursive function to draw tree
def draw_branch(t, branch_length, left_angle, right_angle, reduction_factor, depth):
    """
    Draws a branch of the tree using recursion.
    Parameters:
        t (Turtle): The turtle object used to draw.
        branch_length (flote): Length of the current branch
        left_branch (int): Angle to turn left for left branch
        right_branch (int): Angle to turn right for right branch
        reduction_factor (flote): Factor by which branch length reduce depth
        dept (int): Current recursion depth.
    """
    if depth == 0:
     return

    #branch of tree
    t.forward(branch_length)
    
    
    t.left(left_angle)   #left turn
    draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, reduction_factor, depth - 1)
    t.right(left_angle) 

    
    t.right(right_angle)   #right turn
    draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, reduction_factor, depth - 1)
    t.left(right_angle)   #Turn back to original position
    
    t.backward(branch_length)  # Go back to starting point
# main function
def main():
    """
    Sets up the turtle environment and starts drawing the tree.
    """
    # Defined paramaters
    left_angle = (30)         # Angle to turn for left branches
    right_angle = (30)        # Angle to turn for right branches
    branch_length = (110)     # Starting length of branch
    depth = (5)               # Number of branches
    reduction_factor = (0.7)    # Factor to reduce branch length

    #setup turtle screen and turtle
    screen = turtle.Screen()
    screen.bgcolor("white")  # Background color
    t = turtle.Turtle()
    t.speed("normal")  # drawing speed
    t.left(90)      # point turtle upward
    t.up()
    t.goto(0, -100) 
    t.down()

    # Draw the tree
    draw_branch(t, branch_length, left_angle, right_angle, reduction_factor, depth)

    
    screen.mainloop()  # keep window open
# run the program
if __name__ == "__main__":
    main()
