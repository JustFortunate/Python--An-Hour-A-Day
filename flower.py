world.clear()
import math
from swampy import *
bob = Turtle()

def arc(t, r, theta):
	circumference = 2  * math.pi * r
	n = int (circumference/3) +1
	step_length = circumference * (theta /360 )/n
	step_angle = theta / n
	for _ in range(n):
		fd(t, step_length)
		lt(t, step_angle)
bob.delay =0.001

def leaf(t, length=301, alpha=30, bearing = 0):
	"""Draws a leaf that has :
	t: turtle
	l: length
	alpha: internal_angle
	"""
	lt(t, bearing)
	
	arc(t, (length/2) /math.sin(alpha/2), alpha)
	lt(t, 180 - alpha)
	arc(t, (length/2) /math.sin(alpha/2), alpha)

def flower(t,n ,radius = 500):
	"""
	Draw a flower with n petals and size radius of. 
	"""
	alpha = 360/n
	for i in range(0, n):
		leaf(t, radius, alpha, alpha)
bob.delay = 0.1
leaf(bob, 100, 108, 0)

world.clear()
bob = Turtle()
bob.delay = 0.1
def polygon(t, n, s):
	for i in range(n):
		fd(t, s)
		lt(t, 360/n)

world.clear()
bob = Turtle()
import math
bob.delay = 0.1
def polygon(t, n, s):
	theta = 360/n
	theta_rad = 2 * math.pi /n
	for i in range(n):
		fd(t, s)
		lt(t, theta)
	
	lt(t, 90*(n-2)/n)
	fd(t, (s/(2*math.sin(theta_rad/2))))
	lt(t, theta/2 + theta)
	fd(t, (s/(2*math.sin(theta_rad/2))))
	t.pen = False


polygon(bob, 5, 50)
