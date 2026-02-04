def falsePos(f,a,b,n=1000,eps=1e-10):
    x=a ; fa=f(x)
    if fabs(fa)==0 : return (x,0)
    x=b ; fb=f(x)
    if fabs(fb)==0 : return (x,0)
    
    if fa*fb>0 : return (x,1)
    
    for i in range(1,n+1):
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
        
        if fabs(dx)<=eps+fabs(x) or fabs(fx)<=eps: 
           return (x,0)
    
    print("Maximum d'iteration ")
    return(x,0)
  
#autre version
def falsePos2(f,a,b,n):
    for i in range(n):
        m=a-((a-b)/(f(a)-f(b)))*f(a)
        #m=(a*f(b)-b*f(a))/(f(b)-f(a))
        if f(a)*f(m)>0:
            a=m
        else:
            b=m
    return m
    
def falsePos3(f,a,b,eps=10**-10):
    #Recherche d'un zero d'une fonction par fausse position
    while b-a > eps:
        m=a-((a-b)/(f(a)-f(b)))*f(a)
        if(f(a)*f(m))>0:
            a=m
        else:
            b=m
    return m

def f(x):
    return math.log(x)-x**3+4
    
a=1
b=2
t=falsePos(f,a,b)
print(t[0])

            
    