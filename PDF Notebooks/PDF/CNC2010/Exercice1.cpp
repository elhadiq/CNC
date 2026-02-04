#include <stdio.h>
#include <conio.h>

unsigned long int puiss16(unsigned int i)
{
  if (i==0)
     return 1;
   else
     return 16*puiss16(i-1);
}

int coeff16(unsigned long int m,int i)
{
  unsigned long int r=m;
  int j=0;
  while (j<=i)
  { r=m%16;
    m=m/16;
    j++;    
  }
     return r;
}

main()
{   unsigned long int N;
    do
    { printf("Donner un nombre entier: ");
      scanf("%ul",&N);
     }while((N<0)||(N>puiss16(8)-1));
     
   // N=4294967295;
   // N=420;
    int c;
    int i=7;
    printf("%lu en Hexadecimale est: ",N);
    do
    { c=coeff16(N,i);
      if(c<=9)
      printf("%d",c);
      else
      printf("%c",c+'a'-10);
      i--;
    }while(i>=0);
    printf("\n Verification %x",N);
 getch();
}
