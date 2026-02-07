#Question 1
'''
1.	Écrire une requête SQL permettant de sélectionner les enregistrements qui correspondent au site L uniquement.


SELECT * 
FROM POTERIES
WHERE Site LIKE 'L' ;
'''


#Question 2
'''
2.	Écrire une requête SQL permettant de déterminer la moyenne des valeurs du champ Al pour le site L.

SELECT AVG(AL) as 'Moyenne AL'
FROM POTERIES
WHERE Site LIKE 'L'
'''
#Question 3
import sqlite3 as s3
def moyenne_metaux(s):
    con=s3.connect('c:/poteries.sqlite')
    cur=con.cursor()
    req='select avg(Al),avg(Fe),avg(Mg),avg(Ca),avg(Na) from poteries where site LIKE ?'
    cur.execute(req,[s])
    L= cur.fetchall()  #ici L est une liste contenant un tuple à 5 valeurs
    con.close()
    return list(L[0])
    
#Question 4
def Question4():
    L=moyenne_metaux('L')
    moy=L[0]
    con=s3.connect('c:/poteries.sqlite')
    cur=con.cursor()
    req='select* from poteries where ? between AL-0.1*?  and AL+0.1*?'
    cur.execute(req,[moy,moy,moy])
    for l in  cur.fetchall():
        print(l)
    con.close()
    
def Question4_2():
    L=moyenne_metaux('L')
    moy=L[0]
    con=s3.connect('c:/poteries.sqlite')
    cur=con.cursor()
    req='select* from poteries where Al between ? and ?'
    cur.execute(req,[moy*0.9,moy*1.1])
    for l in  cur.fetchall():
        print(l)
    con.close()
    
#Question 5
import numpy as np
def matrice_site(s):
    con=s3.connect('c:/poteries.sqlite')
    cur=con.cursor()
    req='select Al,Fe from poteries where site=?'
    cur.execute(req,[s])
    L= cur.fetchall()  #ici L est une liste de tuples chacun avec 2 valeurs
    con.close()
    return np.matrix(L)
    
    
#Question 6
import matplotlib.pyplot as plt
def trace_site(s):
    M=matrice_site(s)
    plt.plot(M[:,0],M[:,1])
    
    plt.xlabel('AL') #Etiquette sur l'axe x
    plt.ylabel('Fe') #Etiquette sur l'axe y
    plt.grid()
    plt.show()
        
    
