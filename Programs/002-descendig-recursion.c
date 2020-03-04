#include <stdio.h>

void descending_recursive_func(int a)
{
    if (a>0)
    {
        descending_recursive_func(a-1);
        printf("%d", a);
    }
}

int main()
{
    int x;
    x = 3;
    descending_recursive_func(x); // 123
}
