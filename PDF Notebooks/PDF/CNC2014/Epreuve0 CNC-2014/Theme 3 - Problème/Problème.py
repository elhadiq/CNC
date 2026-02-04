#variable globale
N=8

'''
Question 13 :
Dans le cas de nombres non signés (par exemple : 123, 67, …) donner la taille maximale et la
taille minimale possible pour de tels nombres.

Question 14
Pour réaliser l’addition de deux big-numbers, déterminer la valeur N optimale. Justifier votre
réponse.
'''

#Question 15
def subString (s,debut):
    assert debut+N<=len(s) 
    return s[debut:debut+N]

#Question 16
def transforme (s):
    if len(s)<N:
        return transforme ('0'+s)
    else:
        return s
        
#Question 17
def nbSousChaines(s):
    n=len(s)//N
    if len(s)%N!=0: n+=1
    return n
    
        
#Question 18
def retenue(n):
    s=str(n)
    if len(s)>N:
        return int(s[0])
    else:
        return 0
        
#Question 19
def filtre(n):
    s=str(n)
    if len(s)>N:
        return int(s[1:])
    else:
        return n

#Question 20
'''
 utiliser une fonction intermidiare qui retourne une liste
 des blocs du nombre
'''

def decomposer(s):
    L=[]
    n=nbSousChaines(s)
    for i in range(1,n):
        l=subString(s,len(s)-i*N)
        L=[int(l)]+L
        
    r=(len(s)-N*(n-1))  #caractères restant
    if r!=0: L=[int(s[:r])]+L
    return L

def decomposer2(s):
    L=[]
    i=len(s)-1
    while(i>=0):
        ch=''
        j=0
        while  j<N and i>=0:
            ch=s[i]+ch
            i-=1
            j+=1
        L=[int(ch)]+L
    return L


'''
#pas besoin 
def add_bolcs(b1,b2):
    s=0
    r=0
    s=''
    for i in range(-1,-len(b1)-1,-1):
        v=int(b1[i])+int(b2[i])+r
        if v>9:
            v=v-10
            r=1
        else: 
            r=0
        s=str(v)+s
    if r!=0: s=str(r)+s
    return s
'''

def add_big_number(s1,s2):
    '''
      on suppose ici que s1 et s2 sont composées d'un même nombre de blocs
    '''
    L1=decomposer(s1) #Décomposer s1 en une liste L1 de groupes de N chiffres
    L2=decomposer(s2) #Décomposer s2 en une liste L2 de groupes de N chiffres
    s=''
    r=0
    for i in range(-1,-len(L1)-1,-1):  #parcourir la liste L1  à partir du dernier bloc
        a=L1[i]+L2[i]
        if r==1:
            if retenue(a)==1: 
                a=filtre(a)+1
            else:
                a=a+1
            
        
        r=retenue(a)
        if r==1: a=filtre(a)
        s=str(a)+s
    
    if r==1: s='1'+s  #Ajouter la retenue à gauche s'il existe
    return s
        
        
#Question 21

def add_gene_big_number(s1,s2):
    n1=len(s1)
    n2=len(s2)
    if n1<n2: 
        s1,s2=s2,s1
    
    s2='0'*(n1-n2)+s2
    a=add_big_number(s1,s2)
    
    return a
    
    
        
    
    
    