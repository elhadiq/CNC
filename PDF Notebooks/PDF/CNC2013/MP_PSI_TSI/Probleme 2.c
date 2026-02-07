#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>

/* Déclaration des structures*/

typedef struct
{
 int x;    //abscisse du point
 int y;   //ordonnée du point
}point;

typedef struct typechemin
{
  point p;
  struct typechemin *suiv;
}cheminListe;


/*Prototypes des fonctions demandées*/
void initialiserC();
void cheminHV(point A, point B);
void cheminHV2(point A, point B);
int distancemin();
cheminListe* BversA();
void afficherChemin(cheminListe *dep);
cheminListe *cheminRepere(point A, point B, point R);

/*****************************************************************/
/****Fonctions non demandées (on les a définies pour le teste*****/
/*****************************************************************/
 void affichetabC();
 void afficheCheminHV(); 
 cheminListe* AversB();

/*****Constantes et variables globales****/
 #define Max 100
 #define N 10
 #define NC 5

 point A={2,6};
 point B={4,3};
 point R={1,1};

 point C[Max];
 point tabC[NC][Max]={ { {2,6},{3,6},{4,6},{4,5},{4,4},{4,3},{-1,-1},{-1,-1} },
                       { {2,6},{2,5},{3,5},{3,4},{3,3},{4,3},{-1,-1},{-1,-1} },
                       { {2,6},{3,5},{4,4},{4,3},{-1,-1},{-1,-1}             },
                       { {2,6},{3,3},{4,3},{-1,-1},{-1,-1}                   },
                       { {2,6},{2,5},{2,4},{2,3},{3,3},{4,3},{-1,-1},{-1,-1} }
                     }; 





/****** Programme principal (non demandé) ****/
main()
{
 /*Partie A : */
 /*A.1:*/
 printf("A.1 Initialisation du tableau C:\n");
 initialiserC(); 
 printf("Le tablea C est  initialise par les point (-1,-1):\n");

 /*A.2:*/
 printf("\nA.2 chemin horizontal puis vertical:\n");
 cheminHV2(A,B);
 printf("Chemin horizontal puis vertical de A(2,6) vers B(4,3):\n");
 afficheCheminHV();   //non demandé
 
 /*A.3:\n*/
  printf("\n\nA.3 Chemin Optimal:\n");
  printf("\nSoit l'ensemble des chemin entre les points A(2,6) et  B(4,3):\n");
  affichetabC();
/*A.3.b:\n*/
 printf("\nA.3.b:Distance minimale entre les 2 points A(2,6) et  B(4,3)\n");
 printf("Distance minimum=%d\n",distancemin());
 
 /*Partie B: */
 /*B.1: */
 printf("\n\nB.1 Chemin de retour:\n");
 cheminListe* retour;
 retour=BversA();
 printf("Chemin de B(4,3) vers A(2,6):\t");
 afficherChemin(retour);
 /*B.2: */
 printf("\n\nB.2 Affichage des points d'un chemin:\n");
 printf("Chemin de B(4,3) vers A(2,6):\t");
 afficherChemin(retour);
 
 /*B.3: */
 printf("\n\nB.3 Itineaire passant par un repere:\n");
 printf("Chemin de A(2,6) vers B(4,3) passant par un repere R(1,1):\n");
 cheminListe* cr=cheminRepere( A,  B,  R);
 afficherChemin(cr);
 
 
 getch();
}

/**************************/
/*Définition des fonctions*/
/**************************/

/********************************************/
/*A.1: Initialisation du tableau C***********/
/********************************************/
void initialiserC()
{
   int i;
   for(i=0;i<Max;i++)
   {C[i].x=-1;C[i].y=-1;}
}

/********************************************/
/*A.2: Chamin horizontal puis vertical*******/
/********************************************/
/**************Version 1*************************/
void cheminHV(point A, point B)
{
  int i;
  C[0]=A;
  i=0;
  
  if (A.x<=B.x)   /*deplacement à droite*/
  while(C[i].x<=B.x)
  { C[i+1].x=C[i].x +1; 
    C[i+1].y=A.y; 
    i++;
  }
  else           /*deplacement à gauche*/
  while(C[i].x>=B.x)
  { C[i+1].x=C[i].x -1; 
    C[i+1].y=A.y; 
    i++;
  }
    
  if (A.y>=B.y)  /*deplacement vers le bas*/
  while(C[i].y>=B.y)
  { C[i+1].y=C[i].y -1; 
    C[i+1].x=B.x; 
    i++;
  }
  else          /*deplacement vers le haut*/
  while(C[i].y<=B.y)
  { C[i+1].y=C[i].y +1; 
    C[i+1].x=B.x;  
    i++;
  }
}
/**************Version 2*************************/
void cheminHV2(point A, point B)
{
  int i,j,k;
  
  if (A.x<=B.x)
  /*deplacement à droite*/
  for(k=0,i=A.x;i<=B.x;i++,k++)
  { C[k].x=i; 
    C[k].y=A.y; 
  }
  
  else
  /*deplacement à gauche*/
  for(k=0,i=A.x;i>=B.x;i--,k++)
  { C[k].x=i; 
    C[k].y=A.y; 
  }
  
  
  if (A.y>=B.y)
  /*deplacement vers le bas*/
  for(j=A.y-1 ; j>=B.y;j--,k++)
  { C[k].x=B.x; 
    C[k].y=j;
  }
  else
  
  /*deplacement vers le haut*/
  for(j=A.y+1; j<=B.y;j++,k++)
  { C[k].x=B.x; 
    C[k].y=j; 
  }
}


/********************************************/

/********************************************/
/*A.3: Chemin optimal***********************/
/********************************************/

/********************************************/
/*A.3.a : distance d'un chemin **************/
/********************************************/
int distance(int num)
{
 int i,d;
 d=0;
 
 for(i=1; i<Max && tabC[num][i].x!=-1;i++)
 {
   if(tabC[num][i].x!=A.x && tabC[num][i].y!=A.y) d++;
 }
 return d;
}
/********************************************************/
/*A.3.b : distance minimale entre 2 points **************/
/********************************************************/
int distancemin()
{
  int i,min,d;
  min=distance(0);
  for(i=1;i<NC;i++)
  {
    d=distance(i);
    if(d<min) min =d;
  }
  return min;
}

/********************************************/
/*B1: Chemin de retour **********************/
/********************************************/
cheminListe *ajouterEnFin(cheminListe *l, point p)
{
  cheminListe *nouv, *q;
  nouv=(cheminListe *)malloc (sizeof(cheminListe));
  nouv->suiv=NULL;
  nouv->p=p;
  if(l==NULL) return nouv;
  q=l;
  while(q->suiv!=NULL)
    q=q->suiv;
    
  q->suiv=nouv;
  return l;  
}
/********************************************/
cheminListe *ajouterEnTete(cheminListe *l, point p)
{
  cheminListe *nouv, *q;
  nouv=(cheminListe *)malloc (sizeof(cheminListe));
  nouv->p=p;
  nouv->suiv=l;
  return nouv;  
}

/********************************************/
cheminListe* BversA()
{
  cheminListe *l, *inv;
  point p;
  l=AversB();
  inv=NULL;
  while (l != NULL)
    { 
        inv=ajouterEnTete(inv,l->p);
        l=l->suiv;
    }
  return inv;  
}

/******chemin de retour version 2******************************/
/******inverser le chemin AversB sans créer un autre chemin*****/
cheminListe * BversA2()
{
  cheminListe *l, *inv, *p;
  l=AversB();
  inv=NULL;
  while (l != NULL)
    { p = l;
      l = l -> suiv;
      p -> suiv = inv;
      inv = p;
    }
  return inv;  
}
/********************************************/
/*B2: Affichage des points d'un chemin*******/
/********************************************/
void afficherChemin(cheminListe *dep)
{
  if(dep!=NULL)
  {
   //Afficher le 1er element
    if(dep->suiv==NULL)      
      printf("P(%d,%d)",dep->p.x,dep->p.y); 
    else
      printf("P(%d,%d),",dep->p.x,dep->p.y); 
  
      //Afficher le reste
      afficherChemin(dep->suiv);
  }
      
}

/********************************************/
/*B2: Itinéraire passant par un point********/
/********************************************/
/***Fonction qui permet de créer un chemin entre 2 points A et B***/
cheminListe *crerChemin(point A, point B)
{ cheminListe *C;
  point p;
    
  C=NULL;
  p=A;
  C=ajouterEnFin(C,A);
  
  if (A.x<=B.x)
  //deplacement à droite/
  while(p.x<B.x)
  { p.x=p.x+1; 
    p.y=A.y; 
    C=ajouterEnFin(C,p);
  }
  else
   /*deplacement à gauche*/
  while(p.x>B.x)
  { p.x=p.x-1;  
    p.y=A.y; 
    C=ajouterEnFin(C,p);
  }
  
  
  if (A.y>=B.y)
  /*deplacement vers le bas*/
  while(p.y>B.y)
  { p.x=B.x; 
    p.y=p.y-1;
    C=ajouterEnFin(C,p);
  }
  else
  
  /*deplacement vers le haut*/
  while(p.y<B.y)
  { p.x=B.x; 
    p.y=p.y+1;; 
    C=ajouterEnFin(C,p);
  }
 return C;
}

/***Fonction qui permet de créer itineraire passant par un point***/
cheminListe *cheminRepere(point A, point B, point R)
{
  cheminListe *C1;  //Chemin de A vers R
  cheminListe *C2;  //Chemin de R vers B
  cheminListe *C;   //Chemin de A vers B  passant par R
  
  C=NULL;
  C1=crerChemin(A,R);
  C2=crerChemin(R,B);
  /***Ajouter les points de chemin de A vers R à la liste C ****/
  while(C1!=NULL)
  { C=ajouterEnFin(C,C1->p);
    C1=C1->suiv;
  }
  
  /***Ajouter les points de chemin de R vers B à la liste C ****/
  if (C2!=NULL)C2=C2->suiv;  //pour re pas ajouter le point de repere R 2 fois
  while(C2!=NULL)
  { C=ajouterEnFin(C,C2->p);
    C2=C2->suiv;
  }

 return C;
}

/*****************************************************************/
/*****************************************************************/
/****Fonctions non demandées (on les a définies pour le teste*****/
/*****************************************************************/
cheminListe *AversB()
{  cheminListe *C;
  point p;
    
  C=NULL;
  p=A;
  C=ajouterEnFin(C,A);
  
  if (A.x<=B.x)
  //deplacement à droite/
  while(p.x<B.x)
  { p.x=p.x+1; 
    p.y=A.y; 
    C=ajouterEnFin(C,p);
  }
  else
   /*deplacement à gauche*/
  while(p.x>B.x)
  { p.x=p.x-1;  
    p.y=A.y; 
    C=ajouterEnFin(C,p);
  }
  
  
  if (A.y>=B.y)
  /*deplacement vers le bas*/
  while(p.y>B.y)
  { p.x=B.x; 
    p.y=p.y-1;
    C=ajouterEnFin(C,p);
  }
  else
  
  /*deplacement vers le haut*/
  while(p.y<B.y)
  { p.x=B.x; 
    p.y=p.y+1;; 
    C=ajouterEnFin(C,p);
  }
 return C;
}
/*******************************************************/
void affichetabC()
{ int i,j;
 for (i=0;i<NC;i++)
  {  printf("tabC[%d]=",i);
     for (j=0;j<Max && tabC[i][j].x!=-1;j++)
     { if(tabC[i][j].x!=-1)
       printf("(%d,%d),",tabC[i][j].x,tabC[i][j].y);
     }
     printf("\n");
  }
}
/************************************************************/
void afficheCheminHV()
{ int i;
  for (i=0;i<Max;i++)
  { if(C[i].x!=-1)
    printf("(%d,%d)-->",C[i].x,C[i].y);
  }
}
/**********************************************************/
