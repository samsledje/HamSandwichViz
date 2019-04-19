import math
import statistics
from GeomUtils import *

class LinearPlanarCut:
    def __init__(self, alpha=1/32, epsilon=1/8):
        self.alpha = alpha
        self.epsilon = epsilon

    def cut(self, ham_instance):
        self.ham_instance = ham_instance

        l, r = find_x_bounds(ham_instance.all_points)
        #curr_interval = Interval(l-1,r+1)
        curr_interval = Interval(-15,-10)
        curr_red_lines = ham_instance.red_duals
        curr_blue_lines = ham_instance.blue_duals
        red_p = math.floor((len(ham_instance.red_points) + 1) / 2)
        blue_p = math.floor((len(ham_instance.blue_points) + 1) / 2)
        c = self._get_C()
        print(self._odd_intersection(curr_interval))

    def _get_C(self):
        return self.alpha

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

