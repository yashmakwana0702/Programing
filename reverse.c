#include<stdio.h>
int rev(int i);
int main()
{
int i,j,k,l,m=0;
printf("enter how many digit no. you want to reverse \n");
scanf("%d",&k);
printf("enter the number to reverse it.\n");
scanf("%d",&i);
m = rev(i);
printf("the reverse is %d\n",m);
return 0;
}
int rev(int i){
int l,n,j,k;
j=1
while(j<k)
    {
        l=i%10;
        i=i-l;
        i=i/10;
        m = m + l;
        j++;
        m = m * 10;

    }
return m;
}
