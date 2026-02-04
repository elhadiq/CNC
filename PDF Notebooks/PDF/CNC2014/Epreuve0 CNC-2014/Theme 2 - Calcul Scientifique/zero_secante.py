# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 21:28:18 2014

@author: D.Malka
"""

import numpy as np
import matplotlib.pyplot as plt
from math import fabs

def zero_secante(f,x1,x2):
    '''
    f : fonction, type function
    x1 : point d'intersection avec courbe de f, type : float
    x2 : point d'intersection avec courbe de f, type : float
    '''
    #equation de la secante y=ax+b
    a=(f(x2)-f(x1))/(x2-x1)
    b=f(x2)-a*x2
    zero=-b/a
    return zero
    
def methode_secante(f,u0,u1,epsilon):
    '''
    f fonction dont on cherche un zero
    u0 : point d'intersection 0 avec la secante
    u1 : point d'intersection 1 avec la secante
    epsilon : "precision" sur le zero retourne
    '''
    u=[u0,u1]#tableau contenant les valeurs approchees des 0 de f
    
    i=0
    while fabs(u[i+1]-u[i])>epsilon:
        suivant=zero_secante(f,u[i+1],u[i])
        u.append(suivant)
        i+=1
        
    return u
    

def secante(f,a,b,epsilon=10**-10):
    '''
     f fonction dont on cherche un zero
     epsilon : "precision" sur le zero retourne
    '''
   
    x=b
    while fabs(x-a)> epsilon:
        x=a
        a = a-(f(a)*(b-a))/(f(b)-f(a))

        
    return x
    
    
    
#TEST
f=lambda x:np.log(x)-x**3 +4
'''
u0=float(input("Point d'intersection 0 : u0 = ")) 
u1=float(input("Point d'intersection 1 : u1 = "))
epsilon=float(raw_input("Precision : epsilon = "))  
'''
u0=1
u1=2
epsilon=10**-10

liste=methode_secante(f,u0,u1,epsilon)
print(liste)

#GRAPHE
def f(x):
    return np.log(x)-x**3 +4

x=np.linspace(-1,3,1000)
y=f(x)

plt.plot(x,y,'r-',linewidth=3) 


for i in range(1,len(liste)):
    x1=liste[i-1]
    x2=liste[i]
    a=(f(x2)-f(x1))/(x2-x1)
    b=f(x2)-a*x2
    y=a*x+b
    plt.plot(x,y,label='secante'+str(i))

plt.legend(loc=1,fontsize='small')
plt.grid()
#plt.savefig('methode_secante.pdf',format='pdf')
plt.show()
    