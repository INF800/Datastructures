#include <stdio.h>
 

int func1(int n)
{
    if(n>0)
    {
        return func1(n-1) + n;
    }
    return 0;
}


int main()
{
    int a = 5;
    printf("%d", func1(a)); //15
}
