#include <stdio.h>

void ascending_recursive_func(int a)
{
    if (a>0)
    {
        printf("%d", a);
        ascending_recursive_func(a-1);
    }
}

int main()
{
    int x;
    x = 3;
    //ascending_recursive_func(x); // 321
    
}
