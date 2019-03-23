import sys
import matplotlib.pyplot as plt
from sympy.geometry import Point, Line
from Cuts import Ham_NLogN, Ham_N, Ham_Sandwich
from GeomUtils import *
from PlotUtils import *

def main(args):

    p = Point(3,3)
    line = compute_dual_line(p)
    plot([p, line, 3])

if __name__ == '__main__':
    main(sys.argv)
