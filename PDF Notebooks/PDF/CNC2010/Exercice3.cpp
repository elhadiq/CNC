#include<stdio.h>
#include <conio.h>
#include <stdlib.h>
//////////////////////////////////////
typedef struct
{ 
  unsigned long num ; // numéro de la facture
  char *nom;          // adresse sur le nom du client
  float prixHT ;      // le prix hors taxe à payer en dh
  int an_limite ;     // année limite de paiement
} facture ;
//////////////////////////////////////
typedef struct tliste
{ facture info ;
  struct tliste *suiv;
} liste;       // liste chaînée qui contiendra la liste des factures
//////////////////////////////////////
const int as=2010 ; // année du système
typedef liste *lc;
lc premier;

lc dernier; //necessaire pour ajouter des éléments à la fin de la liste
//////////////////////////////////////
liste *CreerMaillon(facture f)
{ liste *pm=(liste *)malloc(sizeof(liste));
  if(pm!=NULL)
  {pm->info=f;
   pm->suiv=NULL;
  }
  return pm;
}
//////////////////////////////////////
void creerpremier(facture f)
{ liste *pm=CreerMaillon(f);
  if(pm!=NULL)
  { pm->info=f;
    pm->suiv=NULL;
    premier=pm;
    dernier=pm;
  }
}
///////////////////////////////////////
void ajouter(facture f)
{ liste *pm=CreerMaillon(f);
  if(pm!=NULL)
  { pm->info=f;
    pm->suiv=NULL;
    dernier->suiv=pm;
    dernier=pm;
  }
}
///////////////////////////////////////
void creerListe()
{  facture f;
   f.num=1; f.nom="Alami"; f.prixHT=400;  f.an_limite=2005;
   creerpremier(f);
   f.num=2; f.nom="Fikri"; f.prixHT=100;  f.an_limite=2008;
   ajouter(f);
   f.num=3; f.nom="Chaouki"; f.prixHT=100; f.an_limite=2007;
   ajouter(f);
   f.num=4; f.nom="Faiz"; f.prixHT=3000; f.an_limite=2010;
   ajouter(f);
   f.num=5; f.nom="Haimoud"; f.prixHT=2500; f.an_limite=2012;
   ajouter(f);
}
///////////////////////////////////////
void afficheListe()
{  lc ptr=premier;
   while(ptr!=NULL)
   {  printf("%lu\t%s\t\t%.2f\t\t%d\n",ptr->info.num,ptr->info.nom,ptr->info.prixHT,ptr->info.an_limite);
      ptr=ptr->suiv;
   }
}
//3-1//////////////////////////////////
unsigned long nombre()
{  unsigned long n=0;
   lc ptr=premier;
   while(ptr!=NULL)
   {  n++;
      ptr=ptr->suiv;
   }
   return n;
}
//3-2//////////////////////////////////
void supprime(unsigned long val)
{  lc ptr1=premier; 
   lc ptr2=premier;
   short trouve=0;
   while(ptr1!=NULL)
   { if (ptr1->info.num==val)
     {trouve=1;break;}
      ptr2=ptr1;
      ptr1=ptr1->suiv;
   }
   if(trouve==1)
    {   //Mise à jour des numéro des factures
        unsigned long num;
        num=ptr1->info.num;
        lc ptr3=ptr1->suiv;
        while(ptr3!=NULL)
         {ptr3->info.num=num++;
          ptr3=ptr3->suiv;
         }        
        
        //Supprimer la facture       
        if (ptr1==premier) 
            premier=ptr1->suiv;
          else
           ptr2->suiv=ptr1->suiv; //su
          
          free(ptr1);
    }
   else
   printf("Valeur de %d ne coresspond a aucune facture\n",val);
}
//3-3//////////////////////////////////
unsigned long numero()
{  lc ptr=premier;
   while(ptr!=NULL)
   {  if(ptr->info.an_limite>=as)
       return ptr->info.num;
       
      ptr=ptr->suiv;
   }
   return 0;
}
//3-4//////////////////////////////////
void maj_liste()
{
  lc ptr=premier;
   while(ptr!=NULL)
   {  if(ptr->info.an_limite<as)
       {  int n=as-ptr->info.an_limite;
          for(int i=1;i<=n;i++)
           {  float prix=ptr->info.prixHT;
              ptr->info.prixHT=prix+prix*10/100;
           }
       }       
      ptr=ptr->suiv;
   }
}
//3-5//////////////////////////////////
float total_TTC()
{  float total=0;
  lc ptr=premier;
   while(ptr!=NULL)
   {  total=total+ptr->info.prixHT;
      ptr=ptr->suiv;
   }
   return (total+total*19/100);
}
/////////////////////////////////////////
main()
{
  creerListe();
  printf("\nNombre de factures dans la liste est: %lu\n",nombre());
  printf("\n\n\t\tListe des factures avant suppression\n\n");
  afficheListe();
  
  //unsigned long n;
  //printf("\n\nDonner le numero de la facture a supprimer:");
  //scanf("%lu",&n); //supprime(n);
  supprime(3);
   
  printf("\n\n\t\tListe des factures apres suppression\n\n");
  afficheListe();
  
  printf("\nNombre de factures dans la liste est: %lu\n",nombre());
   
  printf("\nLe plus petit numero de la facture dont l'annee >=%d est %lu\n",as,numero());
  
  maj_liste();
  printf("\n\n\t\tListe des factures apres mise a jour\n\n");
  afficheListe();
  
  printf("\n\nSomme des prix totaux TTC des factures %.2f\n\n",total_TTC());
  getch(); 
}
