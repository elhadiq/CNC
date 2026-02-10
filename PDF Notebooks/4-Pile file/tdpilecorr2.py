### implémentation du type abstrait Pile
### avec des listes Python

def pilevide ():
    return []

# choix : sommet de pile en tête de liste
def ajoute (e,p) :
    p.insert(0,e)

def sommet(p) :
    return p[0]

def depile (p) :
    del(p[0])

def estvide(p):
    return len(p)==0

def copiepile(p) :
    return list(p)

def affichepile(p):
    print()
    print('|   |')
    i = 0
    while i<len(p):
        print('|---|')
        print('|',p[i],'|')
        i = i+1
    print(' ---')

### fonctions avancées sur les piles

# inversion d'une pile

def inversepile(p):
    q = copiepile(p)
    r = pilevide()
    while (not(estvide(q))):
        ajoute(sommet(q),r)
        depile(q)
    return r

# vérification parenthésage

def estouvrante (c) :
    return (c=='(') or (c=='{') or (c=='[')

def fermante (c) :
    if (c=='('):
        return ')'
    elif (c=='{'):
        return '}'
    elif (c=='['):
        return ']'
    else:
        return '?'

def verifparenthese (texte):
    print()
    print("-> vérification de «",texte,"»")
    # on commence avec une pile vide
    p = pilevide()
    # parcours du texte caractère par caractère
    for i in range(0,len(texte)):
        if estouvrante(texte[i]):
            # si le caractère est une ouvrante...
            # ... on empile la fermante associée
            ajoute(fermante(texte[i]),p)
        else:
            # sinon la fermante rencontrée doit
            # être la même que celle sur la pile
            if (estvide(p) or (texte[i] != sommet(p))):
                print("erreur caractère",i)
            else:
                depile(p)
    # à la fin du texte, la pile doit être vide
    if (estvide(p)):
        print("fin de vérification")
    else:
        # sinon il y a un problème
        print("pile non vide !")
        affichepile(p)
    print()

# évaluation d'une expression arithmétique

def estoperation(c):
    return (c=='+') or (c=='-') or (c=='*') or (c=='/')

def ptitcalcul (o,a,b):
    if (o=='+'):
        return a+b
    elif (o=='-'):
        return a-b
    elif (o=='*'):
        return a*b
    elif (o=='/'):
        return a/b

def evaluepostfix (expression):
    print()
    print("-> évaluation de «",expression,"»")
    # on commence avec une pile vide
    p = pilevide()
    # parcours de l'expression caractère par caractère
    for i in range(0,len(expression)):
        if estoperation(expression[i]):
            # si c'est un opérateur
            # on dépile un premier entier
            n = sommet(p)
            depile(p)
            # et puis un autre
            m = sommet(p)
            depile(p)
            # on effectue le calcul
            r = ptitcalcul(expression[i],n,m)
            # et on empile le résultat
            ajoute(r,p)
        else: # c'est un entier et on l'empile
            ajoute(int(expression[i]),p)
    # à la fin, le résultat est sur la pile
    print("résultat :",sommet(p))
    print()

### tests

mapile = pilevide()

ajoute(2,mapile)
ajoute(8,mapile)
ajoute(5,mapile)
ajoute(0,mapile)
ajoute(3,mapile)
ajoute(7,mapile)
ajoute(9,mapile)

affichepile(mapile)
affichepile(inversepile(mapile))

verifparenthese("coucou")
verifparenthese("([{{{}}}]{)(()})")
verifparenthese("([{{{}}}]{()()})")
verifparenthese("(([{{{}}}]{()()})")
verifparenthese("([{{{}}}]{()()}))")

evaluepostfix("12+4*3+")
