from shapely.geometry import Point
from PlotUtils import prepare_axis
from GeomUtils import find_x_bounds, find_y_bounds, compute_dual_line, Intersection, random_point_set

class HamInstance:
    def __init__(self, infile = None, plot_constant=10):
        # Read Input Points
        self.plot_constant = plot_constant
        self.red_points = []
        self.blue_points = []
        self.extra_red = False
        self.extra_blue = False

        if infile is None:
            self.start_input()
        else:
            self.read_points(infile)

        # Make point sets odd
        if len(self.red_points) % 2 == 0:
            self.extra_red = self.red_points.pop()
        if len(self.blue_points) % 2 == 0:
            self.extra_blue = self.blue_points.pop()

        # Calculate Duals
        self.red_duals = [compute_dual_line(i,self.plot_constant) for i in self.red_points]
        self.blue_duals = [compute_dual_line(i,self.plot_constant) for i in self.blue_points]

        self.all_points = self.red_points + self.blue_points
        if self.extra_red:
            self.all_points.append(self.extra_red)
        if self.extra_blue:
            self.all_points.append(self.extra_blue)
        #self.all_duals = self.red_duals + self.blue_duals

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
        check = input('You have not provided a point file. Do you want to input points manually [i] or use random points [r]? ')
        if check == 'i':
            self.red_input()
        elif check == 'r':
            self.random_input()
        else:
            print('Please enter a valid input.')
            self.start_input()

    def random_input(self):
        check = input('How many red points? ')
        try:
            if str(int(check)) == check:
                n_reds = int(check)
                check = input('How many blue points? ')
                try:
                    if str(int(check)) == check:
                        n_blues = int(check)
                        reds = random_point_set(n_reds)
                        blues = random_point_set(n_blues)
                        write_point_file('pointsets/randpoints.txt', reds, blues)
                        self.read_points('pointsets/randpoints.txt')
                    else:
                        print('Please enter a valid integer.')
                        self.random_input()
                except:
                    print('Please enter a valid integer.')
                    self.random_input()

            else:
                print('Please enter a valid integer.')
                self.random_input()
        except:
            print('Please enter a valid integer.')
            self.random_input()

    def red_input(self):
        print("Enter in a value for the red points")
        
        x = input("Enter an X coordinate:     ")
        y = input("Enter a Y coordinate:      ")
        
        x = float(x)
        y = float(y)
        
        p = (x,y)
        print("Adding " + "(" + str(x) + "," + str(y) + ")" + " to red points")
        self.red_points.append(Point(p))
        
        print("Would you like to enter an additional red point?")
        print("[y] Enter another red point")
        print("[n] Continue to blue points")
        user_choice = input().strip()
        
        if user_choice == "y":
            self.red_input()
        elif user_choice == "n":
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
            
        print("Would you like to enter an additional red point?")
        print("[y] Enter another blue point")
        print("[n] Start Ham Sandwich")
        user_choice = input().strip()
        if user_choice == "y":
            self.blue_input()
        elif user_choice == "n":
            print("Visualizing...")
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

    def write_points(self, outfile):
        with open(outfile, 'w+') as f:
            full_reds = self.red_points
            full_blues = self.blue_points
            if self.extra_red:
                full_reds.append(self.extra_red)
            if self.extra_blue:
                full_blues.append(self.extra_blue)
            write_point_file(outfile, full_reds, full_blues)

def write_point_file(filename, red_points, blue_points):
    with open(filename, 'w') as f:
        for i in red_points:
            f.write('{},{}'.format(i.x,i.y))
            f.write(' ')
        f.write('\n')
        for i in blue_points:
            f.write('{},{}'.format(i.x,i.y))
            f.write(' ')

def check_save(ham_instance):
    do_save = input('Do you want to save this point set? [y] [n] ')
    if do_save == 'y':
        fname = input('In what file? ')
        ham_instance.write_points(fname.strip())
    elif do_save == 'n':
        pass
    else:
        print('Could not read your response.')
        check_save(reds,blues)
