
def factorial(n):
    # base condn.
    if n == 1:
        return 1

    return factorial(n-1) * n 

def fac(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    
    return ans

if __name__ == '__main__':
    N = 5
    # print(factorial(N))
    print(fac(N))