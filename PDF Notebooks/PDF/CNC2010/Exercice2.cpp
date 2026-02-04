#include<stdio.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>
//////////////////////////////////////
/*****Fonctions*///////////////////////
/////////////////////////////////////
void supprimerEspacesDebut(char *s)
{
	int i,j;
	i=0;
	while(s[i]==' ' && s[i]!='\0')
		i++;
	if(i!=0)
	{
		j=0;
		while(s[j]!='\0')
		{
			s[j]=s[j+i];
			j++;
		}
	}
}
/////////////////////////////////////////////////
void supprimerEspacesFin(char * s)
{
	int i;
	i=strlen(s)-1;        //for(i=0;s[i];i++);i--;
	while(s[i]==' ')
		i--;
	s[i+1]='\0';
}
//////////////////////////////////////////////////////
void supprimerEspacesInterieur(char *s)
{
	int i, j, k;
	i=0;
	while(i<strlen(s)-1)
	{
		if(s[i]==' ' && s[i+1]==' ')
		{
			j=1;
			while(s[i+j]==' ')
				j++;
			for(k=i; k<strlen(s);k++)
				s[k]=s[k+j-1];
		}
		i++;
	}
}
/////////////////////////////////////////////////////
main()
{
	char *s;
	int i;
	s=(char*)malloc(30*sizeof(char));
	printf("Tapez une chaine:");
    gets(s);
	printf("[%s]\n",s);
	supprimerEspacesDebut(s);
	printf("[%s]\n",s);
	supprimerEspacesFin(s);
	printf("[%s]\n",s);
	supprimerEspacesInterieur(s);
	printf("[%s]\n",s);
	free(s);
getch();
}

