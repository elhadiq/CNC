#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int L1=27, L2=4;
char Claire[L1+1]="Ceci est un Texte en Claire";
char Clef[L2+1]="ABCD";
char Chiffre[L1+1];
char K[256];
int  S[256];

/********************************************************************/
/***********Phase  1 Algorithme d'ordonnacement clé (KSA)************/
/********************************************************************/

/***********************************************************************/
/***********Question 1 Initialisation du tableau S avec l'identité******/
/**********************************************************************/
void identiteS()
{
 int i;
 for(i=0;i<256;i++)
 S[i]=i;
}
/****************************************************************/
/***********Question 2 Initialisation du tableau K avec clé******/
/****************************************************************/
void initialiserK()
{int i,j;
  for(i=0,j=0;i<256;i++,j++)
    { if(j==L2) j=0;  // peut être remplacé par j=j%L2;  
      K[i]=Clef[j];
    }
}

//ou bien
void initialiserK2()
{
       int i=0;
       for(i=0;i<256;i++)
       K[i]=Clef[i%L2];
}

void initialiserK3()
{
       
       
}
/******************************************/
/***********Question 3 Permutation ********/
/*****************************************/
void permuterS(int i, int j)
{
 int temp;
 temp=S[i];
 S[i]=S[j];
 S[j] =temp;
}
/******************************************/
/***********Question 4 Algorithme KSA******/
/******************************************/
void KSA()
{
  identiteS();
  initialiserK();
  
  int i,j;
  for(i=0;i<256;i++)
  {
    j=(j+S[i]+K[i])%256;
    permuterS(i,j); 
  }
}

/********************************************************************/
/***********Phase  2 Pseudo Random Generator (PRGA)******************/
/********************************************************************/

/***************************************************/
/***********Question 5  Décomposition binaire *****/
/**************************************************/
void decomposer(int bit[],int nombre)
{
   int i;
   for(i=0;i<=7;i++)
   {bit[i]=nombre%2;
    nombre=nombre/2;
   }
}
/***************************************************/
/***********Question 6  puissance de deux **********/
/**************************************************/
int deuxPuissance(int n)
{
  if(n==0) return 1;
  return 2*deuxPuissance(n-1);
}
/*********************************************************************/
/***********Question 7  valeur décimale d'un nombre binaire **********/
/********************************************************************/
int decimal(int bit[])
{
  int n=0;
  for(int i=0;i<=7;i++)
  n=n+bit[i]*deuxPuissance(i);
  
  return n;
}
/*********************************************************************/
/***********Question 8  valeur décimale d'un nombre binaire **********/
/********************************************************************/
int ouExclusif(int x, int y)
{
   int bitx[8];
   int bity[8];
   int bit[8];
   
   decomposer(bitx,x);
   decomposer(bity,y);
   for(int i=0;i<=7;i++)
   {
    if(bitx[i]==1 && bity[i]==1) 
        bit[i]=0;
    else
        bit[i]=(bitx[i]||bity[i]);
   }
   
   return decimal(bit);
}
/*************************************************/
/***********Question 9 Algorithme PRGA **********/
/************************************************/
void PRGA()
{
     int i,j,a;
     i=0;
     j=0;
     int octet;
     for(a=0;a<L1;a++)
     {
       i=((i+1)%256);
       j=((j+Claire[i])%256);
       permuterS(i,j); 
       octet=S[(S[i]+S[j])%256];
       Chiffre[a]=ouExclusif(Clef[a],octet);
     }
}
/*************PARTIE B*************************************/
/**********************************************************/
/***********Question 10 Chiffrement d'un fichier**********/
/*********************************************************/

/**********************Fonction supposée déjà définie******/
char *RC4Chaine(char *Claire,int L, char *Clef)
{
     char *Chiffre=(char*) malloc(L+1);
     int i,j,a;
     i=0;
     j=0;
     int  L2=strlen(Clef);
     char K[256];
     int  S[256];
     
     int octet;
     
    //****PHASE 1:   KSA()********/
    // identiteS();
    for(i=0;i<256;i++)  S[i]=i; 
                                
    //initialiserK();
    for(i=0,j=0;i<256;i++,j++)
    { if(j==L2) j=0;  // peut être remplacé par j=j%L2;  
      K[i]=Clef[j];
    }
    //permutation
    for(i=0;i<256;i++)
    {
     j=(j+S[i]+K[i])%256;
     permuterS(i,j); 
    }
  
   //****PHASE2:   PRGA()****/
     for(a=0;a<L;a++)
     {
       i=((i+1)%256);
       j=((j+Claire[i])%256);
       permuterS(i,j); 
       octet=S[(S[i]+S[j])%256];
       Chiffre[a]=ouExclusif(Clef[a],octet);
     }
  return Chiffre;
}
/******************************************/
void RC4Fichier(char *fich,char *Clef, char *fichChiffre)
{
  FILE *entree=fopen(fich,"r");
  FILE *sortie=fopen(fichChiffre,"w");
  
  char ligne[81];
  char *ch;
  
  while(fgets(ligne,80,entree))
  {  ch=RC4Chaine(ligne,strlen(ligne),Clef);
     fputs(ch,sortie);
  }
  
  fclose(entree);
  fclose(sortie);
}

/******************************************/

/******************************************/
/***********Programme Principal **********/
/****************************************/


main()
{
  initialiserK();
  printf("***intialiserK():\n");
  for(int i=0;i<256;i++)
  printf("%c ",K[i]);
  
  printf("\n");
  
  
  KSA();
  int t[8]; 
  decomposer(t,11);
  printf("%d\n",decimal(t));
  printf("%d\n",ouExclusif(5,6));
  PRGA();
  
  
  RC4Fichier("Test.txt",Clef, "Test2.txt");
  
  printf("Fichier Test.txt est chiffre");
  
  getch();
}
