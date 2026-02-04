#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>



/*Prototypes des fonctions demandées*/
int  comment(char instr[]);
void supprime_espaces1(char instr[]);   //Version1
void supprime_espaces2(char instr[]);   //Version2
void supprime_espaces3(char instr[]);  //Version2

int motcle(char mot[]);
int identificateur(char id[]);

int  analyserInstruction(char instr[]);
void analyseSource(char source[]);

/*****Constantes et variables globales****/
#define N 5
char tmotscles[N][80]={"entier","reel","repeter","si","sinon"};



/****** Programme principal (non demandé) ****/
main()
{
 char *inst;
 inst=(char*)malloc(100*sizeof(char));
 
 /*A.1:*/
 printf("A.1 Test d'un commentaire:\n");
 strcpy(inst,"\\* explication *\\");
 printf("comment(\"%s\")\tretourne \t: %d\n",inst,comment(inst));
   
 strcpy(inst,"explication *\\");
 printf("comment(\"%s\")\tretourne \t: %d\n",inst,comment(inst));
   
 
 /*A.2*/
 printf("\nA.2 Suppression d'espaces multiples dans une instruction\n");
  strcpy(inst , "    repeter     (max<10)      max++;");
  printf("Instruction avec espaces consicutifs : ");
  printf("\"%s\"\n",inst);
  printf("Instruction sans espaces consicutifs : ");
  supprime_espaces3(inst);
  printf("\"%s\"\n",inst);
  
  /*B.1*/
  printf("\nB.1: Verification d'un mot cle\n");
  printf("motcle(\"si\") \tretourne\t: %d\n",motcle("si"));
  printf("motcle(\"pour\") \tretourne\t: %d\n",motcle("pour"));


  /*B.2*/
  printf("\nB.2: validite d'un identificateur:\n");
  printf("identificateur(\"P 1\") \tretourne\t: %d\n",identificateur("P 1"));
  printf("identificateur(\"1P\") \tretourne\t: %d\n",identificateur("1P"));
  printf("identificateur(\"si\") \tretourne\t: %d\n",identificateur("si"));
  printf("identificateur(\"P1\") \tretourne\t: %d\n",identificateur("P1"));
  
  /*C.1*/
  printf("\nC.1: Analyse d'une instruction\n");
  printf("analyserInstruction(\"var=250\") \t\tretourne\t: %d\n",analyserInstruction("var =250"));
  printf("analyserInstruction(\"var =250;\") \tretourne\t: %d\n",analyserInstruction("var =250;"));
  printf("analyserInstruction(\"reel x=10\") \tretourne\t: %d\n",analyserInstruction("reel x=10"));
  printf("analyserInstruction(\"reel x=10;\") \tretourne\t: %d\n",analyserInstruction("reel x=10;"));
  strcpy(inst,"\\* explication *\\");
  printf("analyserInstruction(\"%s\") \tretourne\t: %d\n",inst,analyserInstruction(inst));  
      
  /*C.2*/      
  printf("\nC.2 Analyse d'un fichier source:\n");
  analyseSource("sourcePL");
  
  free(inst);
 getch();
}

/**************************/
/*Définition des fonctions*/
/**************************/

/*Partie A : Gestion des Commentaires et des espaces*/
/****************************************************/

/*Question A-1 : Test d'un commentaire*/
/**************************************/
int comment(char instr[])
{
 int l=strlen(instr);
 
 if(instr[0]!='\\' || instr[1]!='*' || instr[l-2]!='*' || instr[l-1]!='\\')
    return 0;
    
    return 1;
}

/*Question A-2 : Suppression d'espaces multiples dans une instruction*/
/*********************************Version 1**************************/
void supprime_espaces1(char instr[])
{
  int i,j;
  i=0;
  while(instr[i]!='\0')
  {
     if(instr[i]==' '  && instr[i+1]==' ' )
       {  for(j=i;instr[j]!='\0';j++) 
          instr[j]=instr[j+1];  //decalage vers la gauche
        
       }    
    else
      i++;
  }
 }
 /*********************************Version 2**************************/
 void supprime_espaces2(char instr[])
{
  int i,j,k;
  for(i=0;instr[i]!='\0';i++)
  {
     if(instr[i]==' '  && instr[i+1]==' ' )
       { 
        /*se positionner sur le 1er caractere non vide*/ 
         for(j=i+1; instr[j]!='\0' && instr[j]==' ' ; j++); 
        
         k=i+1;       
         while(instr[j]!='\0')
         { instr[k]=instr[j];  //decalage vers la gauche
           k++; j++;
         }
         instr[k]='\0';
       }    
  
  }
 }
 /*********************************Version 3**************************/
  void copier(char *ch1, char* ch2)
  { int i;
    for(i=0;ch2[i]!='\0';i++)
      ch1[i]=ch2[i];
      
   ch1[i]='\0';   
  }
 /*********************************************************************/
  void supprime_espaces3(char instr[])
  {int i,j;
   for(i=0;instr[i]!='\0';i++)
   {
     if(instr[i]==' '  && instr[i+1]==' ' )
     { 
        /*se positionner sur le 1er caractere non vide*/ 
         for(j=i+1; instr[j]!='\0' && instr[j]==' ' ; j++); 
         
         /*copier la partie de la chaine qui commence de j vers la position i+1*/
         copier(&instr[i+1],&instr[j]);
     }      
   }
  }
  
/*Partie B : Reconnaissance des mots-clés et des identificateurs*****/
/*******************************************************************/


/*Question B-1 : Vérification d'un mot clé*/
/******************************************/
int motcle(char mot[])
{
 int i;
 for(i=0;i<N;i++)
   if(strcmp(tmotscles[i],mot)==0)
    return 1;
    
 return 0;   
}

/*Question B-2 : Vérification d'un identificateur*/
/************************************************/
int identificateur(char id[])
{
  int i;  
  //condition C1
  if(strlen(id)>=80) return 0;

  //condition C2  
  for(i=0;id[i]!='\0';i++)
    if(id[i]==' ') return 0;
  
  //condition C3
  if(id[0]>='0' && id[0]<='9') return 0;
  
  //condition C4
  if(motcle(id)) return 0;
  
  return 1;
}

/*Partie C : Implémentation de l'analyseur lexical*****/
/******************************************************/


/*Question C-1 : Analyse d'une instruction*************/
/*******************************************************/
int analyserInstruction(char instr[])
{
  int i,trouve;
  char *mot,*ligne;
  char *nomfichier="c:\\fmotscles.txt";  //Nom physique
  FILE *F;                               //Nom logique
  
  if(comment(instr)==1) return 1;
  
   mot=(char*)malloc((strlen(instr)+1)*sizeof(char));
   ligne=(char*)malloc((strlen(instr)+1)*sizeof(char));
    
   i=0;
   while(instr[i]!='\0' && instr[i]!=' ')
   { mot[i]=instr[i];
     i++;
   }
   mot[i]='\0';
   
   /*verifier si le 1er mot ne se termine pas par un espace */
   if(instr[i]!=' ') return 0;
   
    /*verifier si le 1er mot est un mot cle */
    
    /*ouvrir lme fichier qui contient les mots clés du langage*/
    F=fopen(nomfichier,"r");
    trouve=0;
    while( fgets(ligne,strlen(instr),F)!=NULL && !trouve)
    {
      ligne[strlen(ligne)-1]='\0';  //supprimer \n à la fin de ligne lu par fgets    
      if(strcmp(mot,ligne)==0) trouve= 1;
    }
    fclose(F);

    /*si le mot n'est pas trouvé*/
    if (!trouve) return 0;
    
    /*si l'instruction ne se termine pas par ; */
    if(instr[strlen(instr)-1]!=';') return 0;
    
    return 1;
}
/*Question C-2 : Analyse d'un fichier source*************/
/********************************************************/
void analyseSource(char source[])
{
     FILE *F;
     int i;
     char ligne[255];
     i=1;
     F=fopen(source,"r");
     int n=0;
    printf("Les numeros de lignes correspondants a des instructions incorrectes sont: ");
    while( fgets(ligne,255,F)!=NULL)
    {
      ligne[strlen(ligne)-1]='\0';  //supprimer \n à la fin de ligne lu par fgets    
      if(analyserInstruction(ligne)==0) 
      printf("%d ",i);
      i++;n++;
    }
    if(n==0) printf("Succes\n");
    fclose(F);
}


