from matplotlib import pyplot as plt
from sympy.geometry import Point, Line

def plot_line(L, axis, marker=None, color='b'):
    """Add point to axis
    
    Arguments:
        P {sympy.geometry Line}
        axis {pyplot axis}
    """
    p1, p2 = L.points
    axis.add_line(plt.Line2D((p1[0],p2[0]),(p1[1],p2[1]), marker=marker, color=color))

def plot_point(P, axis, marker='.', color='b'):
    """Add point to axis
    
    Arguments:
        P {sympy.geometry Point}
        axis {pyplot axis}
    """
    plt.plot(P[0],P[1], marker=marker, color=color)

def plot(S):
    """Plots an array of point or line objects
    
    Arguments:
        S {list} -- Elements of S must be sympy.geometry.Point or sympy.geometry.Line
    """
    plt.axes()
    ax = plt.gca()

    for element in S:
        if type(element) == type(Point(0,0)):
            plot_point(element, ax)
        elif type(element) == type(Line(Point(0,0),Point(0,1))):
            plot_line(element, ax)
        else:
            raise TypeError(f'{element} is not a Point or Line, it is a {type(element)}')

    plt.axis('scaled')
    plt.show()


