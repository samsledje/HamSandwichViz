import numpy as np
from matplotlib import pyplot as plt
from shapely.geometry import Point, LineString
from GeomUtils import *

def prepare_axis(min_x=-10,max_x=10,min_y=-10,max_y=10):
    plt.grid(True,which='major')
    ax = plt.gca()
    ax.set_xlim(min_x,max_x)
    ax.set_ylim(min_y,max_y)
    plt.xticks(np.arange(min(np.array(ax.get_xlim())), max(np.array(ax.get_xlim()))+1, 1.0))
    plt.yticks(np.arange(min(np.array(ax.get_ylim())), max(np.array(ax.get_ylim()))+1, 1.0))

def plot_line(L, linestyle='--', color='b'):
    """Add line to axis
    
    Arguments:
        L {GeomUtils.Line}
    """
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = L.b + L.m * x_vals
    plt.plot(x_vals, y_vals, ls=linestyle, color=color)

def plot_line_segment(L, linestyle='-', color='b'):
    """Add line segment to axis
    
    Arguments:
        L {GeomUtils.LineSegment}
    """
    plt.plot([L.p1.x,L.p2.x],[L.p1.y,L.p2.y], ls=linestyle, color=color, linewidth=4)

def plot_point(P, marker='o', color='b'):
    """Add point to axis
    
    Arguments:
        P {shapely.geometry Point}
    """
    plt.plot(P.x,P.y, marker=marker, color=color)

def plot(S):
    """Plots an array of point or line objects
    
    Arguments:
        S {list} -- Elements of S must be sympy.geometry.Point or sympy.geometry.Line
    """

    for element in S:
        if type(element) == type(Point(0,0)):
            plot_point(element)
            plt.pause(0.5)
        elif type(element) == type(Line(Point(0,0),Point(0,1))):
            plot_line(element)
        else:
            raise TypeError(f'{element} is not a Point or Line, it is a {type(element)}')

    plt.axis('scaled')
    plt.show()


