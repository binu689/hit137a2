import turtle

left_angle = int(input('Left branch angle: '))
right_angle = int(input('Right branch angle: '))
branch_length = int(input('Stating branch length: '))
recursion_depth = int(input('Recursion depth: '))
reduction_factor = float(input('Branch length reduction factor (%): ')) / 100

# setup the screen and the turtle
screen = turtle.Screen()
screen.screensize(600, 600)
t = turtle.Turtle()

def draw(length, depth):
	# if max branching depth reached, return with drawing
	if depth == 0:
		return
	# draw the central stem
	t.forward(length)
	# save branching position
	branch_point = t.pos()
	branch_heading = t.heading()
	# draw the left branch recursively
	t.left(left_angle)
	draw(length * reduction_factor, depth - 1)
	# return to saved branching position
	t.penup()
	t.setpos(branch_point)
	t.setheading(branch_heading)
	t.pendown()
	# draw the right branch recursively
	t.right(right_angle)
	draw(length * reduction_factor, depth - 1)

# go to bottom of the screen and set heading up
t.penup()
t.goto(0, -300)
t.setheading(90)
t.pendown()

# start drawing with starting branch length and recursion depth
draw(branch_length, recursion_depth)

t.hideturtle()
turtle.exitonclick()
