// Sum of `n` Natural Numbers using
// Recursion


#include <stdio.h>

// Note: As this is a tail recursion,
// we can convert it into while-loop
// complexity
//  - time  :
//  - space :
int sumOf(int n)
{
    if (n==0)
    {
        return 0;
    }
    else
        return sumOf(n-1) + n;


}

// using while loop
// complexity
//  - time  :
//  - space :
int efficientSumOf(int n)
{
    while (n>0)
    {
        return n + efficientSumOf(n-1);
    }
    return 0;
}

int main()
{
    int n = 100;
    printf("%d", sumOf(n)); // 5050
    
    // efficient approach
    printf("%d", efficientSumOf(n)); // 5050
}
