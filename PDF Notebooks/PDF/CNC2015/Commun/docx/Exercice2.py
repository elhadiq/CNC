import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


#Variables globales
a,b = -3.0,-1.0

def F(Z,t) :
    [y,dy]=Z
    return dy, a*y+b*dy
    

t=np.linspace(0,5,100)
s=odeint(F,[0.05,0.7],t)

plt.plot(t,s[:,0])
plt.grid()
plt.show()
