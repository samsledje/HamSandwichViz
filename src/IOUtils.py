from shapely.geometry import Point
from PlotUtils import prepare_axis
from GeomUtils import find_x_bounds, find_y_bounds, compute_dual_line, Intersection

class HamInstance:
    def __init__(self, infile = None, plot_constant=10):
        # Read Input Points
        self.plot_constant = plot_constant
        self.red_points = []
        self.blue_points = []

        if infile is None:
            self.start_input()
        else:
            self.read_points(infile)

        # Calculate Duals
        self.red_duals = [compute_dual_line(i,self.plot_constant) for i in self.red_points]
        self.blue_duals = [compute_dual_line(i,self.plot_constant) for i in self.blue_points]

        self.all_points = self.red_points + self.blue_points
        self.all_duals = self.red_duals + self.blue_duals

        # # Compute Intersections
        # self.intersections = []
        # for i,j in zip(self.all_duals, self.all_duals):
        #     if not i == j:
        #         self.intersections.append(Intersection(i,j))

        # Prepare Plot
        self.min_x, self.max_x = find_x_bounds(self.red_points + self.blue_points)
        min_y, max_y = find_y_bounds(self.red_points + self.blue_points)
        prepare_axis(self.min_x-5,self.max_x+5,min_y-5,max_y+5)

    def start_input(self):
        self.red_input()

    def red_input(self):
        print("Enter in a value for the red points")
        
        x = input("Enter an X coordinate:     ")
        y = input("Enter a Y coordinate:      ")
        
        x = float(x)
        y = float(y)
        
        p = (x,y)
        print("Adding " + "(" + str(x) + "," + str(y) + ")" + " to red points")
        self.red_points.append(Point(p))
            
        if len(self.red_points) < 3:
            self.red_input()
        else:
            print("Would you like to enter an additional red point?")
            print("[y] Enter another red point")
            print("[n] Continue to blue points")
            user_choice = input().strip()
            if user_choice == "y":
                print("You said yes!")
                self.red_input()
            elif user_choice == "n":
                print("You said no!")
                self.blue_input()
            else:
                print("We couldn't understand your response: " + user_choice)
                print("Let's try entering in another red point...")
                self.red_input()

    def blue_input(self):
        print("Enter in a value for the blue points")
        
        x = input("Enter an X coordinate:     ")
        y = input("Enter a Y coordinate:     ")
        
        x = float(x)
        y = float(y)
        
        p = (x,y)
        print("Adding " + "(" + str(x) + "," + str(y) + ")" + " to blue points")
        self.blue_points.append(Point(p))
            
        if len(self.blue_points) < 3:
            self.blue_input()
        else:
            print("Would you like to enter an additional red point?")
            print("[y] Enter another blue point")
            print("[n] Start Ham Sandwich")
            user_choice = input().strip()
            if user_choice == "y":
                print("You said yes!")
                self.blue_input()
            elif user_choice == "n":
                print("You said no!")
            else:
                print("We couldn't understand your response: " + user_choice)
                print("Let's try entering in another blue point...")
                self.blue_input()
    
    def read_points(self, infile):
        with open(infile, 'r') as f:
            red_line = f.readline().strip().split()
            blue_line = f.readline().strip().split()
            self.red_points = [Point(float(i.split(',')[0]), float(i.split(',')[1])) for i in red_line]
            self.blue_points = [Point(float(i.split(',')[0]), float(i.split(',')[1])) for i in blue_line]