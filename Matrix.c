#include<stdio.h>
int main()
{int r,c, a[r][c], b[r][c], sum[r][c];
printf("Enter number of rows (between 1 and 100): ");
scanf("%d",&r);
printf("\nEnter number of columns (between 1 and 100): ");
scanf("%d",&c);
printf("\n\nEnter elements of 1st matrix:\n");
for(int i=0;i<r;++i)
{ for(int j=0;j<c;++j)
{
printf("\nEnter element a[%d][%d]:",i+1,j+1);
scanf("%d",&a[i][j]);}}
printf("\nEnter elements of 2nd matrix:\n");
for(int i=0;i<r;++i)
{
    for(int j=0;j<c;++j)
    {
        printf("\nEnter element a%d%d: ",i+1,j+1);
    scanf("%d",&b[i][j]);
    }
}
/*Adding Two matrices */
for(int i=0;i<r;++i)
for(int j=0;j<c;++j)
sum[i][j]=a[i][j]+b[i][j];
printf("\nSum of two matrix is: \n\n");
for(int i=0;i<r;++i)
{ for(int j=0;j<c;++j)
{
printf("%d ",sum[i][j]);
if(j==c-1)printf("\n\n");
}}
return 0;
}
