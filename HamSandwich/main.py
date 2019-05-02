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
    cut_type = None
    while cut_type != 'e':
        cut_type = get_cut_type()
        if cut_type == 't':
            LPC.teach(NewCut)
        elif cut_type == 'c':
            LPC.cut(NewCut)
        elif cut_type == 'a':
            LPC.all_ham_cuts(NewCut)
    check_save(NewCut)

def get_cut_type():
    cut_type = input('Teach [t]\nCut [c]\nAll [a]\nExit [e]\n')
    if cut_type =='t' or cut_type == 'c' or cut_type == 'a' or cut_type == 'e':
        return cut_type
    else:
        print('Please enter a valid input.')
        return get_cut_type()

if __name__ == '__main__':
    main(sys.argv[1])
