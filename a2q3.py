import turtle

def draw_recursive_edge(t, length, depth):

    if depth == 0:
        t.forward(length)
    else:
        # Calculate 1/3 of the length
        third = length / 3
        
        # 1. First segment
        draw_recursive_edge(t, third, depth - 1)
        
        # 2. Turn RIGHT 60 degrees (to point indentation INWARD)
        t.right(60)
        draw_recursive_edge(t, third, depth - 1)
        
        # 3. Turn LEFT 120 degrees
        t.left(120)
        draw_recursive_edge(t, third, depth - 1)
        
        # 4. Turn RIGHT 60 degrees to return to straight
        t.right(60)
        draw_recursive_edge(t, third, depth - 1)

def main():
    # --- PROMPTS FOR USER INPUTS ---
    print("Welcome to the Fractal Pattern Generator")
    try:
        num_sides = int(input("Enter the number of sides: "))
        side_length = float(input("Enter the side length: "))
        depth = int(input("Enter the recursion depth: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    # Window Setup
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    
    t = turtle.Turtle()
    t.speed(0) 
    
    # Starting position to center the 4-sided (square) pattern
    t.penup()
    t.goto(-side_length/2, side_length/2)
    t.pendown()

    # Rule: Pattern starts with a regular polygon
    angle = 360 / num_sides

    # Generate the pattern for each side
    for _ in range(num_sides):
        draw_recursive_edge(t, side_length, depth)
        t.right(angle)

    print("Drawing Finished!")
    screen.mainloop()

if __name__ == "__main__":
    main()