# Program to receive inputs
from barpendulum import barpendulum

print("Enter the following parameters of the bar pendulum (in SI Units):")
mass = float(input("\tMass: "))
length = float(input("\tLength: "))
breadth = float(input("\tBreadth: "))
x = float(input("\tDistance of the Point of Suspension from one of the ends: "))
while (x == length/2) or (x>=length) or (x==0):
	x= float(input("Enter another value for x other than half length of bar: "))
g = float(input("\t Acceleration due to gravity: "))
amplitude = float(input("\t Amplitude (in degrees): "))
while amplitude > 90:
	amplitude = float(input("\t Please give a smaller amplitude: "))
d = input("\tDo you want to consider damping? (y/n) : ")
if d == "y":
	barpendulum.damping = True
elif d == "n":
	barpendulum.damping = False
else:
	print("Unexpected input. Please enter 'y' or 'n'.")
	exit()

barpendulum.barSim(mass,length,breadth,x,amplitude,g)
