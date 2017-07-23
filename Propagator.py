import numpy as np

class OpticalPath:
    """A series of optical elements"""

    elements = []
    
    def __init__ (self):
        elements = []

    def addElement(self, elem):
        self.elements.append(elem)

    def trace(self, pos):
        """Trace a ray through the path in the paraxial approximation.
        
        The start position (pos) should be of the form [x, theta],
        where x and theta are the offset and angle from the optical
        axis.

        Return value is an array of x, z coordinates of the ray path

        """

        z = 0.0
        path = np.matrix([[pos[0], z]])

        for e in self.elements:
            z += e.length()
            pos = e.abcd() * pos

            path = np.concatenate((path, [[pos[0], z]]))

        return path
            
                         
