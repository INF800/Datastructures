#include <stdio.h>

#include <stdio.h>

void ascending_recursive_func(int a)
{
    if (a>0)
    {
        printf("%d", a);
        ascending_recursive_func(a-1);
    }
}

void descending_recursive_func(int a)
{
    if (a>0)
    {
        descending_recursive_func(a-1);
        printf("%d", a);
    }
}


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
    int x;
    x = 3;
    //ascending_recursive_func(x); // 321
    //descending_recursive_func(x); // 123
    int a = 5;
    printf("%d", func1(a));
    
}
