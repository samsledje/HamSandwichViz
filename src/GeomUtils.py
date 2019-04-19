from shapely.geometry import Point, LineString
class Line:
    def __init__(self, m,b):
        self.m = m
        self.b = b

class Interval:
    def __init__(self,l,r):
        self.l = l
        self.r =r

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
    return Line(constant*P.x, -1*P.y)
