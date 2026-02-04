#include <conio.h>
#include <stdio.h>

main()
{
 /* Déclarations */
 char texte[80]="Epreuve de la matiere informatique";
 char mot[]="Une";
 int L=strlen(texte);
 int L1=strlen(mot);
 
 printf("texte=\"%s\"\n\n",texte);
 
 /*Question 1: Nombre de mots dans le texte*/
 int i;              /* indice */
 int nbMots;         /* nombre des mots */
 nbMots=0;
 for(i=0;texte[i]!='\0';i++)
   if(texte[i]==' ')  nbMots++;
   
 nbMots++;
 printf("nbMots=%d\n",nbMots);  

 /*Question 2: les longueurs des mots dans le texte*/
 int tlongueur[nbMots];
 int j,k,n;
 i=0;j=0;k=0;
 while(texte[i]!='\0')
 {    n=0;
      while(texte[i]!='\0' && texte[i]!=' ')  
      {i++; n++;}
      
      if(texte[i]==' ' || texte[i]=='\0')  
      {tlongueur[k]=n; 
       k++;
      }
      i++;
 }
 
 for(i=0;i<nbMots;i++)
 printf("\nLongueure du mot %d=%d",i+1,tlongueur[i]);
 
  /*Question 3: Ajout d'un mot au début du texte*/
   printf("\n\ninserer le mot \"%s\" dans le texte \"%s\"",mot,texte);
  /*décalage vers la droite de L+1 cases*/
  i=L;    /*se positionner à la fin de la chaine texte*/
  while(i>=0)
  { texte[i+L1+1]=texte[i];
    i--;
  }
  
  /*insérer le mot*/
  for(i=0;i<L1;i++)
   texte[i]=mot[i];
   
   /*séparer par un espace*/
   texte[i]=' ';
   
   printf("\ntexte=\"%s\"\n",texte);
   
   /*Question 4: suppression du dernier mot du texte*/
   for(i=0;texte[i]!='\0';i++);   /*se positionner à la fin de la chaine texte*/
   while(texte[i]!=' ' && i>=0)   /*se positionner sur le 1er espace de droite*/
     i--;
     
   texte[i]='\0';                 /*marquer la fin de la chaine*/
   
   printf("\nApres supression du dernier mot, text=\"%s\" \n",texte);  
getch();
}
