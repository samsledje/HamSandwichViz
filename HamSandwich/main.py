#!/usr/bin/python3
import sys
import matplotlib.pyplot as plt
from shapely.geometry import Point
from HamSandwich.Cuts import LinearPlanarCut
from HamSandwich.IOUtils import *
from HamSandwich.GeomUtils import *
from HamSandwich.PlotUtils import *

def main(file):
    try:
        point_file = file
    except IndexError:
        point_file = None
    
    plt.ion()
    plt.show()

    NewCut = HamInstance(point_file,1)
    LPC = LinearPlanarCut()
    LPC.teach(NewCut)
    #LPC.all_ham_cuts(NewCut)
    check_save(NewCut)

if __name__ == '__main__':
    main(sys.argv[1])
