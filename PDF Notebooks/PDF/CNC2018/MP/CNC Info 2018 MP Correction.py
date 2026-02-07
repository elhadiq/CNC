from numpy import *
from matplotlib.pyplot import *
#------------------------------------
#Première partie
#------------------------------------
#  Q1--------------------------------------
def ABM2(f,a,b,y0,h):
    n=int((b-a)/h)
    T=array([a+i*h for i in range(n+1)])
    Y=[0]*(n+1)
    Y[0]=y0
    Y[1]=Y[0]+h*f(T[0],Y[0])
    for i in range(1,n):
        k=Y[i]+h/2*(3*f(T[i],Y[i])-f(T[i-1],Y[i-1]))
        Y[i+1]=Y[i]+h/2*(f(T[i],Y[i])+f(T[i+1],k))
    return T,Y
# Q2---------------------------------------
def G(t,z):
    return array([z[1],-2/3*z[1]-25/3*z[0]])
# Q3-----------------------------------------    
T,Y=ABM2(G,0,8,array([-0.3,0]),0.001)
Y=array(Y)
plot(T,1/2*Y[:,0],label="y(t)")
legend()
grid()
show()
# Q4--------------------------------------
def racines(P):
    n=len(P)
    T=[i*0.001 for i in range(n)]
    R=[] #liste des y(t)=0 ou y(t)#0
    if P[0]==0:
        R.append(t[0])
    for i in range(1,n):
        if P[i]==0:
            R.append(T[i])
        elif P[i-1]*P[i]<0:
            R.append((T[i-1]+T[i])/2)
    return R
#pour tester la fonction racines---------
T,Y=ABM2(G,0,8,array([-0.3,0]),0.001)
Y=array(Y)
y=Y[:,0]
print(racines(y))
#------------------------------------------
#Deuxième partie
#-------------------------------------------
#Bioinformatique
#---------------
# Q1---------------------------------
#  le nombre minimum de bits pour coder 4 états est 2 
# Q2---------------------------------
#'A':00;'C':01;'G':10;'T':11
# Q3-----------------------------
def prefix(M,S):
    m=len(M)
    return M==S[:m]
    
print(prefix(M,S))    
# Q4--------------
# Dans le pire des cas M=S 
#donc La fonction réalise m comparaisons
# donc la complexité est O(m) avec m=len(M)
# Q5----------------
def liste_suffixes(S):
    L=[]
    for i in range(len(S)):
        L.append((S[i:],i))
    return L
# Q6-------------------
def tri_liste(L):#tri par sélection 
    n=len(L)
    for i in range(n-1):
        for j in range(i+1,n):
            if L[i][0]<L[j][0]:
                L[i],L[j]=L[j],L[i]
    return L
# Q7---------------------------------
def recherche_dichotomique(M,L):
    d,f=0,len(L)-1
    while d<=f:
        m=(d+f)//2
        if prefixe(M,L[m][0]):
            return L[m][1]
        elif M<L[m][0]:
            f=m-1
        else:
            d=m+1
    return None
# Q8---------------------
#si  m,k=len(M),len(L)
#  O(m*log(k))
#exemple : M='AAAAAT'  L='AAAAAAAAAAA'

# Q9--------------------------
def feuilles(R):
    if (R[1]==[]): 
        return(R[0])
    L=[]
    for f in R[1]:
        L=L+feuilles(f)
    return L
# Q10------------------
def recherche_arbre(M,R):
    for f in R[1]:
        if f[1]!=[]:
            if prefixe(M,f[0]):
                return feuilles(f)
            elif prefixe(f[0],M):
                n=len(f[0])
                return recherche_arbre(M[n:],f)
    return []
#Q11----------------------
#clé primaire de la table pendule : code
#unicité du code
#clé primaire de la table Mesures: fils ou (pere,fils)
#unicité de fils ou(pere,fils)

# Q12---------------------
#select distinct nom,niveau from Noeuds where nom like 'GCTA%' or nom like '%GCTA'
 
# Q13---------------------
#select count(distinct niveau)+1 from Noeuds  
#ou
# select max(niveau)+2 from Noeuds

# Q14---------------------
#select nom,niveau,count(*) from Noeuds,Liens where code=pere Group by code Having count(*)>2

# Q15---------------------
#select Max(C) from (select count(*) as C from Liens Group by pere)

# Q16---------------------
#select fils from Liens,Noeuds where code=pere and Niveau=(select max(Niveau) from Noeuds)

# Q17---------------------
#proj selon fils( sigma selon (code=pere and niveau>1)(liens x noeuds)))-(proj selon (code)(noeuds))'

# Q18-----------------
def matrice(P,Q):
    a,b=len(P),len(Q)
    M=[[0]*b for i in range(a)]
    for i in range(a):
        for j in range(b):
            if P[i]==Q[j]:
                M[i][j]=M[i-1][j-1]+1
    return M
# Q19-------------------
def plus_long_mc(P,M):
    n,a,b=len(P),len(Q),len(M[0])
    if a!=b and n==b:
        M=[[M[i][j] for i in range(a)]for j in rang(b)]
    L=[max(M[i]) for i in range(len(M))]
    print(L)
    v=max(L)
    C=[]
    if v==0 :
        return C
    for i in range(len(L)):
        if v==L[i]:
            ch=P[i-v+1:i+1]
            if ch not in C:
                C.append(ch)
    return C
# Q20---------------------
f=open("D:/génomes.txt","r")
S=f.read()
f.close()
L=S.split('\n')
P,Q=L[0],L[1]
M=matrice(P,Q)
R=[]
for i in range(len(P)):
    for j in range (len(Q)):
         v=M[i][j]
         ch=P[i-v+1:i+1]
         if ch!="" and ch not in R:
             R.append(ch)
for i in range(2,len(L)):
     Ls=tri_liste(liste_suffixes(L[i]))
     j=0
     while j<len(R):
         if recherche_dichotomique(R[j],Ls)==None:
             del(R[j])
         else:
             j+=1
     if (R==[]):
         break
Z=[]
if len(R)!=0:
    print(R)
    v=max([len(e) for e in R])
    Z=[e for e in R if len(e)==v]
print(Z)
 
#fin

    
    