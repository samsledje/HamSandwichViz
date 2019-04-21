import sys
import matplotlib.pyplot as plt
from shapely.geometry import Point
from Cuts import LinearPlanarCut
from IOUtils import *
from GeomUtils import *
from PlotUtils import *

def main(args):
    try:
        point_file = args[1]
    except IndexError:
        point_file = None
    
    plt.ion()
    plt.show()

    NewCut = HamInstance(point_file,0.5)
    LPC = LinearPlanarCut()
    LPC.median_intersection_cut(NewCut)
    check_save(NewCut)

if __name__ == '__main__':
    main(sys.argv)
