#A- Gestion des commentaires et des espaces
#Question A-1 : test d’un commentaire
def comment(inst):
    return inst[:2]=='/*' and inst[-2:]=='*/'

#Question A-2 : Suppression d’espaces multiples dans une instruction
def suppEspaces(inst):
    
    #pour ne pas copier les espaces  en début
    i=0
    while i<len(inst) and inst[i]==' ': i+=1  
    
    #pour ne pas copier les espaces  consécutifs
    s=''
    while i<len(inst):
        while i<len(inst)-1 and inst[i]==' ' and inst[i+1]==' ': 
            i=i+1  
        s=s+inst[i]
        i+=1 
        
    #pour éliminer l'espace droit
    if s[-1]==' ' : s=s[:-1]    
    return (s)
                
                
#B- Reconnaissance des mots-clés et des identificateurs
MotsCles = ['si','sinon','tantque','pour','definir']

#Question B-1 : Vérification d’un mot clé
def motcle(MotsCles,mot):
    if MotsCles==[]:
        return False
    elif MotsCles[0]==mot:
        return True
    else:
        return motcle(MotsCles[1:],mot)
        
#Question B-2 : Validité d’un identificateur
def identificateur(id):
    if len(id)>=80: return False
    if ' ' in id :  return False
    if id[0] in '0123456789' :return False
    if motcle(MotsCles,id): return False
    return True
    
#C : Implémentation de l’analyseur lexical.
#Question C-1 : Analyse d’une instruction

def analyserInstruction(inst) :
    
    if comment(inst) : return True
    
    inst=suppEspaces(inst)
    mot=''
    i=0
    while i<len(inst) and inst[i]!=' ':
        mot+=inst[i]
        i+=1
    
    if identificateur(mot) and i<len(inst):
        return True
    
    return  motcle(MotsCles,mot) and i<len(inst) and inst[-1]==';'
        
#Question C-2 : Analyse d’un fichier source. 
def analyserSource(sourcePL):
    F=open(sourcePL,'r')
    i=0
    L=[]
    while inst in F:
        if analyserInstruction(inst)==False:
            L.append(i+1)
    F.close()
    
    if L==[] : 
        print('Succés')
    else:
        print('les numéros de lignes correspondants à des instructions incorrectes sont :',end='')
        for i in range(len(L)-1):
            print("%d," % L[i],end='')
        print(L[-1])
    
        

    
    

        
