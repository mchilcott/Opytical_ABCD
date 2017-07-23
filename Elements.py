import numpy as np

from OpElement import OpElement


# NB: Matricies taken from
#       Laser Resonators and Beam Propagation
#       Hodgson and Weber
 

#######################################
#
##     Simple Elements
###
#######################################



class FreeSpace (OpElement):
    """
    Propagation through free space.
    """

    """Length of space"""
    l = 0
    
    def __init__ (self, length):
        """Free space of given length
        """
        self.l = 1.0 * length

    def abcd (self):
        return np.matrix(
            [
                [1, (self.l)],
                [0, 1]
            ]
        )

    def length (self):
        return self.l


class SphericalInterface (OpElement):
    """A spherical dielectric interface
    """

    n_1 = 1
    n_2 = 1.5
    radius = 10

    def __init__(self, radius, n_1 = 1, n_2 = 1.5):
        """A dieletric interface from refractive index n_1 to n_2 with a
        radius of curviture centred on the n_2 side (after the
        interface)
        """
        self.radius = radius
        self.n_1 = n_1
        self.n_2 = n_2
        

    def abcd (self):
        return np.matrix(
            [
                [1, 0],
                [
                    (self.outer_n - self.inner_n)/(self.inner_n * self.radius * 1.0),
                    self.outer_n / (1.0 * self.inner_n)
                ]
            ]
        )
    
    def length (self):
        """In the paraxial approximation the interface is thin"""
        return 0

    
class PlaneInterface (OpElement):
    """A Plane dielectric interface
    """

    n_1 = 1.5
    n_2 = 1.5
    
    def __init__ (self, n_1=1.0, n_2=1.3):
        """A plane interface from refractive index n_1 to n_2
        """
        self.n_1 = 1.0
        self.n_2 = 1.3

    def abcd (self):
        return np.matrix(
            [
                [1, 0],
                [0, self.n_2 * 1.0/self.n_1]
            ]
        )
    
    def length (self):
        """Inteface is thin
        """
        return 0



##########################################
#
##    Complex Elements
###
##########################################

class ThinLens (OpElement):
    """A Thin lens. I.e. no thickness, and defined by focal length
    (negative focal length for diverging lens
    """

    f = 1.0

    def __init__ (self, f=1.0):
        """Create a thin lens with the given focal length
        """
        assert (f != 0)
        self.f = f * 1.0

    def abcd (self):
        return np.matrix(
            [
                [1,0],
                [-1.0/self.f, 1]
            ]
        )

    def length(self):
        """Thin
        """
        return 0


class DielectricSlab (OpElement):

    n_1 = 1.0
    n_2 = 1.5
    l = 0

    def __init__ (self, n_1, n_2, length):
        self.n_1 = n_1
        self.n_2 = n_2
        self.l = length

        
    def abcd (self):
        return np.matrix(
            [
                [1, self.n_1*self.l * 1.0/self.n_2],
                [0, 1]
            ]
        )
    def length (self):
        return self.l
