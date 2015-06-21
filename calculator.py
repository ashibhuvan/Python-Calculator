# Script Name	: calculator.py
# Author		: Asish Mehta
# Created		: 21 June 2015
# Last Modified	: 
# Version		: 1.0

#Functions
#Pythagorean Theorem
#Law of gravitation
#Quadratic Function
import math

def pythag(c,a):
	first=((c**2)-(a**2))
	final = math.sqrt(first)
	return math.sqrt(first)
def gravity(m1,m2,r):
	constant = 6.67*(10**-11)
	firstpart = constant * m1 * m2
	bottom = r**2
	return firstpart/bottom


print "Welcome to the calculator"
print "Press 1 for Pythagorean Theorem \nPress 2 for Law of Gravitation \nPress 3 for quadratic function"
x=int(raw_input("-->"))

if x==1:
	print "Enter the hypotenus and 1 side"
	hello = int(raw_input("C:"))
	bye = int(raw_input("Side"))
	print "The other side is %s " % pythag(hello,bye)
	
elif x==2:
	print "Please enter mass 1, mass2, and the radius"
	mass1 = int(raw_input("Mass 1:"))
	mass2 = int(raw_input("Mass 2:"))
	distance = int(raw_input("Distance:"))
	print "Your force is %s" % gravity(mass1,mass2,distance)

elif x==3
	Print "Please enter a, b, and c"
	a = int(raw_input("A:"))
	b = int(raw_input("B:"))
	c = int(raw_input("C:"))
else
	print "your a retard"