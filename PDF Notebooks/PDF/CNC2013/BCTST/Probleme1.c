#include <conio.h>
#include <stdio.h>


#define N 7
float Facture[]  ={340.7, 1800.00, 56.00, 1800.00, 456.95, 28.45, 276.25};
int   tabLimite[]={2011,  2015   , 2013 , 2012   , 2013  , 2011 , 2014};
int   an=2013; 
main()
{
 int i,j;
 printf("Tableau Facture\t\t:");
 for(i=0;i<N;i++)printf("%.2f\t",Facture[i]);
 
 printf("\nTableau tabLimite\t:");
 for(i=0;i<N;i++)printf("%d\t",tabLimite[i]);
 
 
 /*Question 1: Les factures les plus élevées*/
 /*Question 1.a: Le plus grand d'une facture*/
 float maxMontant;
 //int i,j;
 maxMontant=Facture[0];
 for(i=1;i<N;i++)
 if(Facture[i]>maxMontant) maxMontant=Facture[i];
 
 printf("\n\nLe plus grand montant des facture : %.2f\n",maxMontant),
 
 /*Question 1.b: Les numéros des factures les plus élevées*/
 printf("\nLes numeros des factures les plus elevees sont: ");
 for(i=0;i<N;i++)
   if(Facture[i]==maxMontant)
     printf("%d\t",i+1);
  
 /*Question 2: Tri des factures par ordre croissant de leurs montants**/
 int tabNum[N];
 int aux;
 /*Initialisation du tableau tabNum*/
 for(i=0;i<N;i++)tabNum[i]=i+1;
 
 /* Trier le tableau tabNum en fonction de valeur des Factures*/
 for(i=0;i<N-1;i++)
  for(j=i+1;j<N;j++)
   if(Facture[tabNum[i]-1] > Facture[tabNum[j]-1]) 
   {      
      aux=tabNum[i];
      tabNum[i]=tabNum[j];
      tabNum[j]=aux;
   }
 

 /*Afficher le Tableau tabNum*/
 printf("\n\ntabNum=");
 for(i=0;i<N;i++)
 printf("%d\t",tabNum[i]);
 
/*Question 3: Augmentation forfaitaire**/
   for(i=0;i<N;i++)
     if(tabLimite[i]<an)
       Facture[i]=Facture[i]*1.1;

 printf("\n\nAnnee en cours : %d\n",an);
 printf("\nTableau Facture Apres augmentation:\n");
 for(i=0;i<N;i++)printf("%.2f\t",Facture[i]);

getch();
}
