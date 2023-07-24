
world.clear()
bob = Turtle()
import math
bob.delay = 0.1

def draw_A(t, h):
	"""
	Working code to draw upper case A using a Turtle.
	h: height of letter
    t: turtle
    |> theta: inclination of the diagonal stroke

    """
	theta = 68
	lt(t, theta)
	stroke = h/math.sin(theta/180*math.pi)
	fd(t, stroke) # UP stroke 
	rt(t, 2* theta)
	fd(t, stroke) # Down stroke
	t.pen =False
	bk(t, stroke *2/5)
	rt(t, 180-theta)
	t.pen = True
	fd(t,6/5*  h * math.tan((90-theta)/180*math.pi)) # "in the middle" stroke
	lt(t)
	t.pen = False
	fd(t , 2/5 * h)
	lt(t)
	fd(t, (8/5*  h * math.tan((90-theta)/180*math.pi))+ h/5) # getting it on the floor and a little away from the 


