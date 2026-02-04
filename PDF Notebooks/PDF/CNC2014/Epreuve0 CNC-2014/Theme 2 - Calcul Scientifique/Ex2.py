#Epreuve_Zero 2014

#Exercice 2: Thème Calcul scientifique

#recherchant le zéro d’une fonction
#A: Méthode de la sécante
import math


def f(x):
    return math.log(x)-x**3+4
    
    
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
print("Récursivité:   Abscisse d'un zéro de log(x)-x^3+4 dans [%d;%d] : %.18f" % (xa, xb, x0))
print(f(x0))

print('-------------------------------------------------------')
x0 = secante_iter(xa, xb, f, epsilon)
print("Iteration:  Abscisse d'un zéro de log(x)-x^3+4 dans [%d;%d] : %.18f" % (xa, xb, x0))
print(f(x0))

#B: Méthode Regula Falsi (méthode de la fausse position)
def falsePos(f,a,b):
    eps=1e-10
    itmax=1000
    x=a ; fa=f(x)
    if fabs(fa)==0 : return x
    x=b ; fb=f(x)
    if fabs(fb)==0 : return x
    
    if fa*fb>0 : return   #inteval ne contient pas de sol
    
    #for i in range(1,itmax+1):
    while True:
        #x=(a*fb-b*fa)/(fb-fa)
        x=a-((a-b)/(fa-fb))*fa
        fx=f(x)
        if fa*fx>0 :
            dx=x-a
            a=x
            fa=fx
        else:
            dx=b-x
            b=x
            fb=fx
        
        if fabs(dx)<=eps+fabs(x) or fabs(fx)<=eps: return x
    
    print("Maximum d'iteration ")
    
    

a=1
b=2
x0=falsePos(f,a,b)
print(x0)
