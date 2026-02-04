#I.	Chiffrement de César
#########################
#Question 1
def decaler(car,nb):
    if 'a'<=car<='z': return chr((ord(car)- ord('a')+ nb)%26 + ord('a'))
    elif 'A'<=car<='Z': return chr((ord(car)- ord('A')+ nb)%26 + ord('A'))
    else: return car


#Question 2
def coder(chaine,nb):
    """Code de Cesar avec décalage de nb"""
    phrase=''
    for car in chaine:
        phrase+=decaler(car,nb)
    return phrase


#Question 3
def frequence(chaine):
    """Tableau des apparition des lettres"""
    L=[0]*26
    for car in chaine:
        if 'a'<=car<='z': L[ord(car)-ord('a')]+=1
        elif 'A'<=car<='Z': L[ord(car)-ord('A')]+=1
            
    return L
    
#Question 4
def indiceMax(L):
    ind=0
    for i in range(len(L)):
        if L[i]>L[ind]:ind=i
    return ind
    
#Question 5
def lettreMax(chaine):
    return chr(ord('a')+indiceMax(frequence(chaine)))
    
    
#Question 6
def cle(chainecrypte):
    return (ord(lettreMax(chainecrypte))-ord('e'))%26


#Question 7
def decoder(chaine):
    nb=cle(chaine)
    return coder(chaine,-nb)
    
#Question 8
def coderFichier(nomFichier1, nomFichier2, nb):
    f1=open(nomFichier1,'r')
    f2=open(nomFichier2,'w')
    f2.write(coder(f1.read(),nb))
    f1.close()
    f2.close()


#Question 9
def decoderFichier(nomFichier1, nomFichier2):
    f1=open(nomFichier1,'r')
    f2=open(nomFichier2,'w')
    f2.write(decoder(f1.read()))
    f1.close()
    f2.close()


#II.Chiffrement de Vigenère
###########################

#Question 10
def chiffrementVigenere( texte , cle ):
    """Code de Vigenere"""
    i=0
    phrase=''
    for car in texte:
        phrase+=decaler(car,ord(cle[i])-ord('a')+1)        
        i=i+1
        i=i%len(cle)
    return phrase