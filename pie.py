# Here is a working code that draws a pie of side n of length s

world.clear()
bob = Turtle()
import math
bob.delay = 0.1
def pie(t, n, s):
	theta = 360/n
	theta_rad = 2 * math.pi /n
	for i in range(n):
		fd(t, s)
		lt(t, theta)
	
	lt(t, 90*(n-2)/n)
	fd(t, (s/(2*math.sin(theta_rad/2))))
	lt(t, 180 -theta)

	fd(t, (s/(2*math.sin(theta_rad/2))))
	for _ in range(n-2):
		t.pen = False
		bk(t, (s/(2*math.sin(theta_rad/2))))
		t.pen = True
		rt(t,  theta)
		fd(t, (s/(2*math.sin(theta_rad/2))))
	


pie(bob, 5, 50)