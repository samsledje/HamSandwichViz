'''
Created on Apr 4, 2019

@author: Burt
'''
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
#from builtins import input
#from pip._vendor.distlib.compat import raw_input

points_red = [] #This is for the first set of points
points_blue = [] #This is for the second set of points

def start_input():
    red_input()

def red_input():
    print("Enter in a value for the red points")
    
    x = input("Enter an X coordinate:     ")
    y = input("Enter a Y coordinate:      ")
    
    x = int(x)
    y = int(y)
    
    p = (x,y)
    print("Adding " + "(" + str(x) + "," + str(y) + ")" + " to red points")
    points_red.append(p)
        
    if len(points_red) < 3:
        red_input()
    else:
        print("Would you like to enter an additional red point?")
        print("[y] Enter another red point")
        print("[n] Continue to blue points")
        user_choice = input().strip()
        if user_choice == "y":
            print("You said yes!")
            red_input()
        elif user_choice == "n":
            print("You said no!")
            blue_input()
        else:
            print("We couldn't understand your response: " + user_choice)
            print("Let's try entering in another red point...")
            red_input()

def blue_input():
    print("Enter in a value for the blue points")
    
    x = input("Enter an X coordinate:     ")
    y = input("Enter a Y coordinate:     ")
    
    x = int(x)
    y = int(y)
    
    p = (x,y)
    print("Adding " + "(" + str(x) + "," + str(y) + ")" + " to blue points")
    points_blue.append(p)
        
    if len(points_blue) < 3:
        blue_input()
    else:
        print("Would you like to enter an additional red point?")
        print("[y] Enter another blue point")
        print("[n] Start Ham Sandwich")
        user_choice = input().strip()
        if user_choice == "y":
            print("You said yes!")
            red_input()
        elif user_choice == "n":
            print("You said no!")
        else:
            print("We couldn't understand your response: " + user_choice)
            print("Let's try entering in another blue point...")
            blue_input()

start_input()

polygon1 = Polygon(points_red)
polygon2 = Polygon(points_blue)
plt.plot(*polygon1.exterior.xy)
plt.plot(*polygon2.exterior.xy)
plt.show()
