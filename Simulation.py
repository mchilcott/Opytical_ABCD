from Elements import *
from Propagator import *

import numpy as np
import matplotlib.pyplot as plt


p = OpticalPath()
p.addElement(FreeSpace(3))
p.addElement(DielectricSlab(1.0, 2, 5*2))
p.addElement(FreeSpace(2))
p.addElement(ThinLens(10))
p.addElement(FreeSpace(10))

for theta in [0,0.01, 0.03, -0.01, -0.03]:

    ray = p.trace(np.matrix([[x], [theta]]))
    plt.plot(ray[:,1], ray[:,0])
    print ray

plt.show()
