#include <stdio.h>
int compute_sum(int n)
{
int sum = 0;
for (; n > 0; --n)
sum += n;
printf("%d\n", n); /* 0 is printed */
return sum;
}

int main(void)
{
int n = 3, sum;
printf("%d\n", n); /* 3 is printed */
sum = compute_sum(n);
printf("%d\n", n); /* 3 is printed */
printf("%d\n", sum); /* 6 is printed*/
return 0;}
