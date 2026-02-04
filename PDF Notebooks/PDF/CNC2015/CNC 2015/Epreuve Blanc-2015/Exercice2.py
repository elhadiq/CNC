import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint,quad
#Question 1
def trapezes(f,a,b,n):
    pas=(b-a)/n
    s=0
    for k in range(1,n):
        s=s+f(a+k*pas)+f(a+(k+1)*pas)

    return (pas/2)*s
    
def trapezes2(f,a,b,n):
    pas=(b-a)/n
    s=0
    for k in range(1,n):
        s=s+f(a+k*pas)
    
    return pas*((f(a)+f(b))/2 + s)

print (quad(np.sin,0,np.pi)) 
print (trapezes(np.sin,0,np.pi,10000))
print (trapezes2(np.sin,0,np.pi,10000))

#Question 3
def euler(f,a,b,y0,n):
    t=np.linspace(a,b,n+1)
    y=np.zeros(n+1) # tableau de n+1 éléments
    y[0]=y0
    h=(b-a)/n
    for k in range(n):
        y[k+1]=y[k]+h*f(t[k],y[k])
    return(t,y)

#Question 4 et 5
'''
f=lambda t,y: 3*t*y+4      
(t,y)= euler(f,0,1, 1,50)
print(t,y)
plt.plot(t,y)
plt.grid()
plt.show()
'''

#Question 6
'''
t=np.arange(0,24.5,0.5)
phi = lambda y,t:(np.exp(-0.25*t))-y
s = odeint(phi,20,t)
print(s)
plt.plot(t,s)
plt.xlabel('Temps en h')
plt.ylabel('Température en °c')
plt.grid()
plt.show()
'''

