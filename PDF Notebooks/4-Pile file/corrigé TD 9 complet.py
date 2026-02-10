#gestion de pile avec pile et sommet supposé déclaré en global
def creerPile():
    global sommet
    sommet=-1
def afficherPile():
    if estVidePile()==1:
        print("pile vide")
    else:
        print("le contenu de la pile: ")
        for i in range(sommet,-1,-1):
            print(pile[i],end='|')
        print()
def estVidePile():
    if sommet==-1:
        return(1)
    else:
        return(0)

def estPleinePile():
    if sommet==N-1:
        return(1)
    else:
        return(0)
def sommetPile():
    if estVidePile()==1:
        print("pile vide")
        return
    else:
        return(pile[sommet])
def empilerPile(e):
    global sommet
    if estPleinePile()==1:
        print("pile pleine")
    else:
        sommet+=1
        pile[sommet]=e
def depilerPile():
    global sommet
    if estVidePile()==1:
        print("pile vide")
    else:
        sommet-=1
        return(pile[sommet+1])
#gestion de file avec file, queue et sommet déclarés en globals
#approche par decalage
    
def creerFile():
    global tete,queue
    tete=0
    queue=-1
def fileVide():
    if queue==-1:
        return 1
    else:
        return 0
def filePleine():
    if queue==N-1:
        return 1
    else:
        return 0
def enfiler(x):
    global queue
    if filePleine()==1:
        print("pile pleine")
        return
    else:
        queue+=1
        file[queue]=x
def defiler():
    global queue
    if fileVide()==1:
        print("file vide")
        return
    else:
        aux=file[0]
        for i in range(queue):
            file[i]=file[i+1]
        queue-=1
        return aux
def afficherFile():
    if fileVide()==1:
        print("file vide")
        return
    else:
        print("\n\n contenu de la file")
        for i in range(queue+1):
            print(file[i],end='|')
        print()
def premierFile():
    if fileVide()==1:
        print("file vide")
        return
    else:
        return(file[tete])
#gestion de file avec file, queue et sommet déclarés en globals
#approche par tableau circulaire
def creerFileC():
    global tete,queue
    tete=N-1
    queue=N-1
def fileVideC():
    if tete==queue:
        return 1
    else:
        return 0
def filePleineC():
    if tete==(queue+1)%N:
        return 1
    else:
        return 0
def enfilerC(e):
    global queue
    if filePleineC()==1:
        print("file pleine")
        return
    else:
        queue=(queue+1)%N
        pile[queue]=e
def defilerC():
    global tete
    if fileVideC()==1:
        print("file vide")
        return
    else:
        tete=(tete+1)%N
        return(file[tete])
def afficherFileC():
    if fileVideC()==1:
        print("file vide")
        return
    else:
        i=tete+1
        while i>queue:
            print (file[i])
            i=(i+1)%N
        while i<=queue:
            print (file[i])
            i+=1
def premierFile():
    if fileVideC()==1:
        print("file vide")
        return
    else:
        return file[tete+1]
        
# gestion d'une pile passée en parametre
def creerPile1():
    return(-1)

def afficherPile1(pile1,sommet1):
    if estVidePile1(sommet1)==1:
        print("pile vide")
    else:
        print("le contenu de la pile: ")
        for i in range(sommet1,-1,-1):
            print(pile1[i],end='|')
        print()
def estVidePile1(sommet1):
    if sommet1==-1:
        return(1)
    else:
        return(0)

def estPleinePile1(sommet1):
    if sommet1==N-1:
        return(1)
    else:
        return(0)
def sommetPile1(pile1,sommet1):
    if estVidePile1(sommet1)==1:
        print("pile vide")
        return
    else:
        return(pile1[sommet1])
def empilerPile1(pile1,sommet1,e):
    if estPleinePile1(sommet1)==1:
        print("pile pleine")
    else:
        sommet1+=1
        pile1[sommet1]=e
        return sommet1
def depilerPile1(pile1,sommet1):
    if estVidePile1(sommet1)==1:
        print("pile vide")
    else:
        sommet1-=1
        return(pile1[sommet1+1],sommet1)

# probleme------------------------------------------------------------------------
def inverserPile(pile,sommet):
    #test si la pile est vide
    if estVidePile1(sommet)==1:
        print("pile vide")
        return
    else:
        for i in range((sommet//2)+1):
            aux=pile[i]
            pile[i]=pile[sommet-i]
            pile[sommet-i]=aux
#verification d'une expression mathématique si elle est bien parenthésée
def estOuvrant(c):
    if c=='(' or c=='[':
        return True
    else:
        return False
def estFermant(c):
    if c==')' or c==']':
        return True
    else:
        return False
def fermant(c):
    if c=='(':
        return ')'
    elif c=='[':
        return ']'
    else:
        return
def ouvrant(c):
    if c==')':
        return '('
    elif c==']':
        return '['
    else:
        return
def verification(expres):
    sommet=creerPile1()
    pile=[' ']*MAX
    i=0
    erreur=False
    while expres[i]!='#':
        if estOuvrant(expres[i]):
            sommet=empilerPile1(pile,sommet,fermant(expres[i]))
        elif estFermant(expres[i]):
            if estVidePile1(sommet)==0 and sommetPile1(pile,sommet)==expres[i]:
                sommet=depilerPile1(pile,sommet)[1]
            else:
                print("erreur expression: caractère ouvrant manquant",ouvrant(expres[i]))
                erreur=True
        i+=1
    if estVidePile1(sommet)==1 and not erreur:
        print("expression correcte")
    elif estVidePile1(sommet)==0:
        print("erreur expression: caractères fermants manquants")
        afficherPile1(pile,sommet)
# deuxième question
def operationelem(c):
    if c=='+' or c=='-' or c=='*' or c=='/':
        return True
    else:
        return False
def calcul(a,c,b):
    if c=='+':
        return a+b
    elif c=='-':
        return a-b
    elif c=='*':
        return a*b
    elif c=='/':
        if b==0:
            print("erreur: division par zéro")
            return
        else:
            return a//b
def evaluation(expres):
    sommet=creerPile1()
    pile=['']*MAX
    i=0
    while T[i]!='#':
        if operationelem(T[i])==True:
            b,sommet=depilerPile1(pile,sommet)
            a,sommet=depilerPile1(pile,sommet)
            sommet=empilerPile1(pile,sommet,str(calcul(int(a),T[i],int(b))))
        else:
            sommet=empilerPile1(pile,sommet,T[i])
        i+=1
    print("le résultat du calcul est ", sommetPile1(pile,sommet))
                            
        

#-------------------------------------programme principal
N=100
#gestion de pile

pile=[0]*100
sommet=0

print("gestion d'une Pile: ")
print("appuyer sur 'p' pour une gestion paramétrée et sur 'g' pour une gestion en global")
rep1=input()

if rep1=='g' or rep1=='G':
    
    creerPile()
    rep=input("voulez vous empiler?o/n")
    while rep=='o'or rep=='O':
        e=int(input("saisir l'element à empiler"))
        empilerPile(e)
        rep=input("voulez vous empiler?o/n")

    afficherPile()
    rep=input("voulez vous depiler?o/n")
    while rep=='o' or rep=='O':
        print("element dépilé:", depilerPile())
        rep=input("voulez vous depiler?o/n")

    afficherPile()
    
    
elif rep1=='p' or rep1=='P':
    sommet=creerPile1()
    rep=input("voulez vous empiler?o/n")
    while rep=='o' or rep=='O':
        e=int(input("saisir l'element à empiler"))
        sommet=empilerPile1(pile,sommet,e)
        rep=input("voulez vous empiler?o/n")

    afficherPile1(pile,sommet)
    rep=input("voulez vous depiler?o/n")
    while rep=='o' or rep=='O':
        
        aux,sommet=depilerPile1(pile,sommet)
        print("element dépilé:",aux)
        
        rep=input("voulez vous depiler?o/n")

    afficherPile1(pile,sommet)
    
# gestion d'une file: approche par decalage
file=[0]*100
tete=0
queue=10
print("gestion d'une file par decalage: ")
creerFile()
rep=input("voulez vous enfiler?o/n")
while rep=='o':
    e=int(input("saisir l'element à enfiler"))
    enfiler(e)
    rep=input("voulez vous enfiler?o/n")

afficherFile()
rep=input("voulez vous defiler?o/n")
while rep=='o':
    print("element défilé:", defiler())
    rep=input("voulez vous defiler?o/n")

afficherFile()

#gestion d'une file approche par tableau circulaire
file=[0]*100
tete=0
queue=10
print("gestion d'une file par tableau circulaire: ")
creerFile()
rep=input("voulez vous enfiler?o/n")
while rep=='o':
    e=int(input("saisir l'element à enfiler"))
    enfiler(e)
    rep=input("voulez vous enfiler?o/n")

afficherFile()
rep=input("voulez vous defiler?o/n")
while rep=='o':
    print("element défilé:", defiler())
    rep=input("voulez vous defiler?o/n")

afficherFile()
#probleme:
MAX=100
T=['']*MAX
#saisie de l'expression mathématique
#1: vérification d'une expression mathématique si elle est bien parenthésée
i=0
c=''
while c!='#':
    print('saisir le caractère ',i+1,"de l'expression")
    c=input()
    T[i]=c
    i+=1
verification(T)
#evaluation d'une expression mathematique postfixée
i=0
c=''
while c!='#':
    print('saisir le caractère ',i+1,"de l'expression")
    c=input()
    T[i]=c
    i+=1
evaluation(T)
