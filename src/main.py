import sys
import matplotlib.pyplot as plt
from shapely.geometry import Point
from Cuts import LinearPlanarCut
from IOUtils import *
from GeomUtils import *
from PlotUtils import *

def main(args):

    NewCut = HamInstance(args[1],1)
    LPC = LinearPlanarCut()
    #LPC.cut(NewCut)
    plt.ion()
    plt.show()
    for p,d in zip(NewCut.red_points, NewCut.red_duals):
        plot_point(p, color='r')
        plt.draw()
        plt.pause(0.5)
        plot_line(d, color='r')
        plt.draw()
        plt.pause(0.5)
    for p,d in zip(NewCut.blue_points, NewCut.blue_duals):
        plot_point(p, color='b')
        plt.draw()
        plt.pause(0.5)
        plot_line(d, color='b')
        plt.draw()
        plt.pause(0.5)
    LPC.show_median_intersection(NewCut)
    input()

if __name__ == '__main__':
    main(sys.argv)
