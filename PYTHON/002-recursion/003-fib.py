def func(n):
    '''
    Exponential growth func
    > O(2^n)
    '''
    if n==0:
        return 0
    if n==1:
        return 1
    
    prev = func(n-1)
    next = func(n-2)
    return (prev + next)

#print(func(1))

def f2(n):
    if n==0: return 0
    if n==1: return 1
    
    fib = None
    
    fir = 0
    sec = 1
    for i in range(2, n+1):
        fib = fir + sec
        
        fir = sec
        sec = fib

    return fib

print(f2(100000))
'''
for i in range(0, 10):
    print(f'idx: {i} \t fib: {f2(i)}')
'''