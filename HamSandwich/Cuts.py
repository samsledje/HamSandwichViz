import math
from random import choice
from HamSandwich.GeomUtils import *
from HamSandwich.PlotUtils import *
from shapely.geometry import Point

class LinearPlanarCut:
    def __init__(self, alpha=1/32, epsilon=1/8):
        self.alpha = alpha
        self.epsilon = epsilon

    def cut(self, ham_instance):
        self.ham_instance = ham_instance

        l, r = find_x_bounds(ham_instance.all_points)
        curr_interval = Interval(l-1,r+1)
        curr_red_lines = ham_instance.red_duals
        curr_blue_lines = ham_instance.blue_duals
        red_p = math.floor((len(ham_instance.red_points) + 1) / 2)
        blue_p = math.floor((len(ham_instance.blue_points) + 1) / 2)
        c = self._get_C()
        #self._get_intervals(curr_interval)
        #for i,j in zip(curr_red_lines, curr_blue_lines):
        #    plot_point(Intersection(i,j), color='g')

    def median_intersection_cut(self, ham_instance):
        self.ham_instance = ham_instance
        x_min, x_max = find_x_bounds(self.ham_instance.all_points)
        y_min, y_max = find_y_bounds(self.ham_instance.all_points)
        
        self.interval = Interval(x_min-5, x_max+5)
        plt.title('Ham Sandwich Cut')
        prepare_axis(x_min-5, x_max+5,y_min-5,y_max+5)

        plot_points_and_duals(self.ham_instance)

        red_intersections = []
        for i in range(len(self.ham_instance.red_duals)):
            for j in range(len(self.ham_instance.red_duals)):
                if (not i == j) and (i < j):
                    d1 = self.ham_instance.red_duals[i]
                    d2 = self.ham_instance.red_duals[j]
                    new_inter = Intersection(d1,d2)
                    if new_inter.x == np.inf:
                        pass
                    else:
                        red_intersections.append(new_inter)
        red_intersections.sort(key = lambda I: I.x)
        
        red_med_levels = [Point(self.interval.l, self._find_median_level(self.interval.l, self.ham_instance.red_duals))]
        red_med_levels.extend([Point(i.x, self._find_median_level(i.x,self.ham_instance.red_duals)) for i in red_intersections])
        red_med_levels.extend([Point(self.interval.r, self._find_median_level(self.interval.r, self.ham_instance.red_duals))])

        for i in range(0,len(red_med_levels)-1):
            plot_line_segment(LineSegment(red_med_levels[i], red_med_levels[i+1]), color='r')
            plt.pause(0.5)

        red_med_linestring = LineString(red_med_levels)

        blue_intersections = []
        for i in range(len(self.ham_instance.blue_duals)):
            for j in range(len(self.ham_instance.blue_duals)):
                if (not i == j) and (i < j):
                    d1 = self.ham_instance.blue_duals[i]
                    d2 = self.ham_instance.blue_duals[j]
                    new_inter = Intersection(d1,d2)
                    if new_inter.x == np.inf:
                        pass
                    else:
                        blue_intersections.append(new_inter)
        blue_intersections.sort(key = lambda I: I.x)
        
        blue_med_levels = [Point(self.interval.l, self._find_median_level(self.interval.l, self.ham_instance.blue_duals))]
        blue_med_levels.extend([Point(i.x, self._find_median_level(i.x,self.ham_instance.blue_duals)) for i in blue_intersections])
        blue_med_levels.extend([Point(self.interval.r, self._find_median_level(self.interval.r, self.ham_instance.blue_duals))])
        
        for i in range(0,len(blue_med_levels)-1):
            plot_line_segment(LineSegment(blue_med_levels[i], blue_med_levels[i+1]), color='b')
            plt.pause(0.5)

        blue_med_linestring = LineString(blue_med_levels)
        ham_points = red_med_linestring.intersection(blue_med_linestring)
        if isinstance(ham_points, Point):
            ham_points = [ham_points]
        ham_cuts = [compute_dual_line(hp, constant=self.ham_instance.plot_constant) for hp in ham_points]
        for hp in ham_points:
            plot_point(hp,color='c',marker='*',size=20)

        input('Press Enter to View the Ham Sandwich Cut')
        plt.gca().clear()
        plt.title('Ham Sandwich Cut')
        prepare_axis(x_min-5,x_max+5,y_min-5,y_max+5)
        for hp in ham_points:
            plot_point(hp, color='c',marker='*',size=20)
        plot_point_set(self.ham_instance)
        for hc in ham_cuts:
            plot_line(hc,color='c',linestyle='-',)
            plt.pause(0.5)
   

    def _get_C(self):
        return self.alpha

    def _get_intervals(self, interval):
        # returns two new intervals
        intersections = []
        for i in self.ham_instance.intersections:
            if interval.l <= i.x and interval.r >= i.x:
                intersections.append(i)
        random_intersection = choice(intersections)
        return Interval(interval.l,random_intersection.x), Interval(random_intersection.x,interval.r)

    def _odd_intersection(self, interval):
        l = interval.l
        r = interval.r

        lmr = self._find_median_level(l, self.ham_instance.red_duals)
        lmb = self._find_median_level(l, self.ham_instance.blue_duals)

        rmr = self._find_median_level(r, self.ham_instance.red_duals)
        rmb = self._find_median_level(r, self.ham_instance.blue_duals)

        return (lmr - lmb)*(rmr - rmb) < 0

    def _find_median_level(self,x,lines):
        y_vals = [line.b + (x * line.m) for line in lines]
        y_vals.sort()
        med = math.floor((len(y_vals) + 1) / 2)
        return y_vals[med-1]

