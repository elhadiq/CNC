#  Implémentation du type abstrait Pile avec des listes Python
def   creer_pile( ): 
    return [ ]

def    depiler(p):
    assert len(p) > 0
    return p.pop( )

def   empiler(p, v):
    p.append(v)

def    sommet(p):
    assert len(p) > 0
    return p[-1]

def   taille(p):
    return len(p)

def    est_vide(p):
    return taille(p) == 0




def   EstNombre(x) :
    y=x.lstrip("-")
    y=y.lstrip("+")
    y=y.split(".")
    if  len(y) > 2 :
        return False
    else:
        for k in y:
            if not k.isdigit():
                return False
    return True


def   operation(o,a,b):
    if     o=="+": 	return  a+b
    elif   o=="-":	return  a-b 
    elif   o=="*":	return  a*b 
    else:
        if   b!=0:
            return   a/b
        else:
            return  "Erreur, division par zero"

def   postfix(expr):
    expr=expr.split()
    p=creer_pile()
    for  k   in  expr:
            if   EstNombre(k)==True:
                empiler(p,float(k))
            else:
                b=depiler(p)
                a=depiler(p)
                r=operation(k,a,b)
                print(r)
                empiler(p,r)
            print(p)
    v=depiler(p)
    assert   est_vide(p), 'la pile n est pas vide expression non valide '
    return  v


#  Vérification des parenthèses
def   verifparenthese (texte):
    # On commence avec une pile vide 
    p = creer_pile( )
    # Parcours du texte caractère par caractère 
    for   i    in   range(0 , len(texte)): 
        if   (texte[i]=='(' ): 
            # Si le caractère est une parenthèse ouvrante, on empile son indice i 
            empiler(p, i) 
        elif (texte[i]==')' ): 
            # Sinon, c’est qu’il s’agit d’une parenthèse fermante 
            if (est_vide(p)): 
            # Si la pile est vide le mot n’est pas bien parenthèsé
                return  False 
            # Sinon, on dépile l’indice j de la dernière parenthèse ouvrante 
            j = depiler(p) 
            # On affiche le couple (j,i) : la parenthèse ouvrante de l’indice j
            # correspond à la parenthèse fermante à l’indice i 
            print( j , i )
        
    # Il ne reste plus qu’ à vérifier si la pile est vide 
    return  est_vide(p)
