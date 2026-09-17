#Nelson Davis
#September 17th
#P2LAB1
#The program will calculate the diameter and area of a circle
import math

#Get radius from user
radius = float(input("What is the radius of a circle? "))
print()

#calculate diameter
diameter = 2 * radius

#Display diameter with 1 decimal point
print(f"The diameter of the circle is {diameter:.1f}\n")

#Calculate circumference
circumference = 2 * math . pi * radius
 
#Display circumference with 2 decimal places
print(f"The circumference of a circle is {circumference:.2f}\n")

#Calculate the area
area = math. pi * radius**2

#Display arrea with 3 decimal places
print(f"The area of the circle is {area:.3f}")
