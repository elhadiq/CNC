#Question 9
'''
 Dans la notation postfixée les parenthèses deviennent inutiles
'''
#Question 10
def initPile():
    return []

#Question 11    
def estVide(pile):
    return pile==[]
    
#Question 12
def empiler(pile,elem):
    pile.append(elem)

#Question 13
def depiler(pile):
    if pile==[] : return None #raise PileideException('pile vide')
    x=pile[-1]
    pile.reverse()
    pile.remove(x)
    pile.reverse()
    return x
    
def depiler2(pile):
    if pile==[] : return None
    x=pile[-1]
    pile[-1:]=[]
    return x
    
#Question 14:
def valeurSommet(pile):
    if pile==[] : 
        return None
    else:
        return pile[-1]
        
#Question 15:
def hauteur(pile):
    i=0
    for e in pile: i+=1
    return i

#Question 16:
def estEtier(e, first=True):
    e=str(e)
    if e=='':
        if first:
            return False
        else:
            return True
   
    elif e[0]<'0' or e[0]>'9':
        return False
    else:
        return estEtier(e[1:],False)

#Question 17:    
class OpNonValideException(Exception):
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return self.message
        
class ArgNonValideException(Exception):
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return self.message
        
def eval(o,a,b):
    if o not in '+-*/.':
        raise OpNonValideException('Opérateur non valide')
    elif not (type(a) is int and type(b) is int ):
        raise ArgNonValideException('argument non valide')
    else:
        if   o=="+": 	return  a+b
        elif o=="-":	return  a-b 
        elif o=="*":	return  a*b 
        else:
            if   b!=0:
                return   a/b
            else:
                raise   ZeroDivisionError("Erreur, division par zero")


#Question 18:
def evalue(expr):
    p=initPile()
    i=0
    while i<hauteur(expr) and expr[i]!='.':
        e=expr[i]
        if  estEtier(e)==True:
            empiler(p,int(e))
        else:
            b=depiler(p)
            a=depiler(p)
            r=eval(e,a,b)
            empiler(p,r)
        i+=1
    v=depiler(p)
    if not estVide(p): print('la pile n est pas vide expression non valide ')
    return  v
    
#Question 19
def   estBienParenthesee (expr):
    oui='Expression bien parenthésée'
    non='Expression mal  parenthésée'
    
    # On commence avec une pile vide 
    p = initPile( )
    # Parcours l'expression élément pa élément 
    
    for   i    in   range(hauteur(expr)): 
        if   expr[i]=='(': 
            # Si le caractère est une parenthèse ouvrante, on l'empile 
            empiler(p,   expr[i]) 
        elif (  expr[i]==')' ):
                # Sinon, c’est qu’il s’agit d’une parenthèse fermante 
                if (estVide(p) or   expr[i-1]==')'): 
                    # Si la pile est vide l'espresion n’est pas bien parenthèsé
                    return non
                else:
                    # Sinon, on dépile la dernière parenthèse ouvrante 
                    depiler(p) 

    # Il ne reste plus qu’ à vérifier si la pile est vide 
    if  estVide(p):
        return oui
    else:
        return non


#Question 20
class ExpressionMalException(Exception):
    def __init__(self,mess):
        self.mess = mess
    def __str__(self):
        return self.mess
        

def transInfix(expr):
    if expr=='':
        raise ExpressionMalException("expression vide")
    else:
        p1=initPile()  #pile de opérateurs
        p2=initPile()  #pile intermédiare
        p3=initPile()  #pile qui sera retournée
        er=False
        i=0
        while expr[i]!='.' and not er:
            if expr[i] in '+-*/':
                empiler(p1,expr[i])
            elif estEntier(expr[i]):
                empiler(p2,expr[i])
            else: er=True
            i+=1
        if er:
            raise ExpressionMalException("expression mal formée")
        else:
            empiler(p3,depiler(p2))
            while not estVide(p1) and not estVide(p2):
               empiler(p3,depiler(p2))
               empiler(p3,depiler(p1))
            empiler(p3,'.')
            return(p3)
    
#Question 21
def priorite(c):
    if c in('+-'):  return  1
    if c in ('*/'): return 2
    if c in ('^'):  return 3
    if c=='(':      return 0
    
def transInfix1SeulNiveau(expr):
    p1=initPile() #pile des opérateurs
    p2=initPile() #pile qui sera retournée
    i=0
    while expr[i]!='.':
        c=expr[i]
        if estEtier(c):
            empiler(p2,c)
        elif c=='(':
            empiler(p1,c)
        elif c==')':
            while valeurSommet(p1)!='(' :
                empiler(p2,depiler(p1))
            depiler(p1)
        else:  #c'est un operateur
            while (not estVide(p1) and (priorite(valeurSommet(p1))>=priorite(c))):
                empiler(p2,depiler(p1))
            empiler(p1,c)
        
        i+=1
        
    # vider la pile des operateurs
    while not estVide(p1):
        empiler(p2,depiler(p1))
    empiler(p2,'.')    
    return (p2)

#print(transInfix1SeulNiveau(['(','1','+','2',')','*','4','.']))
    
#Question 22
def transtotal(expr):
    p1=initPile()  #pile de opérateurs
    p2=initPile()  #pile des nombres
    p3=initPile()  #pile qui sera retournée
    i=0
    while expr[i]!='.':
        if estEntier(expr[i]):
            empiler(p2,expr[i])
        else:
            empiler(p1,expr[i])
        i+=1
    while not estVide(p2):
        empiler(p3,depiler(p2))
    p1.reverse()
    while not estVide(p1):
        empiler(p3,depiler(p1))
    empiler(p3,'.')
    return(p3)
#print(transtotal(['8', '4', '+', '3', '*', '1', '-', '.']))

#Question 23
def transtotal1(expr):
    expr=transInfix(expr)
    p1=initPile()    #pile des opérateurs
    p2=initPile()    #pile de nombes
    p3=initPile()    #pile à retourner
    i=0
    while expr[i]!='.':
        if estEntier(expr[i]):
            empiler(p2,expr[i])
        else:
            empiler(p1,expr[i])
        i+=1
    while not estVide(p2):
        empiler(p3,depiler(p2))
    
    p1.reverse()
    while not estVide(p1):
        empiler(p3,depiler(p1))
    empiler(p3,'.')
    return(p3)
#print(transtotal(['1','+','3','*','4','+','8','.']))