from Elements import *
from Propagator import *

import numpy as np
import matplotlib.pyplot as plt


p = OpticalPath()
p.addElement(FreeSpace(3))
p.addElement(DielectricSlab(1, 2, 5*2))
p.addElement(FreeSpace(2))
p.addElement(ThinLens(10))
p.addElement(FreeSpace(30))

style = ['r', 'b', 'g'].__iter__()
fig = [1,2,3].__iter__()


plt.figure()

for x in [-0.05, 0, 0.05]:
    s = style.next()
    plt.subplot(3, 1, fig.next())
    
    for theta in [0,0.01, 0.03, -0.01, -0.03]:

        ray = p.trace(np.matrix([[x], [theta]]))
        plt.plot(ray[:,1], ray[:,0], s)

    plt.ylim((-0.5, 0.5))



##################
# Astigmatic beam feedback
count = 0
for col_len in np.linspace(4,12,100):
    
    q = OpticalPath()
    
    q.addElement(FreeSpace(col_len))
    q.addElement(ThinLens(10))
    q.addElement(FreeSpace(30))
    q.addElement(ThinLens(10))
    q.addElement(FreeSpace(col_len))
    
    
    fast = 0.1
    slow = 0.3
    theta = 0.1
    
    plt.figure()
    
    ray = q.trace(np.matrix([[fast], [theta*3]]))
    plt.plot(ray[:,1], ray[:,0], 'r-.' )
    
    ray = q.trace(np.matrix([[-fast], [-theta*3]]))
    plt.plot(ray[:,1], ray[:,0], 'r-.')
    
    ray = q.trace(np.matrix([[slow], [theta]]))
    plt.plot(ray[:,1], ray[:,0], 'r')
    
    ray = q.trace(np.matrix([[-slow], [-theta]]))
    plt.plot(ray[:,1], ray[:,0], 'r')

    plt.ylim((-4, 4))
    
    plt.title("Astigmatic external cavity")
    plt.savefig(str(count) + ".png")
    count += 1
#plt.show()
