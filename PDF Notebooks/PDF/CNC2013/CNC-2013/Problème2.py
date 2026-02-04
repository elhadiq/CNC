 #variables globales
Max=100
N = 10
NC = 5
 
#pour les tests
 
tabC=L=[ [[2,6],[3,6],[4,6],[4,5],[4,4],[4,3],[-1,-1],[-1,-1] ],
    [ [2,6],[2,5],[3,5],[3,4],[3,3],[4,3],[-1,-1],[-1,-1] ],
    [ [2,6],[3,5],[4,4],[4,3],[-1,-1],[-1,-1]             ],
    [ [2,6],[3,3],[4,3],[-1,-1],[-1,-1]                   ],
    [ [2,6],[2,5],[2,4],[2,3],[3,3],[4,3],[-1,-1],[-1,-1] ]
  ]
  
A=[2,6]
B=[4,3]
R=[1,1]
  
#Question 1
def initChemin():
     return [[-1,-1] for i in range(Max)]
     
#Question 2

def cheminHV(A,B):
    HVAB=initChemin()
    HVAB[0]=A;
    i=0;
    if (A[0]<=B[0]):   #deplacement à droite
        while(HVAB[i][0]<B[0]):
            HVAB[i+1][0]=HVAB[i][0] +1; 
            HVAB[i+1][1]=A[1]; 
            i+=1;
    else :          #deplacement à gauche
        while(HVAB[i][0]>=B[0]):
            HVAB[i+1][0]=HVAB[i][0] -1; 
            HVAB[i+1][1]=A[1]; 
            i+=1;
    
    if (A[1]>=B[1]):  #deplacement vers le bas
        while(HVAB[i][1]>B[1]):
            HVAB[i+1][1]=HVAB[i][1] -1; 
            HVAB[i+1][0]=B[0]; 
            i+=1;
    else:          #deplacement vers le haut
        while(HVAB[i][1]<=B[1]):
            HVAB[i+1][1]=HVAB[i][1] +1; 
            HVAB[i+1][0]=B[0];  
            i+=1;
  
    return HVAB[:i+1]