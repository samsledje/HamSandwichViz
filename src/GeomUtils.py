from sympy.geometry import Point, Line

def compute_dual_line(P):
    """Compute dual of a point
    
    Arguments:
        P {Point}
    """
    m = P[0]
    b = P[1]
    return Line(Point(0,-b), Point(1,-b+m))

def primitive_1(H, i, j, k):
    pass

