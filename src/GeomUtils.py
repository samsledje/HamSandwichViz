from shapely.geometry import Point, LineString
from numpy.linalg import det
import numpy as np

class Line:
    def __init__(self,m,b):
        self.m = m
        self.b = b

class LineSegment:
    def __init__(self,point1,point2):
        self.p1 = point1
        self.p2 = point2

    def __str__(self):
        return 'LineSegment ({},{})'.format(self.p1, self.p2)

class Interval:
    def __init__(self,l,r):
        self.l = l
        self.r =r

class Intersection:
    def __init__(self, line1, line2):
        if line1.m == line2.m:
            self.x = np.inf
            self.y = np.inf
        else:
            self.x = (line2.b - line1.b) / (line1.m - line2.m)
            self.y = line1.m * self.x + line1.b

def find_x_bounds(point_set):
    """Find min and max x
    
    Arguments:
        point_set {array of shapely.geometry.Point} -- set of points
    """
    min_x = min(point_set, key=lambda P: P.x).x
    max_x = max(point_set, key=lambda P: P.x).x
    return min_x, max_x
    
def find_y_bounds(point_set):
    """Find min and max y
    
    Arguments:
        point_set {array of shapely.geometry.Point} -- set of points
    """
    min_y = min(point_set, key=lambda P: P.y).y
    max_y = max(point_set, key=lambda P: P.y).y
    return min_y, max_y

def compute_dual_line(P, constant=1):
    """Compute dual of a point
    
    Arguments:
        P {shapely.geometry.Point}
    """
    return Line(constant*P.x, -P.y)