
class Ham_Cut:
    """General Ham Sandwich Cut Class
    """

    def __init__(self, W, B, dimension):
        """General Ham Sandwich Cut
        
        Arguments:
            W {Set of points} -- White points
            B {Set of points} -- Black points
            dimension {int} -- Dimension of points
        """
        self.W = W
        self.B = B
        self.dimension = dimension

    def calculate_cut(self):
        raise NotImplementedError


class Ham_NLogN(Ham_Cut):
    """O(nlogn) time algorithm for ham sandwich cuts in the plane
    """
    pass

class Ham_N(Ham_Cut):
    """O(n) time algorithm for ham sandwich cuts in the plane
    """

    pass

class Ham_Sandwich(Ham_Cut):
    """Ham Sandwich Cut in D-Dimensions
    """

    pass