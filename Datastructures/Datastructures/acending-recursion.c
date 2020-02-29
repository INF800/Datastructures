#include "acending-recursion.h"

void func1(int a)
{
    if (a>0)
    {
        printf("%d", a);
        func1(a-1);
    }
}

int main()
{
    int x;
    x = 3;
    func1(x);
}
