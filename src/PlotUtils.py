import numpy as np
from matplotlib import pyplot as plt
from shapely.geometry import Point, LineString
from GeomUtils import *

def prepare_axis(min_x=-10,max_x=10,min_y=-10,max_y=10):
    plt.grid(True,which='major')
    ax = plt.gca()
    min_x = int(min_x)
    max_x = int(max_x)
    min_y = int(min_y)
    max_y = int(max_y)
    ax.set_xlim(min_x,max_x)
    ax.set_ylim(min_y,max_y)
    plt.xticks(np.arange(min(np.array(ax.get_xlim())), max(np.array(ax.get_xlim()))+1, 1.0))
    plt.yticks(np.arange(min(np.array(ax.get_ylim())), max(np.array(ax.get_ylim()))+1, 1.0))
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

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

def plot_point(P, marker='o', color='b',size=5):
    """Add point to axis
    
    Arguments:
        P {shapely.geometry Point}
    """
    plt.plot(P.x,P.y, marker=marker, color=color,markersize=size)

def plot_points_and_duals(ham_instance):
    for p,d in zip(ham_instance.red_points, ham_instance.red_duals):
        plot_point(p, color='r')
        plt.draw()
        plt.pause(0.5)
        plot_line(d, color='r')
        plt.draw()
        plt.pause(0.5)
    if ham_instance.extra_red:
        plot_point(ham_instance.extra_red, color='r')
        plt.pause(0.5)
        plot_line(compute_dual_line(ham_instance.extra_red), color='r')
        plt.pause(0.5)
    for p,d in zip(ham_instance.blue_points, ham_instance.blue_duals):
        plot_point(p, color='b')
        plt.draw()
        plt.pause(0.5)
        plot_line(d, color='b')
        plt.draw()
        plt.pause(0.5)
    if ham_instance.extra_blue:
        plot_point(ham_instance.extra_blue, color='b')
        plt.pause(0.5)
        plot_line(compute_dual_line(ham_instance.extra_blue), color='b')
        plt.pause(0.5)

def plot_point_set(ham_instance):
    for p in ham_instance.red_points:
        plot_point(p, color='r')
        plt.draw()
        plt.pause(0.5)
    if ham_instance.extra_red:
        plot_point(ham_instance.extra_red, color='r')
        plt.pause(0.5)
    for p in ham_instance.blue_points:
        plot_point(p, color='b')
        plt.draw()
        plt.pause(0.5)
    if ham_instance.extra_blue:
        plot_point(ham_instance.extra_blue, color='b')
        plt.pause(0.5)
