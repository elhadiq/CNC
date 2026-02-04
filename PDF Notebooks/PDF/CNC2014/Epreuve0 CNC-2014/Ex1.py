#Epreuve_Zero 2014

import math

def f(x):
    return math.log(x)-x**3 +4

def secante_rec(xn_1, xn, f, epsilon):
    if(math.fabs(xn_1 - xn) <= epsilon):
        return xn
    else:
        return secante_rec(xn, xn - (xn - xn_1)/(f(xn) - f(xn_1))*f(xn) , f, epsilon)
        

def secante_rec(xn_1, xn , f, epsilon):
    xn1= xn - (xn - xn_1)/(f(xn) - f(xn_1))*f(xn) 
    while math.fabs(xn1 - xn_1) > epsilon :
        xn_1=xn
        xn=xn1
        xn1= xn - (xn - xn_1)/(f(xn) - f(xn_1))*f(xn) 
        
    return xn1
        
    
xa = 1
xb = 2
epsilon = 10**-10

x0 = secante_rec(xa, xb, f, epsilon)
print("-recu--  Abscisse d'un zéro de log(x)-x^3+4 dans [%d;%d] : %.20f" % (xa, xb, x0))
print(f(x0))


x0 = secante_iter(xa, xb, f, epsilon)
print("-iter--  Abscisse d'un zéro de log(x)-x^3+4 dans [%d;%d] : %.20f" % (xa, xb, x0))
print(f(x0))