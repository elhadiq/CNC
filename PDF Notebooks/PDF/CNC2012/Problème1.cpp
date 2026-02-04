#include <conio.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct Liste
 {
  short int partie;
  struct Liste *suiv;
 }ListeNombres;
 
 
 //variable globale
 char s[100];
 
 /***Fonctions non demandées***/
 void copier(char *s1, char *s2)
 {
   int i=0;
   while(s2[i]!='\0')
   {
     s1[i]=s2[i];
     i++;
   }
   s1[i]='\0';
 }
 
 /*********************************/
  int longueur(char* s)
  {
    int i=0;
    while(s[i]!='\0')
    i++;
    
    return i;
  }
/*********************************/
 //Question 1:
 /********************************/ 
 int ChaineChiffres()
 {
   int i=0;
   while(s[i]!='\0')
  { if(s[i]<'0' || s[i]>'9') return 0;
    i++;
  }
  if(i==0) return 0;
   return 1;
 }
/*********************************/
//Question 2:
/********************************/ 
void supprime_zero()
{
  int i=0;
  while(s[i]=='0' && s[i]!='\0')
  i++;
  
  copier(s,s+i);   //copier(s,&s[i]); 
}       
/********************************/     
//Question 3:
/********************************/ 
void additionner(char S1[],char S2[], char SOM[])
{
  int i,j,k;
  char ch;
  for(i=0;S1[i]!='\0';i++);
  for(j=0;S2[j]!='\0';j++);
   
  if(i>j)
      k=i+1;
  else
      k=j+1;

   SOM[k]='\0';
   i--;
   j--;
   k--;
   
  int r=0;
  while(i>=0 && j>=0)
  {
    ch=r+S1[i]+ S2[j]-'0';
    
    if (ch>'9')
       { ch=ch-10;
         r=1;
       }
    else
       r=0;
    
    SOM[k]=ch;
    i--;  j--; k--;
  }
  
  while(i>=0)
  {ch=r+S1[i];
   if (ch>'9')
       { ch=ch-10;
         r=1;
       }
    else
       r=0;

   SOM[k]=ch;
   i--;
   k--;
  }
  
  while(j>=0)
  {ch=r+S2[j];
   if (ch>'9')
       { ch=ch-10;
         r=1;
       }
    else
       r=0;

   SOM[k]=ch;
   j--;
   k--;
  }
  
  SOM[k]=r+'0';   
  if(SOM[k]=='0') copier(SOM,SOM+1);  //Eliminer le zero non significatif 
}
/********************************/ 
 //Question 4:
/********************************/  
ListeNombres *ajouterEnfin(ListeNombres *P,short int n)
{
  ListeNombres *nouv ,*q;
  nouv=(ListeNombres*)malloc(sizeof(ListeNombres));
  if(nouv==NULL) return P;
  
  nouv->partie=n;
  nouv->suiv=NULL;
  
  if(P==NULL) return nouv;
  
  q=P;
  while(q->suiv!=NULL)
     q=q->suiv;
     
     q->suiv=nouv;
  
  return P;
}

/**********************************/
/***********VERSION 1**************/
/**********************************/
ListeNombres *regrouperChiffres(char *S)
{
  ListeNombres *P=NULL;
  int i=0,k;
  short int n;
  while (S[i]!='\0')
  {    
       k=0;                       //compteur de chiffres (au plus 4)
       n=0;
       while (S[i]!='\0' && k<4)  //compter les chiffres
       { n=n*10+S[i]-'0';
         i++;
         k++;
       }
       P=ajouterEnfin(P,n);
  }
  return P;
}
/**********************************/
/***********VERSION 2**************/
/**********************************/
ListeNombres *regrouperChiffres2(char *S)
{ ListeNombres *P=NULL;
  int i=0;
  short int n;
  while (S[i]!='\0')
  {    n=0;
       do{ 
            n=n*10+S[i]-'0';
            i++;
          }while (S[i]!='\0' && i%4!=0) ; //compter les chiffres
      P=ajouterEnfin(P,n);
  }
  return P;
}
/**********************************/
/***********VERSION 3**************/
/**********************************/
ListeNombres *regrouperChiffres3(char *S)
{
  ListeNombres *P=NULL;
  int i,j,k;
  short int n;   
  int l=longueur(S);
  int nbpartie=l/4;  //Nombre de parties à 4 chiffres
  i=0;
  j=1;
  while (j<=nbpartie)
  {    
       k=1;  //compteur de chiffres (au plus 4)
       n=0;  //calculer la valeur formée des 4 caractères
       while (k<=4)  //compter les chiffres
       { n=n*10+S[i]-'0';
         i++;k++;
       }

       P=ajouterEnfin(P,n);
       j++;
  }
  
  //dernière partie
  k=l%4;
  n=0;
  while (k>0) 
  {  n=n*10+S[i]-48;   //n=n*10+S[i]-'0';
     i++;k--;
  }
  
  P=ajouterEnfin(P,n);
  
  return P;
}

/**********************************/
/***********VERSION 4**************/
/**********************************/
ListeNombres *regrouperChiffres4(char *S)
{
  ListeNombres *P=NULL;
  int i=0,j,k;
  short int n;
  while (S[i]!='\0')
  {    
       k=0;                       //compteur de chiffres (au plus 4)
       j=i;
       while (S[j]!='\0' && k<4)  //compter les chiffres
       { j++;k++; }
      
       n=0;
       for(j=1;j<=k;j++)
       {
          n=n*10+(S[i+j-1]-'0');
       }
      
       P=ajouterEnfin(P,n);
     
       i=i+k ;
  }
  
  return P;
}
/********************************/
/********************************/
/********NON DEAMNANDEE**********/
/********************************/
void afficheListe(ListeNombres *p)
{
     int i=1;
     while (p!=NULL)
     {
       printf("partie %d : %d\n",i++,p->partie);
       p=p->suiv;
     }
 
 }
/********************************/    
/********NON DEAMNANDEE**********/    
/********************************/     
main()
{
      copier(s,"000009760004300");
      printf("S=%s\n",s);
     
      //Question 1:
      printf("ChaineChiffres(%s)= %d\n\n",s,ChaineChiffres());
     
      //Question 2
      supprime_zero();
      printf("supprimeZero:%s\n\n",s);
      
      //Question 3
      char s1[100],s2[100],som[101];
      copier(s1,"129782004977");
      copier(s2,"7540229953");
      
      additionner(s1,s2,som);
      printf("%s+%s=%s\n\n",s1,s2,som);
      
      //Question 4:
      copier(s,"8002590300407896420003");
      printf("S=%s\n",s);
      ListeNombres *P=regrouperChiffres(s);
      afficheListe(P);
      
     // copier(s,"330104660000027");
      copier(s,"8002590300407896420003");
      printf("S=%s\n",s);
      P=regrouperChiffres2(s);
      afficheListe(P);
      
 
 getch();
 
}
