#include <stdio.h>
 
int x = 0;
int func1(int n)
{
    if(n>0)
    {
        x++;
        return func1(n-1) + x;
    }
    return 0;
}


int main()
{
    int a = 5;
    printf("%d", func1(a)); //25
}
