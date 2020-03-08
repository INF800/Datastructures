#include <stdio.h>

// prototyp to tell `funcA` that
// `funcB` exists
void funcB(int n);

void funcA(int n)
{
    if (n>0)
    {
        printf("%d", n);
        funcB(n-1);
    }
}

void funcB(int n)
{
    if (n>1)
    {
        printf("%d", n);
        funcA(n/2);
    }
}

int main()
{
    funcA(20); //201998431
}
