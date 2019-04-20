import math
from random import choice
import statistics
from GeomUtils import *
from PlotUtils import *

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

    def show_median_intersection(self, ham_instance):
        self.ham_instance = ham_instance
        x_min, x_max = find_x_bounds(self.ham_instance.all_points)
        self.interval = Interval(x_min-1, x_max+1)
        #######
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
        for i in range(0,len(red_med_levels)-2):
            plot_line_segment(LineSegment(red_med_levels[i], red_med_levels[i+1]), color='r')
        #######
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
        return statistics.median(y_vals)

