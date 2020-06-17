## TODO improve so that it has no oscillation at half length

from vpython import *
clicked = False
damping = False
# Defining various functions to be used along the program. The arguments are:
	# M --> Mass; L --> Length; B --> Breadth; x --> Distance from one end to the axis of oscillaton.

def barMI(M,L,B,x):			# Function to find the Moment of Inertia of the bar
	a = M * (L**2 + B**2)/12
	b = M * ((L/2) - x)**2
	I = a + b
	return I

def barTime(M,L,B,x,g):		# Function to find the Time Period of oscillation
	I = barMI(M,L,B,x)
	if damping:			# Damping should be a global variable
		z = M * g * abs((L/2) - x + 5e-6)
	else:
		z = M * g * abs((L/2) - x)
	T = 2 * pi * sqrt(I/z)
	return T,I

def clicker(evt):
	global clicked
	clicked = True

def barSim(M,L,B,x,A,g):		# Function to simulate oscillation
	t = 0
	dt = 0.01
	T,I = barTime(M,L,B,x,g)	# Fetching time period and MOI
	w = 2*pi / T			# Calculate the angular frequency
	POSy = abs((L/2)-x)
	POS = vec(0,POSy,-0.4*B)
	AOS = vec(0,0,0.8*B)
	ampli = radians(A) # A/((L/2)+POSy) is to be used if we have to use arc length as amplitude
	theta = -(ampli) # Initial angular position
	

	# Graphics
	scene.width = 600
	scene.height = 600
	scene.title = "<b style='margin-bottom:2pt;'>Bar Pendulum Simulation</b>"
	zbar = box(pos=vector(0,0,0),size=vector(B,L,0.1*B),color=color.white,texture=textures.metal) # Bar pendulum
	zarrow = arrow(pos=POS, axis=AOS, shaftwidth=0.25*B, color=vec(0.5,0.5,0.5)) # Axis
	text_label = label(pos=vec(0.3*L,0.4*L,0), text='0.0' ) # Label Text
	T_text = ""	# To display the time period in text box
	Click_text = label(pos=vec(-0.35*L,0.4*L,0), text="Click here to\nview the x-T\ngraph of the bar" )
	scene.bind('click', clicker)
	zbar.rotate(angle=-(ampli), axis=AOS, origin=POS) # Setting initial position of bar
	rate(100)
	while True:
		rate(100)
		theta1 = theta				# Initial position
		if damping:
			theta = ampli * e**(-0.00062*t) * sin(w*t - (pi/2))	# New position
		else:
			theta = ampli * sin(w*t - (pi/2))	# New position
		dtheta = theta - theta1		# Angular displacement (difference)
		zbar.rotate(angle=dtheta, axis=AOS, origin=POS)	# Rotating the bar
		if round(t,2) == round(T,2):
			T_text = "%0.2f s"%(T)
		text_label.text = "t = %0.2f s\nI = %0.5f kgm2\nT = %s"%(t, I, T_text) # Display the data
		t=t+dt
		if clicked:
			break

	# Plot the curve
	scene.delete()
	scene.title = "<b style='margin-bottom:2pt;'>x-T CURVE OF BAR PENDULUM<b>"
	xlist = list(arange(0,L,(L/100)))[1:]		# Creating array of x without 0
	xlist.remove(L/2)			# Removing L/2 as there is no oscillation
	gd = graph(ymax =barTime(M,L,B,xlist[int((len(xlist)-1)/2)]*0.9999,9.8)[0], xmin=1e-5, xmax=max(xlist)*0.99,
		xtitle="Distance of suspension point from an end, x\t\t(m)",
		ytitle="Time Period, T\t\t(s)") 
	f1 = gcurve(color=vec(0.5,0.5,0.5))
	for x in xlist:
		T = barTime(M,L,B,x,g)[0]
		f1.plot(x,T)
	f1.plot((L/2),1e8)
